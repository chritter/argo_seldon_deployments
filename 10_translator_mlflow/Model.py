# predict function modified from https://docs.seldon.io/projects/seldon-core/en/latest/workflow/github-readme.html

from joblib import dump, load
import logging
from mlflow import pyfunc
import os
import pandas as pd
from datetime import datetime
import socket

logging.basicConfig(format='%(asctime)s (%(levelname)s) %(message)s',
                    level=logging.INFO,
                    datefmt='%d.%m.%Y %H:%M:%S')

class Model:
    def __init__(self):

        with open("version.txt", 'r') as f:
            self.image_version = f.readline().strip()
        with open("model.txt", 'r') as f:
            self.model_version = f.readline().strip()

    def load(self):
        
        # use the load() function to initialize model, else the request 
        # gets stuck. The class gets initialized in the main process
        # before forking/spawning, while load() is called on the spawns
        # see  https://github.com/SeldonIO/seldon-core/issues/2680
        # load mlflow model
        logging.info("load model")
        os.chdir("model")
        self._model = pyfunc.load_model(".")
        os.chdir("../")
        logging.info("loading model done")


    def predict(self, X, features_names=None):

        logging.info(f'received X {X}')
        t_start = datetime.now()
        output = self._model.predict(X)
        inference_time = round((datetime.now() - t_start).total_seconds())
        logging.info(f"inference time [s]: {inference_time}")

        logging.info(f"model output {output}")

        return output

    def health_status(self):
        """
        check if model is working on benchmark example

        Returns:
            [type]: [description]
        """
        sample_test = ["Aujourd hui est un bon jour"]
        response = self._model.predict(sample_test)
        expected_response =  ["Today is a good day"]

        # simple model validation
        assert len(response) == 1, "health check: prediction error, len wrong" 
        assert response == expected_response, f"""health check: 
                    prediction error, wrong translation
                    expected: {expected_response} 
                    received: {response} """

        return response

    def tags(self):

        logging.info(f'preparing tags')

        hostname = socket.gethostname()

        # adding fixed tag to returned metadata
        return {"mode":"dev", "hostname": hostname, 
                "image_version": self.image_version,
                "model_version": self.model_version}