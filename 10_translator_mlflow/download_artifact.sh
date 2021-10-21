# download artifact

export ARTIFACT_LOCATION="minio-1631912584-local/bucket/mlflow/1/fd5abd139d1d4de6993e2f2cde029142/artifacts/model"

mc cp $ARTIFACT_LOCATION . --recursive

