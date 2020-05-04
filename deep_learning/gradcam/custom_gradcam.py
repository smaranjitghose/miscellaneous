from gradcam import GradCAM
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-m", "--model", type=str, required=True,
	help="path to the model")
ap.add_argument("-wd", "--width", type=int, required=True,
	help="width of the image")
ap.add_argument("-ht", "--height", type=int, required=True,
	help="height of the image")
ap.add_argument("-l", "--layer", type=str, default="None",
	help="gradcam of specific layer")
args = vars(ap.parse_args())

# load the custom model and print summary()
model = load_model(args["model"])
model.summary()

image = args["image"]
w, h = args["width"], args["height"]
orig = cv2.imread(image)
resized = cv2.resize(orig, (w, h))

# load the input image from disk (in Keras/TensorFlow format) and
# preprocess it
image = load_img(image, target_size=(w, h))
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
image = image.astype('float64')

preds = model.predict(image)
i = np.argmax(preds[0])


if args['layer'] == 'None':
	cam = GradCAM(model, i)
else:
    cam = GradCAM(model, i, args['layer'])
    
heatmap = cam.compute_heatmap(image)

# resize the resulting heatmap to the original input image dimensions
# and then overlay heatmap on top of the image
heatmap = cv2.resize(heatmap, (orig.shape[1], orig.shape[0]))
(heatmap, output) = cam.overlay_heatmap(heatmap, orig, alpha=0.5)

# draw the predicted label on the output image
cv2.rectangle(output, (0, 0), (140, 40), (0, 0, 0), -1)
cv2.putText(output, "GradCAM", (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
	0.6, (255, 255, 255), 2)

# display the original image and resulting heatmap and output image
# to our screen
output = np.hstack([orig, heatmap, output])
output = imutils.resize(output, height=400)
cv2.imshow("Output", output)
cv2.waitKey(0)