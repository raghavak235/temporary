import db

def create_app():

  Other initializations 
  with app.app_context():
    db.initialization()
