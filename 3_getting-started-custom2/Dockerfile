FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

# Define environment variable, MODEL_NAME must be name of Wrapper class
ENV MODEL_NAME Model
#ENV API_TYPE REST
# simple model instead of ROUTER, TRANSFORMER etc.
ENV SERVICE_TYPE MODEL
#ENV PERSISTENCE 0

USER seldon

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
# CMD exec seldon-core-microservice $MODEL_NAME $API_TYPE \
#                --service-type $SERVICE_TYPE --persistence $PERSISTENCE
