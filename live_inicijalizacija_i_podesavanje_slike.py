import cv2
import numpy as np

def podesavanje_homografije():
    ID_MAP = {23: "UL", 22: "UR", 21: "LL", 20: "LR"}
    REAL_POINTS = {
        "UL": (600, 600), "UR": (2400, 600),
        "LL": (600, 1400), "LR": (2400, 1400)
    }

    table_width, table_height = 3000, 2000
    scale = 0.5 
    out_w, out_h = int(table_width * scale), int(table_height * scale)

    sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    H_fixed = None  
    calibrated = False
    smooth_coords = {} 

    return ID_MAP, REAL_POINTS, table_width, table_height, out_w, out_h, sharpen_kernel, H_fixed, calibrated, smooth_coords, scale


def podesavanje_kamere():
    cap = cv2.VideoCapture(1, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) 
    cap.set(cv2.CAP_PROP_EXPOSURE, -6)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    aruco_params = cv2.aruco.DetectorParameters()
    aruco_params.adaptiveThreshConstant = 10
    aruco_params.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_SUBPIX
    aruco_params.cornerRefinementWinSize = 5
    aruco_params.cornerRefinementMinAccuracy = 0.1
    aruco_params.minMarkerPerimeterRate = 0.03

    detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

    return cap, aruco_dict, aruco_params, detector
