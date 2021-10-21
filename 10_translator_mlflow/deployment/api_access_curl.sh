
curl -s -X POST http:///localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{ "data": { "ndarray": ["Aujourd hui est un bon jour"] } }'
