test:
	docker build  -f Dockerfile . --rm  -t app-flask-test-coverage
	docker run --rm -it app-flask-test-coverage