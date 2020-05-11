# import the necessary packages
import os

# define the path to our face detector model
FACE_PROTOTXT = os.path.sep.join(["models", "face_detector",
	"deploy.prototxt"])
FACE_WEIGHTS = os.path.sep.join(["models", "face_detector",
	"res10_300x300_ssd_iter_140000.caffemodel"])

# define the path to our age detector model
AGE_PROTOTXT = os.path.sep.join(["models", "age_detector",
	"age_deploy.prototxt"])
AGE_WEIGHTS = os.path.sep.join(["models", "age_detector",
	"age_net.caffemodel"])

# define the path to our camo detector model
CAMO_MODEL = os.path.sep.join(["models", "camo_detector",
	"camo_detector.model"])