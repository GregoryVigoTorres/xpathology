from app import create_app

# this is intended for Heroku
# I don't want to run app with dev config
App = create_app()
