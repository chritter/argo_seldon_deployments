# sends requests for 10minutes
for i in `seq 1 6000`; do \
   echo next request
   sleep 1 && curl -s -X POST http:///localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{ "data": { "ndarray": ["Aujourd hui est un bon jour"] } }'
done
