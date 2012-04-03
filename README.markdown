# CMSss...

Amazon Web Services S3 Content Management System.

# Install

Have an S3 bucket ready. And, make it web-site-able.

    . env/bin/activate
    pip install Jinja2
    pip install boto
    vim local_settings.py #and write your access key and stuff
    python build.py

Now html, js, css files are generated and uploaded to your bucket.
Visit your bucket and CMS!

# Benefits

## Twitter URL

Urls look like web scale twitter: yoursite.com/#!some-page.html

## Web Scale 3.0+ Compliant

All static means it's web traffic rush proven to handle even.



