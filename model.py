import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json


class ExpressionClassifier():

    emotions = ["Angry", "Disgust", "Fear",
                "Happy", "Neutral", "Sad", "Surprised"]

    def __init__(self, model_file, weights_file):
        with open(model_file, 'r') as file:
            json_model = file.read()
            self.model = model_from_json(json_model)

        self.model.load_weights(weights_file)

    def return_emotions(self, input):

        self.preds = self.model.predict(input)
        return ExpressionClassifier.emotions[np.argmax(self.preds)]

    def return_probs(self, input):

        self.preds = self.model.predict(input)
        return self.preds
