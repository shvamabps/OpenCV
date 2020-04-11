import cv2


img = cv2.imread("./opencv/samples/data/lena.jpg", -1)
cv2.imshow("Image", img)


k = cv2.waitKey(5000) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
