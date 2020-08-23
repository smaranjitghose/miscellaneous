# Flask utils
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageOps
import tensorflow.keras
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf


# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'knee_implant.h5'

# Load the model
model = tensorflow.keras.models.load_model(MODEL_PATH)




def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
   # x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds==0:
        preds = "The closest match is Zimmer LPS"
    elif preds==1:
        preds = "The closest match is Smith and Nephew Legion"
    elif preds==2:
        preds = "The closest match is Maxx Freedom"
    elif preds == 3:
        preds = "The closest match is Stryker NRG "
    elif preds == 4:
        preds = "The closest match is Exactech Optertrack"
    else:
        preds="The closest match is Zimmer Persona"

    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(port=5001,debug=True)


