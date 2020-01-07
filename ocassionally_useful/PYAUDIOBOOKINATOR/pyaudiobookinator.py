import pyttsx3 # Importing library for converting text to speech
import PyPDF2 # Importing Python PDF playaround library
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,help="path to the PDF Document")
args = vars(ap.parse_args())

pdf_doc = open(args["input"], 'rb')
interpreted_doc = PyPDF2.PdfFileReader(pdf_doc)
speaker = pyttsx3.init()  # Intialize Text to Speech Object

for pages in range(0, interpreted_doc.numPages):
	page = interpreted_doc.getPage(pages) # Get the specific page
	data = page.extractText() # Extract the text data
	speaker.say(data) # Convert it to speech
	speaker.runAndWait() # Play the speech
