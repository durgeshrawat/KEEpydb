from distutils.core import setup
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
  name = 'KEEpydb',         # How you named your package folder (MyLib)
  packages = ['KEEpydb'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Database for Python',   # Give a short description about your library
  long_description=long_description
  author = 'Durgesh Rawat',                   # Type in your name
  author_email = 'durgeshrawat.info@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/durgeshrawat/KEEpydb',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/durgeshrawat/KEEpydb/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['KEEpydb', 'database', 'db'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'openpyxl',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.8',
  ],
)
