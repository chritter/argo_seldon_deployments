# Deployment of Mlflow Model with Language Wrapper and MLflow

Transformers deep learning translator model is saved to MLlflow
as part of experimentation. Now we would like to deploy it via Seldon.

## Model Image Builder

Two major options:
* A) Build image with Python dependencies AND model artifact
	* Image size 3.78GB, but no external dependnecy speeds up deployment
    * pip install takes 360s when building docker image
* B) Possibly: Build image with Python dependencies but WITHOUT artifact, to
    download artifact based on pod env variable


### Challenges of Model

* Dependency on perl script executed as separate process
* Pre-fork gunicorn model loading setup needs to account for deep learning model
