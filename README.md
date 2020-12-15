# SecureHeaders

OWASP SecureHeaders Project  

SecureHeaders project consist in two main modules:

1. an engine to scan a list of sites fastly and with minimal resources;
2. a web interface with a dashboard to view, search and customize besides
provide insight and feedback about the use of HTTP secure headers.

HTTP secure headers are resources known to some and despised by others.
However it's a fact that the versatility and security provided by feature can
help make web applications more secure.

## Dependencies  

- Redis
- Python 3.6

## Configuration (Dashboard | Scanner)

Edit `.env` file or set environment variable:

````txt
# general settings
## scanner
THREAD_NUMBER=1000
TOPSTIES_FILENAME=conf/topsites_global.csv
SENTRY_ENABLED=False
SENTRY_DSN=''

# http settings
ORIGIN=http://a.com
TIMEOUT=3

# mysql settings
MYSQL_USERNAME=root
MYSQL_PASSWORD=password
MYSQL_HOST=localhost
MYSQL_DATABASE=headers

# redis settings
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_TTL=60

# http header filters
HEADERS=strict-transport-security,public-key-pins,x-xss-protection,x-frame-options,x-content-type-options,content-security-policy,x-permitted-cross-domain-policies,referrer-policy

# plugins settings
MIME_TYPES=text/html,text/html; charset=utf-8,text/css,text/xml,application/json,image/png,application/javascript,image/jpeg
````




#### setup, install and run scanner:

````bash
# install virtualevn
#
pip install virtualenv
# create virtualenv locally
#
virtualenv venv
# active virtualenv
#
source venv/bin/activate
# install application dependencies
#
pip install -r requirements.txt
# start application (web interface)
#
python cli.py scanner -f conf/develop.csv
Thread pool 1 (0 - 1000)
[*] connection error for <pclady.com.cn>
[!] site <pclady.com.cn> will be excluded from the analysis

Connections summary
https: 3
http: 2
error: 2


