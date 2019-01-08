
PACKAGE = strudel.ghutils

.PHONY: test
test:
	python -m unittest test

.PHONY: build
build:
	$(MAKE) clean
	$(MAKE) test
	python setup.py sdist bdist_wheel
	# twine upload dist/*  # handled by semantic-release in this package

.PHONY: clean
clean:
	rm -rf $(PACKAGE).egg-info dist build docs/build
	find -name "*.pyo" -delete
	find -name "*.pyc" -delete
	find -name __pycache__ -delete

.PHONY: html
html:
	sphinx-build -M html "docs" "docs/build"

.PHONY: install_dev
install_dev:
	pip install -r requirements.txt
	pip install sphinx sphinx-autobuild
