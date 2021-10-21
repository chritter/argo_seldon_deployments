
recreate:
	conda create -n seldon_getting_started_custom_mlflow python=3.8
install:
	conda env create -f environment.yml

env:
	conda activate seldon_getting_started_custom_mlflow
export:
	conda activate seldon_getting_started_custom_mlflow
	conda env export | grep -v "^prefix: " > environment.yml
