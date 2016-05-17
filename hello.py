# view.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")


#urls.py
from django.conf.urls import url

urlpatterns = (
    url(r'^$', index),
)


# settings.py
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='somesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


# wsgi.py
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


# manage.py
import sys

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
