import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

def load_and_prepare_image(img_path):
    """
    Load an image file and prepare it for prediction.
    """
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded)

def predict_image_content(model, img_array):
    """
    Use the pre-trained model to predict the image's content.
    """
    predictions = model.predict(img_array)
    return decode_predictions(predictions, top=10)[0]

def detect_labels_tensorflow(image_path):
    predictions =''
    # Load the pre-trained MobileNetV2 model
    model = MobileNetV2(weights='imagenet')

    # Prepare the image
    img_array = load_and_prepare_image(image_path)

    # Make predictions
    preds = predict_image_content(model, img_array)

    # Print predictions
    for pred in preds:
        predictions = predictions + ' ' + pred[1] + '\n'
    
    return 'from the image ' + image_path + '\n' + predictions
