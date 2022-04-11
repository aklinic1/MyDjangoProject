import os

user = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASSWORD')

print(user + '\n' + password)