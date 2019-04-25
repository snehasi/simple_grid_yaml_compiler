init:
	pip install -r requirements.txt
test:
	mkdir .temp
	python -m unittest discover
