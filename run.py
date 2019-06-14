# coding: utf-8
from create_app import app


@app.template_filter('md')
def markdown_to_html(txt):
    from markdown import markdown
    return markdown(txt)


@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
