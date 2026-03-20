import cv2
import numpy as np
import socket

from live_inicijalizacija_i_podesavanje_slike import podesavanje_kamere
from live_inicijalizacija_i_podesavanje_slike import podesavanje_homografije
from setup_boje import color_ranges
from setup_boje import osmatracke_zone
from setup_boje import pantry
from citanje_zone import citanje_zone
from kalibracija import kalibracija
import socket
import pyrealsense2 as rs

# Inicijalizacija pipelinea
pipeline = rs.pipeline()
config = rs.config()
pipeline_profile = pipeline.start(config)

device = pipeline_profile.get_device()
depth_sensor = device.first_depth_sensor
if depth_sensor.supports(rs.option.emitter_enabled):
    depth_sensor.set_option(rs.option.emitter_enabled, 0) 


# Podešavanja komunikacije
ESP32_IP = "192.168.43.33"  
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def posalji_podatke(boja, zona):
    poruka = f"{boja}:{zona}"
    sock.sendto(poruka.encode(), (ESP32_IP, UDP_PORT))

# Pozivanje funkcija
ID_MAP, REAL_POINTS, table_width, table_height, out_w, out_h, sharpen_kernel, H_fixed, calibrated, smooth_coords, scale = podesavanje_homografije()
cap, aruco_dict, aruco_params, detector = podesavanje_kamere()

frame = cv2.imread("Test14_Color.png")

print("Sistem pokrenut.")


while True:
    ret, frame = cap.read()
    if not ret:
        print("Ne citam frejm sa kamere")
        break

    
    # Prva obrada slike
    sharpened = cv2.filter2D(frame, -1, sharpen_kernel)
    gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = detector.detectMarkers(gray)

    
    # Kalibracija

    if not calibrated:
            image_points = {}
            if ids is not None:
                for corner, marker_id in zip(corners, ids.flatten()):
                    if marker_id in ID_MAP:
                        cx, cy = corner[0][:, 0].mean(), corner[0][:, 1].mean()
                        image_points[ID_MAP[marker_id]] = (cx, cy)

            if len(image_points) == 4:
                src_pts = np.array([image_points["UL"], image_points["UR"], 
                                    image_points["LL"], image_points["LR"]], dtype=np.float32)
                dst_pts = np.array([REAL_POINTS["UL"], REAL_POINTS["UR"], 
                                    REAL_POINTS["LL"], REAL_POINTS["LR"]], dtype=np.float32) * scale
                
                H_fixed, _ = cv2.findHomography(src_pts, dst_pts)
                calibrated = True
                print("Kalibracija uspesna")
    
   
    #Detekcija boja
   
    if calibrated:
        
        warped = cv2.warpPerspective(frame, H_fixed, (out_w, out_h))

        
        hsv_warped = cv2.cvtColor(warped, cv2.COLOR_BGR2HSV)
        hsv_warped = cv2.GaussianBlur(hsv_warped, (5, 5), 0)
        posalji_podatke("Crvena", 1) 

        # Detekcija
        pantry_bajtovi = citanje_zone(pantry, scale, hsv_warped, color_ranges, warped)
        zone_bajtovi = citanje_zone(osmatracke_zone, scale, hsv_warped, color_ranges, warped)
        posalji_podatke("Crvena", 1)

        # Poruka za ESP
        finalni_paket = bytearray([0xAA]) + pantry_bajtovi + zone_bajtovi + bytearray([0x55])

        try:
            sock.sendto(finalni_paket, (ESP32_IP, UDP_PORT))
        except Exception as e:
            print(f"Greška pri slanju: {e}")

        
        print(f"Poslato: {finalni_paket.hex().upper()}")

        
        cv2.imshow("Fiksni Pogled (Warped)", warped)
        cv2.waitKey(0)
    
    
    cv2.imshow("Kamera Live", frame)

    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord('r'):
        calibrated = False
        H_fixed = None
        print("Sistem resetovan. Ponovite kalibraciju uglova.")


cap.release()
cv2.destroyAllWindows()