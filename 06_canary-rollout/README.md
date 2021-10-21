# Canary Rollout Example

First use basic model `mock_classifier:1.11.0-dev` via 
`kubectl apply -f main_model.yaml` (e.g. monitor
performance via grafana). Then decide to roll out new model 
`mock_classifier_rest:1.2.4` via `kubectl apply -f canary.yaml`.

Implementation:
* Uses a list of two Predictors (two pairs of componentSpecs+Graph), 
one for main model and one for the canary alternative
model.

Result:
* Each Predictor each hosting their predictor pod and a orchestrator.
* Note: each deployment can be scaled individually


References:
* Based on https://docs.seldon.io/projects/seldon-core/en/latest/examples/ambassador_canary.html