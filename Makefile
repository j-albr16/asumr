VENV= $(. ../venv/bin/activate)
JB=$(VENV) jb
PYTHON=$(VENV) python3


build:
	rm -rf _build
	$(JB) clean .
	$(JB) build --all .

url:
	$(PYTHON) jupyterhub.py
