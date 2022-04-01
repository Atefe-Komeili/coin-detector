import cv2


# show image
def show(img, title=None):
    cv2.imshow(title, img)
    cv2.waitKey(0)


# read image
base_image = cv2.imread('image.jpg')

# make copy of image to have original image at the end
image = base_image.copy()

# convert to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
show(image, "gray")

# apply binary threshold with OTSU method
otsu_threshold, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, )
show(image, "treshold")

# blur image to remove noise
image = cv2.GaussianBlur(image, (17, 17), 0)
show(image, "blur")

# detection edges in image
image = cv2.cvtColor(cv2.Canny(image=image, threshold1=148, threshold2=255), cv2.COLOR_GRAY2BGR)
show(image, "canny")

# blur image
image = cv2.GaussianBlur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), (7, 7), 0)
show(image, "blur candy")

# find circles in image
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, minDist=30, param1=96, param2=21, minRadius=18, maxRadius=40)

# convert the (x, y) coordinates and radius of the circles to integers
number = 1
for circle in circles[0, :]:
    x, y, r = [int(i) for i in circle]
    # draw the circle
    cv2.circle(base_image, (x, y), r, (0, 255, 0), 2)
    # add number to the center of the circle
    cv2.putText(base_image, str(number), (x - 10, y), cv2.FONT_HERSHEY_PLAIN, 1.2, (60, 76, 250), 2)
    number += 1

cv2.imwrite("result.jpg", base_image)
show(base_image, "image with circles")