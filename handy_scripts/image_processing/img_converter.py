# Import the dependencies
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-c", "--choice", required=True, help="choice of conversion")
args = vars(ap.parse_args())


drawing = svg2rlg(args["image"])
choice = args["choice"]
if choice == 'pdf':
    renderPDF.drawToFile(drawing, "output.pdf")
if choice == 'png':
    renderPM.drawToFile(drawing, "file.png", fmt="PNG")
