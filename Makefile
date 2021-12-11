test:
	venv/bin/python3 -m pytest

cov-test:
	coverage run -m pytest -v tests && coverage report -m

