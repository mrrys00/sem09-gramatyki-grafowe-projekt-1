prepare_venv:
	python3 -m venv venv

install_requirements:
	pip3 install -r requirements.cfg

run_main:
	python3 main.py

test_production_01:
	pytest -vrPs productions/p01/test_01.py

test_production_02:
	pytest -vrPs productions/p02/test_02.py

test_production_03:
	pytest -vrPs productions/p03/tests03.py

test_production_04:
	pytest -vrPs productions/p04/tests04.py

test_production_07:
	pytest -vrPs productions/p07/tests07.py

test_production_08:
	pytest -vrPs productions/p08/tests08.py

test_production_09:
	pytest -vrPs productions/p09/tests09.py

test_production_10:
	pytest -vrPs productions/p10/tests10.py

test_production_11:
	pytest -vrPs productions/p11/tests11.py

test_production_16:
	pytest -vrPs productions/p16/tests16.py

test_production_17:
	pytest -vrPs productions/p17/tests17.py
