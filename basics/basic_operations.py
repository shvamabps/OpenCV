import cv2

img1 = cv2.imread('opencv/samples/data/messi5.jpg')
img2 = cv2.imread('opencv/samples/data/opencv-logo.png')

print(img1.shape)
print(img2.shape)
print(img1.size)
print(img2.size)
print(img1.dtype)
print(img2.dtype)

b, g, r = cv2.split(img1)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# dst_img = cv2.add(img1, img2)
dst_img = cv2.addWeighted(img1, .9, img2, .1, 0)

cv2.imshow('image', dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
