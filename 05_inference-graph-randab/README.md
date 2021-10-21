# Deployments of Random AB Test Models

Uses the RandomAB Test Static Router. Graph definition in Case 1) and Case 2) are the same.
## Case 1) One pod with Model A and B

Run `apply -f ab_test_1pods.yaml`.

Implementation:
* One `componentSpecs` entry with two containers in `containers` entries.

Outcome:
* Will create one `predictor` with only one deployment, one pod on which both 
model A,B containers run. Orchestrator is also present on the pod.


## Case 2) Two pods with Model A and Model B

Run `apply -f ab_test_2pods.yaml`.

Implementation:

Two `componentSpecs` entries with one container each in `containers`.

Outcome:

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

## helm Chart

Helm chart allows to use both cases Case I and 2 via helm.

Reference:

* Example adapted from https://docs.seldon.io/projects/seldon-core/en/latest/examples/helm_examples.html
* https://docs.seldon.io/projects/seldon-core/en/latest/analytics/routers.html
* https://docs.seldon.io/projects/seldon-core/en/latest/examples/helm_examples.html
* RANDOM_ABTEST definition here: https://docs.seldon.io/projects/seldon-core/en/v0.5.0/reference/seldon-deployment.html
