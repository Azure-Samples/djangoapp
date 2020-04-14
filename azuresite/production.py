from .settings import *

# Configure default domain name
ALLOWED_HOSTS = [os.environ['WEBSITE_SITE_NAME'] + '.azurewebsites.net', '127.0.0.1'] if 'WEBSITE_SITE_NAME' in os.environ else []

# WhiteNoise configuration
MIDDLEWARE = [                                                                   
    'django.middleware.security.SecurityMiddleware',
# Add whitenoise middleware after the security middleware                             
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',                      
    'django.middleware.common.CommonMiddleware',                                 
    'django.middleware.csrf.CsrfViewMiddleware',                                 
    'django.contrib.auth.middleware.AuthenticationMiddleware',                   
    'django.contrib.messages.middleware.MessageMiddleware',                      
    'django.middleware.clickjacking.XFrameOptionsMiddleware',                    
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configure Postgres database
DATABASES = {                                                                    
    'default': {                                                                 
        'ENGINE': 'django.db.backends.postgresql',                               
        'NAME': os.environ['DBNAME'],                                            
        'HOST': os.environ['DBHOST'],                                            
        'USER': os.environ['DBUSER'],                                            
        'PASSWORD': os.environ['DBPASS']                                         
    }                                                                            
}
