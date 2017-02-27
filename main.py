import os
import htmlPy

from api_1_0 import API

# Mode
RUN_MODE = 'development'

# Initial configurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# GUI initializations
app = htmlPy.AppGUI(title=u"Sample application", maximized=True, plugins=True, developer_mode=True)

# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")
app.bind(API(app, mode=RUN_MODE))

app.template = (u"index.html", {RUN_MODE: True})

if __name__ == "__main__":
    app.start()
