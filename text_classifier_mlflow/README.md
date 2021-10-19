# Mlflow Sklearn Text Classifier with Language Wrapper

NLP model deployed with Seldon MLFLOW_SERVER.

## Model Training

NLP_Classifier.ipynb: Trains NLP Model with more complex preprocessing pipeline.

As Conda environments exist two:
A) for local development/experimentation purpose: environment.yml
B) for deployment with sklearn server: environment_model.yml. The latter avoids any system
dependency through `--no-builds` and also contains only essential dependencies.


## Deployment
check deployment dir.

### Usage of Minio as S3 Storage

Note that to access minio, seldon needs to have access to the credentials
provided via a secret. The method is to use a specific secret which the 
seldon operator reads. The (at time of writing) current secret setup as
on Seldon page might not work (non-working version in deprecated folder). Instead
I used the deployment/secret_rclone.yaml implementation from the seldon github page which
worked fine. Note that secret_rclone.yaml needs to be deployed in the seldon operator
namespace. 
