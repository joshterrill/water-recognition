import cv2 as cv
import numpy as np

# Color of water [blue green red]
BGR = np.array([249, 192, 157])
upper = BGR + 10
lower = BGR - 10

def read_image(path):
    return cv.imread(path)

def find_mask(image):
    return cv.inRange(image, lower, upper)

def find_contours(mask):
    (_, contours, hierarchy) = cv.findContours(
            mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = np.asarray([contours[i] for i in range(len(contours)) if hierarchy[0][i][2] == -1])
    print("Found %d black shapes" % (len(contours)))
    return contours

# def find_contours(mask):
#     items = cv.findContours(
#             mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     cnts = items[0] if len(items) == 2 else items[1]

#     print("Found %d black shapes" % (len(cnts)))
#     return cnts

def show_contours(contours, image):
    cv.drawContours(image, contours, -1, (0, 0, 255), 2)

def show_centers(contours, image):
    for i in contours:
        M = cv.moments(i)
        # print(M)
        if M["m00"] != 0:
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv.drawContours(image, [i], -1, (0, 255, 0), 2)
            cv.circle(image, (cx, cy), 3, (0, 0, 255), -1)
            cv.putText(image, "center", (cx - 20, cy - 20),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            print(f"x: {cx} y: {cy}")

def get_main_contour(contours):
    print(contours.read())
    copy = contours.copy()
    copy.sort(key=len, reverse=True)
    return copy[0]

if __name__ == "__main__":
    image = read_image("example-in-4.png")
    mask = find_mask(image)

    contours = find_contours(mask)
    # contours = contours[0] if len(contours) == 2 else contours[1]
    # main_contour = get_main_contour(contours) 
    # print(main_contour)
    # show_contours(contours, image)
    all = []
    for i in contours:
        # print(len(i))
        if len(i) > 10 and len(i) < 1500:
            all.append(i)
    show_centers(all, image)
    cv.imshow("contours", image)

    key = cv.waitKey(0)