from app.app import app
import os 
# do some production specific things to the app
if os.environ.get('DEBUG', False):
    app.config['DEBUG'] = True
else:
    app.config['DEBUG'] = False
