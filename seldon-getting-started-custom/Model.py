# predict function modified from https://docs.seldon.io/projects/seldon-core/en/latest/workflow/github-readme.html

from joblib import dump, load
import logging

logging.basicConfig(format='%(asctime)s (%(levelname)s) %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d.%m.%Y %H:%M:%S')

class Model:
    def __init__(self):
        self._model = load("model.joblib")

    def predict(self, X, features_names=None):

        logging.info(f'received X {X}')

        output = self._model.predict(X)

        logging.info(f"model output {output}")

        return output