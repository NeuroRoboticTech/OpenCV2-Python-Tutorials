#!/usr/bin/env python

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('../../../../data/messi5.jpg', cv2.IMREAD_COLOR)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

