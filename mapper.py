import cv2
import numpy as np

class WorldMapper:
    def __init__(self):
        src = np.float32([[100,720],[1180,720],[750,400],[530,400]])
        dst = np.float32([[0,10],[10,10],[10,0],[0,0]])
        self.H = cv2.getPerspectiveTransform(src, dst)

    def map_point(self, x, y):
        pt = np.array([[x, y]], dtype='float32')
        pt = np.array([pt])
        mapped = cv2.perspectiveTransform(pt, self.H)
        return mapped[0][0]
