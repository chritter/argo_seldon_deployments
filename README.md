Examples for deployment of ML models on K8s via Seldon Core.
Order according from simple to sohpisticated.

* 1) `01_getting-started`: deploys iris model binary provided by Seldon on Google Cloud Storage with pre-packaged seldon sklearn MLServer.
* 2) `02_getting-started-custom`: Trains iris model, use custom language wrapper (predict class) and build image with s2i, use with MLServer.
* 3) `03_getting-started-custom2`: as example `2_getting-started-custom` but build
image with regular docker file instead of s2i.
* 4) `04_getting-started-custom-mlflow/`: Trains iris model and saves to mlflow. Loads
separate Mlflow Cloud Storage model as deploys with pre-packaged seldon mlflow MLServer.
* 5) `05_inference-graph-randab`: Demos random A/B test with two models leveraging
the seldon RANDOM_ABTEST implementation.
* 6) `06_canary-rollout`: Demos the application of two models via a Canary deployment.
* 7) `07_seldon-grafana-metrics`: Simple deployment with notes about working
with Prometheus/Grafana.
* 8) `08_sklearnserver`: effort to build custom seldon inference server. Not 
pursued further as implementation requires modification of seldon core operator
settings, which is unpractical for deployment at this point.
* 9) `09_text_classifier_mlflow`: trainings NLP classifier model with some
dependencies and saves as custom Python mlflow model. then deployment via
pre-packaged seldon mlflow server.
* 10) `10_translator_mlflow`: deploys Transformers French-to-English 
language translator model. Model mlflow artifact is pulled from minio on k8s.
