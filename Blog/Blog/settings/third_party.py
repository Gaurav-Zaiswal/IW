# this file contains only third party apps settings
# and this file is inherited by ./prod.py and ./base.py

from Blog.settings.base import *


INSTALLED_APPS += [
    'ckeditor',
]