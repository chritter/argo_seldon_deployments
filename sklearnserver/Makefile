SHELL := /bin/bash
VERSION := $(shell cat version.txt)
IMAGE_NAME_BASE=sklearnserver
IMAGE_NAME=chritter/${IMAGE_NAME_BASE}
KIND_NAME ?= kind

build:
	s2i build \
		-E environment \
		./sklearnserver \
		seldonio/seldon-core-s2i-python3:1.7.0 \
		${IMAGE_NAME}:${VERSION}

push:
	docker push ${IMAGE_NAME}:${VERSION}
