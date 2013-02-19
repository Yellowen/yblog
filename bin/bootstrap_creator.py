import virtualenv
import textwrap


output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess
def after_install(options, home_dir):
    subprocess.call([join(home_dir, 'bin', 'pip'),
                     'install', 'ipython', 'vanda', 'vakhshour', 'daarmaan', 'mimeparse', 'python-dateutil', 'lxml', 'pyyaml', 'uuid', 'django-tastypie', 'markdown', 'pygment', 'django-haystack', 'whoosh', 'django-tagging', 'django-robots', 'feedparser', 'django-recaptcha' ])
"""))
f = open('bootstrap.py', 'w').write(output)
