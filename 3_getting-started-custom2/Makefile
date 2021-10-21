IMAGE_VERSION=0.1
build:
	docker build . -t sklearn_iris2:$(IMAGE_VERSION)
push:
	docker tag sklearn_iris2:$(IMAGE_VERSION) chritter/sklearn_iris2:$(IMAGE_VERSION)
	docker push chritter/sklearn_iris2:$(IMAGE_VERSION)
