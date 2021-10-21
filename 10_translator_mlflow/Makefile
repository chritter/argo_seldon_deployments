IMAGE_VERSION := $(shell cat version.txt)
MODEL_VERSION := $(shell cat model.txt)

build:
	docker build . -t translator:$(IMAGE_VERSION) --label modelversion=$(MODEL_VERSION)
push:
	docker tag translator:$(IMAGE_VERSION) chritter/translator:$(IMAGE_VERSION)
	docker push chritter/translator:$(IMAGE_VERSION)