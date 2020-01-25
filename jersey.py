import cv2
import numpy as np

img=cv2.imread("IMG.jpg")
img_original=img.copy()
print("img.shape",img.shape)

img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower mask (0-10)
lower_red = np.array([0,100,100])
upper_red = np.array([20,255,255])
# upper_red = np.array([10,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([150,105,100])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join my masks
mask = mask0+mask1

# set my output img to zero everywhere except my mask
output_img = img.copy()
output_img[np.where(mask==0)] = 0

# or your HSV image, which I *believe* is what you want
output_hsv = img_hsv.copy()
# output_hsv[np.where(mask==0)] = 0
img[mask>0]=(0,102,51)


cv2.imshow("img",img)
cv2.imwrite("jersey.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imshow("img_original",img_original)
# cv2.imshow("Output",output_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()