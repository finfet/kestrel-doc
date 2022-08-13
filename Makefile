all: download build

build:
	zola build
	mdbook build
	tar -czvf public.tar.gz public

download:
	wget -i releases.txt -x -nH -P static/releases

clean:
	rm -rf public public.tar.gz static/releases

.PHONY: all build download clean
