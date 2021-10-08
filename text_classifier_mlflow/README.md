# Mlflow Sklearn Text Classifier with Language Wrapper

* Use the Seldon MLFLOW_SERVER. 
* ..

## Usage of Minio as S3 Storage

Note that to access minio, seldon needs to have access to the credentials
provided via a secret. The (at time of writing) current secret setup as
on Seldon page might not work (non-working version in deprecated folder). Instead
I used the secret_rclone.yaml implementation from the seldon github page which
worked.
