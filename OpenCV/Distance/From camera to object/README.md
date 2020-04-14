## [Find distance from camera to object/marker using Python and OpenCV](https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/)

In order to determine the distance from our camera to a known object or marker, we are going to utilize triangle similarity.

The triangle similarity goes something like this: Let’s say we have a marker or object with a known width W. We then place this marker some distance D from our camera. We take a picture of our object using our camera and then measure the apparent width in pixels P. This allows us to derive the perceived focal length F of our camera:

F = (P x  D) / W

For example, let’s say I place a standard piece of 210 x 297 mm piece of paper (horizontally; W = 210) D = 610 mm in front of my camera and take a photo. When I measure the width of the piece of paper in the image, I notice that the perceived width of the paper is P = 248 pixels.

My focal length F is then:

F = (248px x 610mm) / 297mm = 509.36

As I continue to move my camera both closer and farther away from the object/marker, I can apply the triangle similarity to determine the distance of the object to the camera:

D’ = (W x F) / P

Again, to make this more concrete, let’s say I move my camera  900 mm away from my marker and take a photo of the same piece of paper. Through automatic image processing I am able to determine that the perceived width of the piece of paper is now 170 pixels. Plugging this into the equation we now get:

D’ = (297 x 509.36) / 170 = 889.88 mm

Or roughly 900 mm.

