
recreate:
	conda create -n seldexamp python=3.8
install:
	conda env create -f environment.yml

env:
	conda activate seldexamp
export:
	conda activate seldexamp	
	conda env export | grep -v "^prefix: " > environment.yml
