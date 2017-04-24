class DevelopmentConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    STRIPE_SECRET_KEY = ''
    STRIPE_PUBLIC_KEY = ''
    SEGMENT_WRITE_KEY = ''

    STRIPE_SECRET_KEY = 'sk_test_c6CmSmOKbChoRqShPiKTV9yi'


class ProductionConfig(DevelopmentConfig):
    DEBUG = False
    SECRET_KEY = '\xc4\x1cax\x84\xa6$\xb6Is\xcbuO\x8b@\xa8/~\xda\xd8-1\x0c\xc2Y\x8a'
    STRIPE_SECRET_KEY = 'sk_live_vKTfuiydeDwca2xmYM7sU9KF'

