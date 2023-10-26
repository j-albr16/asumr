VENV= $(. ../venv/bin/activate)
JB=$(VENV) jb
PYTHON=$(VENV) python3


build:
	rm -rf _build;
	sleep 1;
	$(JB) build --all .

url:
	$(PYTHON) jupyterhub.py
