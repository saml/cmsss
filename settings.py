title = 'your website title'
aws_access_key = 'your access key'
aws_secret_key = 'your secret key'

try:
    from local_settings import *
except ImportError:
    pass

css_url = 'assets/css'
js_url = 'assets/js'

import os

output_dir = os.path.abspath('./build')
template_dir = os.path.abspath('./src')
templates = ['index.html', 'admin.html']
javascripts_admin = ['src/sha1.js',
        'src/S3Ajax.js']
javascripts = ['src/utility.js']
