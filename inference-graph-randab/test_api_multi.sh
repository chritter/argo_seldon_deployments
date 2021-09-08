# sends requests for 10minutes
for i in `seq 1 6000`; do \
   sleep 1 && curl -d '{"data": {"ndarray":[[1, 2, 3, 4]]}}' \
   -X POST http://localhost:9000/api/v1.0/predictions \
   -H "Content-Type: application/json";
done
