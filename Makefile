VENV= $(. ../venv/bin/activate)
JB=$(VENV) jb
PYTHON=$(VENV) python3

clean:
	rm -rf _build
	jb clean .

build:
	$(JB) build --all .;


url:
	$(PYTHON) jupyterhub.py

server:
	python3 -m http.server 8000 --directory _build/html

pid: 
	sudo lsof -i :8000

