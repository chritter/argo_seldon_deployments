# Deployment on K8s

* baseline.yaml: deploy baseline model
* port_forward_seldon.sh: port-forward baseline model to localhost 9000
* api_access_curl.sh: send request for translation to model

## AB Testing

Choose second model to test/compare with baseline model.
Choose 2pods setup as I can manage resources per model A (baseline) or B (new) better. Also
I can watch resource usage easier via Grafana as separate pods. Hence use the abtest_2pods.yaml file for deployment.


## Canary

Requires ingress gateway such as istio, currently not on my cluster

### Deployment Speed

* 2min50s+ for new deployment.
* Additional pod-creation time for scaling: 
