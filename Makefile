VENV= $(. ../venv/bin/activate)
JB=$(VENV) jb
PYTHON=$(VENV) python3

clean:
	rm -rf _build
	jb clean .

build:
	$(JB) build --all .

url:
	$(PYTHON) jupyterhub.py
