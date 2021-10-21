IMAGE_VERSION=0.4
build:
	# see language wrapper images at https://docs.seldon.io/projects/seldon-core/en/latest/reference/images.html
	s2i build . -E environment seldonio/seldon-core-s2i-python3:1.7.0 sklearn_iris:$(IMAGE_VERSION)
push:
	docker tag sklearn_iris:$(IMAGE_VERSION) chritter/sklearn_iris:$(IMAGE_VERSION)
	docker push chritter/sklearn_iris:$(IMAGE_VERSION)
