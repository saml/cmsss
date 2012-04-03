import sys
import re
import os

import jinja2

import settings

class Main(object):
    WHITESPACE = re.compile(r'>\s+<')
    def __init__(self, settings=settings):
        os.makedirs(settings.output_dir)

    def build_html(self):
        loader = jinja2.FileSystemLoader(settings.template_dir)
        env = jinja2.Environment(loader=loader, trim_blocks=True)

        for template_path in settings.templates:
            template = env.get_template(template_path)
            output_path = os.path.join(settings.output_dir, os.path.basename(template_path))
            with open(output_path, 'w') as f:
                print('writing ' + output_path)
                f.write(self.WHITESPACE.sub('><', 
                    template.render(title=settings.title,
                        js_url=settings.js_url,
                        css_url=settings.css_url)))


    def build_js(self):
        pass

    def build_css(self):
        pass

    def upload_to_s3(self):
        pass


def main(argv):
    app = Main()
    app.build_html()
    app.build_js()
    app.build_css()
    app.upload_to_s3()

if __name__ == '__main__':
    main(sys.argv)
