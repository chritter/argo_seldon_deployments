IMAGE_VERSION=0.1
condacreate:
	conda create -n textclass python=3.7
condafrom:
	conda env create -f environment.yml
condaexport:
	conda activate textclass
	conda env export | grep -v "^prefix: " > environment.yml
condamodelcreate:
	conda create -n textclass_model python=3.7
condamodelfrom:
	conda env create -f environment_model.yml
condamodelexport:
	conda activate textclass_model
	conda env export | grep -v "^prefix: " > environment_model.yml
registerkernel:
	python -m ipykernel install --user --name=textclass
build:
	docker build . -t translator:$(IMAGE_VERSION) --label "run_id=aceec0e241614f0db300ac8ebb8f1901"
push:
	docker tag translator:$(IMAGE_VERSION) chritter/translator:$(IMAGE_VERSION)
	docker push chritter/translator:$(IMAGE_VERSION)
