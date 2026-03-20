import numpy as np
import cv2

def kalibracija(ids, corners, ID_MAP, REAL_POINTS, scale, calibrated):
  
    current_h = None
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
                
                current_h, _ = cv2.findHomography(src_pts, dst_pts)
                calibrated = True
                
            else: print("Neuspesna kalibracija")
    return calibrated, current_h