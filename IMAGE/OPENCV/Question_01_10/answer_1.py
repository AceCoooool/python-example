import cv2

#####################################################
# method 1
#####################################################
# Read image
img = cv2.imread("imori.jpg")
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# RGB -> BGR
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

# Save result
cv2.imwrite("answer_1.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#####################################################
# method 2
#####################################################
# # Read image and convert color
# img = cv2.imread("imori.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
# # Save result
# cv2.imwrite("answer_1.jpg", img)
# cv2.imshow("result", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
