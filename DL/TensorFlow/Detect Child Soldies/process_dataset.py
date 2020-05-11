# USAGE
# python process_dataset.py --dataset VictorGevers_Dataset --output output

# import the necessary packages
from worker.helpers import detect_and_predict_age
from worker.helpers import detect_camo
from worker import config
from keras.models import load_model
from imutils import paths
import progressbar
import argparse
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input directory of images to process")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory where CSV files will be stored")
args = vars(ap.parse_args())

# initialize a dictionary that will store output file pointers for
# our age and camo predictions, respectively
FILES = {}

# loop over our two types of output predictions
for k in ("ages", "camo"):
	# construct the output file path for the CSV file, open a path to
	# the file pointer, and then store it in our files dictionary
	p = os.path.sep.join([args["output"], "{}.csv".format(k)])
	f = open(p, "w")
	FILES[k] = f

# load our serialized face detector, age detector, and camo detector from disk
print("[INFO] loading trained models...")
faceNet = cv2.dnn.readNet(config.FACE_PROTOTXT, config.FACE_WEIGHTS)
ageNet = cv2.dnn.readNet(config.AGE_PROTOTXT, config.AGE_WEIGHTS)
camoNet = load_model(config.CAMO_MODEL)

# grab the paths to all images in our dataset
imagePaths = sorted(list(paths.list_images(args["dataset"])))
print("[INFO] processing {} images".format(len(imagePaths)))

# initialize the progress bar
widgets = ["Processing Images: ", progressbar.Percentage(), " ",
	progressbar.Bar(), " ", progressbar.ETA()]
pbar = progressbar.ProgressBar(maxval=len(imagePaths),
	widgets=widgets).start()

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	# load the image from disk
	image = cv2.imread(imagePath)

	# if the image is 'None', then it could not be properly read from
	# disk (so we should just skip it)
	if image is None:
		continue

	# detect all faces in the input image and then predict their
	# perceived age based on the face ROI
	ageResults = detect_and_predict_age(image, faceNet, ageNet)

	# use our camo detection model to detect if camouflage exists in
	# the image or not
	camoResults = detect_camo(image, camoNet)

	# loop over the age detection results
	for r in ageResults:
		# the output row for the ages CSV consists of (1) the image
		# file path, (2) bounding box coordinates of the face, (3)
		# the predicted age, and (4) the corresponding probability
		# of the age prediction
		row = [imagePath, *r["loc"], r["age"][0], r["age"][1]]
		row = ",".join([str(x) for x in row])

		# write the row to the age prediction CSV file
		FILES["ages"].write("{}\n".format(row))
		FILES["ages"].flush()

	# check to see if our camouflage predictor was triggered
	if camoResults[0] == "camouflage_clothes":
		# the output row for the camo CSV consists of (1) the image
		# file path and (2) the probability of the camo prediction
		row = [imagePath, camoResults[1]]
		row = ",".join([str(x) for x in row])

		# write the row to the camo prediction CSV file
		FILES["camo"].write("{}\n".format(row))
		FILES["camo"].flush()

	# update the progress bar
	pbar.update(i)

# stop the progress bar
pbar.finish()
print("[INFO] cleaning up...")

# loop over the open file pointers and close them
for f in FILES.values():
	f.close()