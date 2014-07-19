venv:
	virtualenv venv

install: venv
	venv/bin/pip install -r requirements.txt

freeze:
	venv/bin/pip freeze > requirements.txt
