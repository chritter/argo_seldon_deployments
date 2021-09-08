
Uses the RandomAB Test Static Router

It will create one predictor (predictive unit) which graph consists of the
two model
It will create two deployments (each with a pod) and one replicaset. One
pod hosts the service orchestrator (https://docs.seldon.io/projects/seldon-core/en/latest/graph/svcorch.html)
which manages the request/response and is used by the main service.

See the Custom Resource under `seldondeployments` in the deployment namespace
for details. Here it is called `seldon-abtest`.

Metrics in Grafana can be viewed via the Seldon Deployment Monitoring 1 dashboard.
However it looks like prometheus pod resource metrics such as `process_cpu_seconds_total`
are only available for the pod hosting the orchestrator.

Reference:

* Example adapted from https://docs.seldon.io/projects/seldon-core/en/latest/examples/helm_examples.html
* https://docs.seldon.io/projects/seldon-core/en/latest/analytics/routers.html
* https://docs.seldon.io/projects/seldon-core/en/latest/examples/helm_examples.html
* RANDOM_ABTEST definition here: https://docs.seldon.io/projects/seldon-core/en/v0.5.0/reference/seldon-deployment.html
