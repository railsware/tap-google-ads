#!/usr/bin/env python

from setuptools import setup

setup(name='tap-google-ads',
      version='1.6.0',
      description='Singer.io tap for extracting data from the Google Ads API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_google_ads'],
      install_requires=[
          'singer-python@git+https://github.com/railsware/singer-python/@565fcb685e6a636c3ad21e421a0662da47757573',
          'requests>=2.26.0',
          'backoff~=2.2.1',
          'google-ads==25.1.0',
          'protobuf==4.25.3',
          # Necessary to handle gRPC exceptions properly, documented
          # in an issue here: https://github.com/googleapis/python-api-core/issues/301
          'grpcio-status>=1.59.0,<1.64.0',  # 1.64 depends on protobuf 5.x
      ],
      extras_require= {
          'dev': [
              'pylint',
              'nose',
              'ipdb',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-google-ads=tap_google_ads:main
      ''',
      packages=['tap_google_ads'],
      package_data = {
      },
      include_package_data=True,
)
