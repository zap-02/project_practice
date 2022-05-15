import cv2
# read two images
src1 = cv2.imread('011.jpg', cv2.IMREAD_COLOR)
src2 = cv2.imread('image6.jpg', cv2.IMREAD_COLOR)

# add or blend the images
dst = cv2.addWeighted(src1, 1, src2, 0.1, 0.0)

# save the output image
cv2.imwrite('12.jpg', dst)


