from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY'] = '89d2be80b2a972451fda9bf50e85c94cc374fc79239b966d'

from app import routes
