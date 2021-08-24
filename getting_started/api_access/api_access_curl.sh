# port 9000 exposed through the sklearn container
curl -s -X POST http://localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{ "data": { "ndarray": [[1,2,3,4]] } }'

# port 8000 exposed through seldon-container-engine container
# Swagger API doc at http://localhost:8000/api/v1.0/doc/

