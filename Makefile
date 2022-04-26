build:
	docker build --tag=jdvelasq/iris_app  app/


train:
	python3 train/train.py 