make_vm:
	python -m venv venv
	
install:
	venv\Scripts\activate \
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python	-m	pytest	-vv	main_test.py

format:
	black *.py

lint:
	pylint --disable=R,C main.py

all: install lint test
