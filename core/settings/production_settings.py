from .base_settings import *


logging.info("In production 🏭")

SECRET_KEY = os.environ.get("SECRET_KEY")  # We'll get this from the environment variable on the server.

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600
    )
}


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Setup static file collection for Render.
if not DEBUG:
    STATIC_URL = 'static/'
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(REPO_DIR, 'staticfiles')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

