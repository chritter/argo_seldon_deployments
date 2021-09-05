# Simple Seldon Model with Access to Metrics

Deploy model via model_seldon_rest.yaml. Portforward service rest-seldon-model with
ports 9000:8000, then test api with shell scripts.



### Metrics Exposed for Prometheus 




#### Latencies

##### Requsets from ingress to the service orchestsrator (container engine)

* HELP seldon_api_executor_server_requests_seconds_summary A summary of latencies for executor server
* TYPE seldon_api_executor_server_requests_seconds_summary summary
seldon_api_executor_server_requests_seconds_summary_count - e.g. 251
seldon_api_executor_server_requests_seconds_summary - e.g. at quantile=0.5: 0.006337823
bucket also?

* HELP seldon_api_executor_server_requests_seconds A histogram of latencies for executor server
* TYPE seldon_api_executor_server_requests_seconds histogram
seldon_api_executor_server_requests_seconds_sum - e.g. 1.676134387
seldon_api_executor_server_requests_seconds_bucket - e.g. at le=0.01 239
count also?

##### Requsets from service orchestrator to the model container


* HELP seldon_api_executor_client_requests_seconds_summary A summary of latencies for client calls from executor
* TYPE seldon_api_executor_client_requests_seconds_summary summary
seldon_api_executor_client_requests_seconds_summary: e.g. at quantile="0.98: 0.007
seldon_api_executor_client_requests_seconds_summary_count 251
seldon_api_executor_client_requests_seconds_summary_sum 1.493476493

* HELP seldon_api_executor_client_requests_seconds A histogram of latencies for client calls from executor
* TYPE seldon_api_executor_client_requests_seconds histogram
seldon_api_executor_client_requests_seconds_sum 1.490669816
seldon_api_executor_client_requests_seconds_count 251
seldon_api_executor_client_requests_seconds_bucket: le=0.025 251

#### HTTP Status

* HELP promhttp_metric_handler_requests_total Total number of scrapes by HTTP status code.
* TYPE promhttp_metric_handler_requests_total counter 
promhttp_metric_handler_requests_total{code="200"} 4010
promhttp_metric_handler_requests_total{code="500"} 0
promhttp_metric_handler_requests_total{code="503"} 0


#### Memory

* HELP process_virtual_memory_max_bytes Maximum amount of virtual memory available in bytes.
* TYPE process_virtual_memory_max_bytes gauge
process_virtual_memory_max_bytes -1

* HELP process_virtual_memory_bytes Virtual memory size in bytes.
* TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 9.08283904e+08

* HELP process_resident_memory_bytes Resident memory size in bytes.
* TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 4.3380736e+07

* HELP go_memstats_sys_bytes Number of bytes obtained from system.
* TYPE go_memstats_sys_bytes gauge
go_memstats_sys_bytes 7.1762168e+07

#### CPU

* HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
* TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 57.65

* HELP go_threads Number of OS threads created.
* TYPE go_threads gauge
go_threads 12

#### Other


* HELP promhttp_metric_handler_requests_in_flight Current number of scrapes being served.
* TYPE promhttp_metric_handler_requests_in_flight gauge
promhttp_metric_handler_requests_in_flight 1

* HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
* TYPE process_start_time_seconds gauge
process_start_time_seconds 1.63052279399e+09

* HELP process_open_fds Number of open file descriptors.
* TYPE process_open_fds gauge
process_open_fds 1

* HELP process_max_fds Maximum number of open file descriptors.
* TYPE process_max_fds gauge
process_max_fds 1.048576e+06


#### Less Relevant metrics


* HELP go_memstats_stack_sys_bytes Number of bytes obtained from system for stack allocator.
* TYPE go_memstats_stack_sys_bytes gauge
go_memstats_stack_sys_bytes 786432

* HELP go_memstats_stack_inuse_bytes Number of bytes in use by the stack allocator.
* TYPE go_memstats_stack_inuse_bytes gauge
go_memstats_stack_inuse_bytes 786432

Further metrics bout go such as memstats information