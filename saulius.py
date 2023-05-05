from flask import Flask, request
import tensorflow as tf
import base64
from keras.models import load_model

def load_image_from_base64(base64_string, target_size=(100, 100)):
    img_bytes = base64.b64decode(base64_string)
    img = tf.io.decode_image(img_bytes, channels=3)
    img = tf.image.resize(img, target_size)
    img = img / 255.0
    img = tf.expand_dims(img, axis=0)
    return img

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

def predict_image(model, img):
    pred = model.predict(img)
    return pred[0]

def threshold_human(value):
    non_human_probability = value[0]
    human_probability = value[1]
    threshold = 0.75

    if human_probability >= threshold and non_human_probability <= threshold:
        return str(True)
    else:
        return str(False)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Blank</p>"

@app.route('/is_human', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        param = request.json["image"]

        model = load_model("./human-face.h5")
        img = load_image_from_base64(param)
        pred = predict_image(model, img)
        result = threshold_human(pred)
        
        return result
    else:
        return 'Content-Type not supported!'
