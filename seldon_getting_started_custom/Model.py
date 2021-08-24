# predict function modified from https://docs.seldon.io/projects/seldon-core/en/latest/workflow/github-readme.html

from joblib import dump, load
class Model:
    def __init__(self):
        self._model = load("model.joblib", "rb")

    def predict(self, X):
        output = self._model(X)
        return output