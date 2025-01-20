from config.env import env

APPS = [
    "channels",
    "cacheops",
    "rosetta",
    "django_ckeditor_5",
    "drf_spectacular",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_redis",
    "rest_framework_simplejwt",
    "django_core",
    "core.apps.accounts.apps.AccountsConfig",
    'core.apps.api',
    'core.apps.students',
    'core.apps.educenter',
    'core.apps.teachers',
    'core.apps.users',
]

if env.str("PROJECT_ENV") == "debug":
    APPS += [
        "silk",
    ]