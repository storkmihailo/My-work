import cv2

def citanje_zone(posmatrane_zone, scale, hsv_warped, color_ranges, slika):

    paket_bajtova = bytearray()
    
    for zona in posmatrane_zone:

        tip = 1 if "Pantry" not in zona["ime"] else 0

        import re
        brojevi = re.findall(r'\d+', zona["ime"])
        oznaka = int(brojevi[0]) if brojevi else 0

        # Konvertuj mm koordinate u piksele
        x, y, w, h = [int(v * scale) for v in zona["rect"]]

        # Iseci
        roi = hsv_warped[y:y+h, x:x+w]
        
        found_color = "Prazno"
        max_pixels = 0
        
        # Provera boje
        for color_name, limits in color_ranges.items():
            mask = cv2.inRange(roi, limits["lower"], limits["upper"])
            pixel_count = cv2.countNonZero(mask)
            
            # Raspon detekcije
            if pixel_count > (w * h * 0.15) and pixel_count > max_pixels:
                found_color = color_name
                max_pixels = pixel_count
        
        # Vizuelni prikaz 
        color_bgr = (0, 255, 0) if found_color != "Prazno" else (0, 0, 255)
        cv2.rectangle(slika, (x, y), (x + w, y + h), color_bgr, 2)
        cv2.putText(slika, f"{found_color}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_bgr, 2)

        prisutan = 1 if found_color != "Prazno" else 0
        boja_bit = 1 if found_color == "1" else 0
        

        orijentacija_bit = 1 if zona["orijentacija"] == "u" else 0

        # Pakovanje poruke
        # Bajt 1: [Tip(1), ID(6), Prisutan(1)]
        b1 = (tip << 7) | ((oznaka & 0x3F) << 1) | prisutan
        # Bajt 2: [Boja(1), Orijentacija(1), 0]
        b2 = (boja_bit << 7) | (orijentacija_bit << 6)

        paket_bajtova.extend([b1, b2])
        
    return paket_bajtova