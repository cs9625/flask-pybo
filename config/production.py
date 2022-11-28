from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = b'V\xfe~\xb9j\x0cz\xc57\xb7\x82X\x08w\xf1\x1f'
