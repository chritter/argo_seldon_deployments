# Usage of Python Language Wrapper for trained Iris Model

See IrisTrain.ipynb for model training and steps for deployment.

## Notes

* Environment file `environment` need to contain model name of Model.py file. Also Model.py file needs to contain the class with the same name, Model.
* Adapted parts from example at https://github.com/SeldonIO/seldon-core/blob/master/servers/sklearnserver/sklearnserver/SKLearnServer.py
* Uses Source-to-Image tool (RedHat supported) for faster docker image build, which means no Docker file necessary.
* Test microservice local in debug mode with script
