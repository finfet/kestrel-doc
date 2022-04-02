all: build

build:
	rsync -a --delete ../releases static/
	zola build
	mdbook build

deploy: build
	rsync -avz --delete public/ ${KESTREL_DOC_LOCATION}

.PHONY: all build deploy
