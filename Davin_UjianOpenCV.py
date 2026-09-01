import cv2 as cv


images = cv.imread("task.png")
gaussian_blur = cv.GaussianBlur(images,(5,5), 0)


print(images.shape)

y_start = 20
y_end = 450

x_start = 346
x_end = 765

# .copy() makes this an independent array, not a view into `images`
cropping = images[y_start:y_end, x_start:x_end].copy()
gaussian_blur = cv.GaussianBlur(cropping,(5,5), 0)
#3
font = cv.FONT_HERSHEY_COMPLEX
size = 0.5
color = (0, 0, 0)
thickness = 2
text1 = "Davin Chester Limantara"
text2 = "Davin Chester Limantara"
position = (100, 100)

cv.putText(images, text1, position, font, size, color, thickness, cv.LINE_AA)
cv.putText(cropping, text1, position, font, size, color, thickness, cv.LINE_AA)
cv.putText(gaussian_blur, text2, position, font, size, color, thickness, cv.LINE_AA)


cv.imshow("images", images)
cv.imshow("cropped", cropping)
cv.imshow("filtered",gaussian_blur)
cv.imwrite("hasil edit.png",gaussian_blur)
cv.waitKey(0)
cv.destroyAllWindows()