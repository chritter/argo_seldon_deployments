build:
	s2i build . -E environment seldonio/seldon-core-s2i-python3:0.18 sklearn_iris:0.1
	# s2i build . -E environment docker pull seldonio/seldon-core-s2i-python38:1.10.0 sklearn_iris:0.1 #  error: des not contain io.openshift.s2i.scripts-url label
	# s2i build . -E environment docker pull  seldonio/seldon-core-s2i-python3:1.1.1-rc sklearn_iris:0.1
push:
	docker tag sklearn_iris:0.1 chritter/sklearn_iris:0.1
	docker push chritter/sklearn_iris:0.1