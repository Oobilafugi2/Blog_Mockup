from flask import Flask

# creates app objuect using the imported Flask class, and passing the name of the module to reference
app = Flask(__name__)

# this is the app directory, which is a package because of the __init__.py file inside
from app import routes