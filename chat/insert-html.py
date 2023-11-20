import os


INDEX_HTML_PATH = "_build/html/intro.html"
INCLUDE_HTML_PATH = "chat/chat_button.html"
MODAL_PATH = "chat/chat_modal.html"


def main():

    with open(INDEX_HTML_PATH, "r") as f:
        index_html = f.read()

    with open(INCLUDE_HTML_PATH, "r") as f:
        include_html = f.read()

    with open(MODAL_PATH, "r") as f:
        modal_html = f.read()

    index_html = index_html.replace(
        '<button onclick="toggleFullScreen()"',
        include_html + '\n<button onclick="toggleFullScreen()"'
    )

    index_html = index_html.replace(
        '</body>',
        modal_html + '\n</body>'
    )

    with open(INDEX_HTML_PATH, "w") as f:
        f.write(index_html)

    # copy folder
    os.system("rm -rf _build/html/chat")
    os.system("cp -r chat _build/html/chat")


if __name__ == '__main__':
    main()
