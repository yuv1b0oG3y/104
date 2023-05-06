import cv2
import numpy as np

img = cv2.imread("solar-system.jpg")

sun = "Sun"
mercury = "Mercury"
venus = "Venus"
earth = "Earth"
mars = "Mars"
jupiter = "Jupiter"
saturn = "Saturn"
uranus = "Uranus"
neptune = "Neptune"

cv2.putText(img, sun, (100, 360), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=4, color=(0, 0, 255))
cv2.putText(img, mercury, (100, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, venus, (170, 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, earth, (270, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, mars, (370, 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, jupiter, (470, 90), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, saturn, (670, 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, uranus, (870, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, neptune, (1070, 260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))


cv2.imshow("display image", img)
cv2.imwrite("image.jpg", img)

cv2.waitKey(5000)