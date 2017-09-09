from flask import Flask
import os

template_dir = os.path.abspath('../../frontend')
app = Flask(__name__, template_folder=template_dir)

from .server import *
