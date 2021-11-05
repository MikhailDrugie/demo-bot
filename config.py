import os

# for uploading new files from PC
# MY_ID = int('my_id')
# DB_FILENAME = 'botuploads.db'
# TOKEN = 'token'

# for launching bot itself
TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    print('You have forgotten to set BOT_TOKEN')
    quit()

'''
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
'''
