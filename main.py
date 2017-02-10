import htmlPy
from backend import BackEnd

app = htmlPy.AppGUI(title=u"Sample application")
app.maximized = True
app.template_path = "."
app.bind(BackEnd(app))

app.template = (u"./static/index.html", {})

if __name__ == "__main__":
    app.start()