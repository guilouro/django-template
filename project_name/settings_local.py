DEBUG = True

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': parse('sqlite:///' + BASE_DIR.child('db.sqlite3'))
}

HTML_MINIFY = True

THUMBNAIL_DEBUG = True