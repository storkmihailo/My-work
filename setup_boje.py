import numpy as np
color_ranges = {
    "1": {
        "lower": np.array([95, 110, 50]), 
        "upper": np.array([135, 255, 255])
    },
    "0": {
        "lower": np.array([20, 100, 100]), 
        "upper": np.array([40, 255, 255])
    }
}

x_duzina=200
y_duzina=200

pantry = [
    {"ime": "Pantry_1", "rect": (600, 0, x_duzina, y_duzina), "orijentacija": "n"}, 
    {"ime": "Pantry_2", "rect": (1400, 0, x_duzina, y_duzina), "orijentacija": "n"},
    {"ime": "Pantry_3", "rect": (2200, 0, x_duzina, y_duzina), "orijentacija": "n"},
    {"ime": "Pantry_4", "rect": (0, 700, x_duzina, y_duzina), "orijentacija": "n"},
    {"ime": "Pantry_5", "rect": (700, 700, x_duzina, y_duzina), "orijentacija": "n"},
    {"ime": "Pantry_6", "rect": (1400, 700, x_duzina, y_duzina), "orijentacija": "n"},
    {"ime": "Pantry_7", "rect": (2100, 700, x_duzina, y_duzina), "orijentacija": "n"},
    {"ime": "Pantry_8", "rect": (2800, 700, x_duzina, y_duzina), "orijentacija": "n"},
    
]

x_duzina_b=50
y_duzina_b=160

y_offset=10

osmatracke_zone = [
    {"ime": "11", "rect": (1000, 50, x_duzina_b, y_duzina_b), "orijentacija": "v"}, 
    {"ime": "12", "rect": (1050, 50, x_duzina_b, y_duzina_b), "orijentacija": "v"}, 
    {"ime": "13", "rect": (1100, 50, x_duzina_b, y_duzina_b), "orijentacija": "v"}, 
    {"ime": "14", "rect": (1150, 50, x_duzina_b, y_duzina_b), "orijentacija": "v"}, 

    {"ime": "21", "rect": (1800,  50, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "22", "rect": (1850,  50, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "23", "rect": (1900,  50, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "24", "rect": (1950,  50, x_duzina_b, y_duzina_b), "orijentacija": "v"},

    {"ime": "31", "rect": (75, 260, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "32", "rect": (75, 310, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "33", "rect": (75, 360, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "34", "rect": (75, 410, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},

    {"ime": "41", "rect": (2775, 260, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "42", "rect": (2775, 310, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "43", "rect": (2775, 360, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "43", "rect": (2775, 410, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},

    {"ime": "51", "rect": (1050, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "52", "rect": (1100, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "53", "rect": (1150, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "54", "rect": (1200, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},

    {"ime": "61", "rect": (1750, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "62", "rect": (1800, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "63", "rect": (1850, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},
    {"ime": "64", "rect": (1900, 700, x_duzina_b, y_duzina_b), "orijentacija": "v"},

    {"ime": "71", "rect": (75, 1080, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "72", "rect": (75, 1130, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "73", "rect": (75, 1180, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "74", "rect": (75, 1230, y_duzina_b - y_offset, x_duzina_b),  "orijentacija": "u"},

    {"ime": "81", "rect": (2775, 1080, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "82", "rect": (2775, 1130, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "83", "rect": (2775, 1180, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    {"ime": "84", "rect": (2775, 1230, y_duzina_b - y_offset, x_duzina_b), "orijentacija": "u"},
    
]