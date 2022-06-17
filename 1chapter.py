import cv2

image = cv2.imread("Image/lena.png", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Lena", image)
cv2.waitKey()
cv2.destroyAllWindows()