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

    def health_status(self):
        # check if model is working on test examples or benchmarks

        sample_1 = [2, 2, 2, 3]
        sample_2 = [2, 3, 3, 2]
        response = self.predict([sample_1, sample_2], ["f1", "f2"])

        # simple model validation
        assert len(response) == 2, "health check returning bad predictions" 

        return response

    def tags(self):

        logging.info(f'preparing tags')

        # adding fixed tag to returned metadata
        return {"system":"dev"}