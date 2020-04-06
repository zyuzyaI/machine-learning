# import necessary packages 
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np 
import argparse
import imutils
import cv2 

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image") 
ap.add_argument("-w", "--width", type=float, required=True,
        help="width of the left-most object in the image (in cm)")
args = vars(ap.parse_args())

# load the image, convert itto grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)

# perform edge detection, then perform a dilation + erosion to close gaps in between 
# object edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# sort the counturs from left-to-right and, then initialize the distance 
# colors and reference object
(cnts, _) = contours.sort_contours(cnts)
colors = ((0, 0, 255), (240, 0, 159), (0, 165, 255), (255, 255, 0),(255, 0, 255))
refobj = None

# loop over the countours individually 
for c in cnts:
    # if the countur is not sufficiently large, ignore it
    if cv2.contourArea(c) < 100:
        continue

    # compute the rotated bounding box of the contour
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")

    # order the points in the contour such that they appear in top-left, top-right,
    # bottom-right, and bottom-left order, then draw the outline of the rotated 
    # bounding box
    box = perspective.order_points(box)
    # compute the center of the bounding box 
    cX = np.average(box[:, 0])
    cY = np.average(box[:, 1])

    # if this is the first contour we are examining (i.e., the left-most contour),
    # we presume this is the reference object
    if refobj is None:
        print("refobj is none")
        # unpack the ordered bounding box, then compute the midpoint between 
        # the top-left and top-right points, followed by the midpoint between the 
        # top-right and botton-right 
        (tl, tr, br, bl) = box 
        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)

        # compute the Euclidean distance between the midpoints, then construct
        # the reference object
        D = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
        refobj = (box, (cX, cY), D / args["width"])
        continue 

    # draw the contours on the image 
    orig = image.copy()
    cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0),2)
    cv2.drawContours(orig, [refobj[0].astype("int")], -1, (0, 255, 0), 2)

    # stack the reference coordinates and the object coordinates to include 
    # the oject center 
    refCoords = np.vstack([refobj[0], refobj[1]])
    objCoords = np.vstack([box, (cX, cY)])

    # loop over the original points
    for ((xA, yA), (xB, yB), color) in zip(refCoords, objCoords, colors):
        print("come in second")

        # draw circles corresponding to the current points and connect them
        # with a line
        cv2.circle(orig, (int(xA), int(yA)), 5, color, -1)
        cv2.circle(orig, (int(xB), int(yA)), 5, color, -1)
        cv2.line(orig, (int(xA), int(yA)), (int(xB), int(yB)), color, 2)

        # compute the Euclidean distance between the coordinates, and then
        # convert the distance in pixels to distance in units 
        D = dist.euclidean((xA,yA), (xB, yB)) / refobj[2]
        (mX, mY) = midpoint((xA, yA), (xB, yB))
        cv2.putText(orig, "{:.1f}cm".format(D), (int(mX), int(mY - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

        # show the output image
        cv2.imshow("Image", orig)
        cv2.waitKey(0)
        