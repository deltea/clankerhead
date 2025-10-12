import cv2

cam = cv2.VideoCapture(0, cv2.CAP_V4L2)

cv2.namedWindow("Imagetest", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Imagetest", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
	ret, image = cam.read()
	if ret and image is not None:
		cv2.imshow("Imagetest", image)
	k = cv2.waitKey(1)
	if k != -1:
		break

cv2.imwrite("/home/leo/test.jpg", image)
cam.release()
cv2.destroyAllWindows()
