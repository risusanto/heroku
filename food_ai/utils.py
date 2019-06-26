from django.shortcuts import render
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.models import model_from_json
import pickle

global graph,model


#initializing the graph
graph = tf.get_default_graph()

#loading our trained model
print("Keras model loading.......")

json_file = open('food_ai/data/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("food_ai/data/model.h5")

encoder = pickle.load(open('food_ai/data/cls_name','rb'))
print("Model loaded!!")

def recognize(img_data):
    img = image.load_img(img_data, target_size=(299, 299))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    # img = img/255
    with graph.as_default():
        preds = model.predict(img)[0]
    
    cls_idx = np.argmax(preds)
    cls_name = encoder[cls_idx]
    acc = "%.2f" % (preds[cls_idx] * 100)

    return cls_name, acc

