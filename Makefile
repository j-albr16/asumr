JB = jb

clean:
	rm -rf _build
	jb clean .

build: 
	$(JB) build --all .;
	make include


url:
	python3 jupyterhub.py

server:
	python3 api/main.py

pid: 
	sudo lsof -i :8000

include: _build/html/intro.html chat/chat_button.html
	python3 chat/insert-html.py

