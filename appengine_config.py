from google.appengine.ext import vendor

import os
import sys

rootdir = os.path.dirname(os.path.abspath(__file__))
lib = os.path.join(rootdir, 'venv/Lib/site-packages/')
print(lib)


vendor.add('lib')