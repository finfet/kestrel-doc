all: download build

build:
	zola build
	tar -czvf public.tar.gz public

download:
	python3 download.py

clean:
	rm -rf public public.tar.gz static/releases

.PHONY: all build download clean
