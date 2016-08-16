TARGET=boundary
VERSION=$(shell grep version setup.py | cut -d "'" -f 2)
TAR_FILE=dist/$(TARGET)-$(VERSION).tar.gz

install: build
	pip install $(TAR_FILE)

build:
	python setup.py sdist

doc:
	pandoc -f markdown -t plain README.md > README.txt

rebuild: clean install

upload:
	python setup.py sdist upload
	
clean:
	/bin/rm -rf build dist site MANIFEST
	pip freeze | grep -v "$(TARGET)==$(VERSION)" && pip uninstall -y $(TARGET)
