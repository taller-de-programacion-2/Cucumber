
test:
	docker build  -f Dockerfile . --rm  -t app-node-test
	docker run --rm -it app-node-test
