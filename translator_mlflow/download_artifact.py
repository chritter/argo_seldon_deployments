
import logging
import mlflow
from mlflow.tracking import MlflowClient
import shutil
import os
import subprocess  

log = logging.getLogger()
log.setLevel("INFO")

def download(run_id):
    """
    Downloads run into model directory

    Args:
        run_id ([type]): [description]
    """

    server_url = "http://localhost:8088"
    mlflow.set_tracking_uri(server_url)
    
    # Download artifacts
    client = MlflowClient()
    client.download_artifacts(run_id, "model", ".")


if __name__ == "__main__":

    with open("model.txt", 'r') as f:
        run_id = f.readline().strip()

    download(run_id)
