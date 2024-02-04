from dotenv import   dotenv_values
config = dotenv_values('.env')

CLIENT_ID =config['GOOGLE_CLIENT_ID']
CLIENT_SECRET = config['GOOGLE_SECRET_KEY']