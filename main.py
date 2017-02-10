import os
import htmlPy
from backend import BackEnd

# Initial configurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# GUI initializations
app = htmlPy.AppGUI(title=u"Sample application", maximized=True, plugins=True)

# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")
app.bind(BackEnd(app))

app.template = (u"index.html", {})

if __name__ == "__main__":
    app.start()