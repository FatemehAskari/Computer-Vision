import os
import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np
import cv2
import glob

a=[12,5,6,7978,6565689,56578]
findhasdigit=[int(digit) for digit in str(a[4])[::1]]
print(findhasdigit)