all: build

build:
	rsync -a site/ static/
	rsync -a ../releases static/
	mdbook build

deploy: build
	rsync -a static/ ${KESTREL_DOC_LOCATION}

.PHONY: all build publish
