test:
	venv/bin/python3 -m pytest

cov-test:
	venv/bin/coverage run -m pytest -v tests && venv/bin/coverage report -m

