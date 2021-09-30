TEST_PATH=./

help:
	@echo "make init"
	@echo "		initialize the project"
	@echo "make init-dev"
	@echo "		intialize the project for development"
	@echo "make clean"
	@echo "		remove python artifacts"

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

test: clean
	py.test --verbose --color=yes $(TEST_PATH)

init:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

init-dev:
	make init
	python -m pip install -r dev-requirements.txt
