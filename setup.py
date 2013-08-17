import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'pyramid==1.4',
    'pyramid_debugtoolbar',
    'pyramid_exclog',
    'waitress',
    'nose',
    'coverage',
    'SQLAlchemy',
    'zope.sqlalchemy',
    'transaction',
    'pyramid_tm',
    #'mysql-python',
    'pyramid_jinja2'
    ]

setup(name='hellopyramid',
      version='0.1',
      description='hellopyramid',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='hellopyramid',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = hellopyramid:main
      [console_scripts]
      initialize_hellopyramid_db = hellopyramid.scripts.initializedb:main
      """,
      )
