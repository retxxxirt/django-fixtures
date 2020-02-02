SECRET_KEY = 'j1y3vnt1-9qb0(o(s#z*km0owr4^4nm2dfgw$^3*wew&6_w18f'

INSTALLED_APPS = [
    'django_fixtures',
    'tests.project.app_a',
    'tests.project.app_b',
    'tests.project.app_c'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
