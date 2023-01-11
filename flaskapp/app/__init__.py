from flask import Flask,render_template,redirect
from .config import Configuration
# from .models import db, Employee   # New import
# from .routes import simple
# from flask_login import LoginManager,login_required
# from .forms import SimpleForm
# from .models import db, SimplePerson
# from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)

@app.route('/')
def index():
    return render_template('main_page.html', title="Pre-group-project-flaskapp")

@app.route('/test')
def test():
    return {"hello":"welcome testers"}