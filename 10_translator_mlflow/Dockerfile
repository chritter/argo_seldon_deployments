FROM python:3.7-slim

RUN apt-get update && apt-get install perl==v5.32.1 -y \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install -r model/requirements.txt
RUN pip install -r requirements_seldon.txt
#RUN conda activate mlflow && pip install -r requirements_seldon.txt

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

# Define environment variable, MODEL_NAME must be name of Wrapper class
ENV MODEL_NAME Model
# simple model instead of ROUTER, TRANSFORMER etc.
ENV SERVICE_TYPE MODEL

# run gunicorn server only with default workers=1, nthreads=10 to allow
# for one request at a time to be processed
CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
