all: build

build:
	rsync -a --delete ../releases static/
	zola build
	mdbook build
	tar -czvf public.tar.gz public

clean:
	rm -rf public public.tar.gz

.PHONY: all build clean
