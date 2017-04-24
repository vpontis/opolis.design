class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    STRIPE_SECRET_KEY = ''
    STRIPE_PUBLIC_KEY = ''
    SEGMENT_WRITE_KEY = ''

    # createsend.com is an alias of campaignmonitor.com
    CREATE_SEND_API_KEY = ''

    SENTRY_PRIVATE_DSN = ''
    SENTRY_PUBLIC_DSN = ''


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = '\xc4\x1cax\x84\xa6$\xb6Is\xcbuO\x8b@\xa8/~\xda\xd8-1\x0c\xc2Y\x8a'


class StagingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True

