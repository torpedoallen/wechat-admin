clean_pyc:
	find `pwd` -name '*.pyc' -type f -delete

initdb:
	python initdb.py
