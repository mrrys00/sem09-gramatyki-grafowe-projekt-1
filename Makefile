prepare_venv:
	python3 -m venv venv

install_requirements:
	pip3 install -r requirements.cfg

run_main:
	python3 main.py

example_test_production_01:
	pytest -vrPs productions/p01/tests01.py

example_test_production_02:
	pytest -vrPs productions/p02/tests02.py
