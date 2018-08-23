import os
import errno
from settings.settings import BASE_DIR
from .exceptions import CommandError


def create_app(app_name):
    try:
        os.makedirs(BASE_DIR + '/{}'.format(app_name))
    except OSError as e:
        if e.errno == errno.EEXIST:
            raise CommandError('Already has {} app'.format(app_name))

    app_dir = BASE_DIR + "/{}".format(app_name)

    models = open(os.path.join(app_dir, 'models.py'), 'w')
    views = open(os.path.join(app_dir, 'views.py'), 'w')
    urls = open(os.path.join(app_dir, 'urls.py'), 'w')

    models.write('from py_rest.db import models \n\n\n')
    models.write('# Write here your models \n')
    models.close()
    views.write('# write here your views \n')
    views.close()
    urls.write('# Your URL patten \n')
    urls.close()
