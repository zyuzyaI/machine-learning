import argparse
import pandas
import cv2

# Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image Path")
args = vars(ap.parse_args())

# Reading the image with opencv
img_path = args["image"]
img = cv2.imread(img_path)

#declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv_df = pandas.read_csv("color.csv", names=index, header=None)

# Calculate distance to get color name 
def getColorName(R, G, B):
	minimum = 10000
	for i in range(len(csv_df)):
		d = abs(R - int(csv_df.loc[i, "R"])) + (abs(G - int(csv_df.loc[i, "G"]))) + abs(B - int(csv_df.loc[i, "B"]))
		if d <= minimum:
			minimum = d 
			cname = csv_df.loc[i, "color_name"]
	return cname 

def draw_function(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		print("[INFO] detecting color...")
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x 
		ypos = y 
		b, g, r = img[y, x]
		b = int(b)
		g = int(g)
		r = int(r)
		print("[INFO] done!")

# Set a mouse calllback event on a window
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_function)

# Display image on the window
while True:
	cv2.imshow("image", img)	

	if clicked:
		#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
		cv2.rectangle(img, (20,20), (750, 60), (b, g, r), -1)

		# Creating text string to display (Color name and RGB values)
		text = getColorName(r, g, b) + " R=" + str(r) + " G=" + str(g) + " B=" + str(b)
		cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

		# For very light colors we will display text in black color
		if (r + g + b) >= 600:
			cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

		clicked = False 

	# Break the loop when user hits "esc" key
	if cv2.waitKey(1) & 0xFF ==27:
		break

cv2.destroyAllWindows()