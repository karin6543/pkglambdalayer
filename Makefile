PYTHON_VERSION := 3.9
TAG := dev

build:
	docker build --build-arg PYTHON_VERSION=${PYTHON_VERSION} -t pkglambdalayer:${TAG} .

build-dev:
	docker build \
		--build-arg PYTHON_VERSION=${PYTHON_VERSION} \
		-t pkglambdalayer_dev:${TAG} dev

lint: build-dev ## Run linting
	docker run \
		-v ${PWD}:/app \
		pkglambdalayer_dev:${TAG} autopep8 --in-place --recursive --global-config=/app/dev/setup.cfg .