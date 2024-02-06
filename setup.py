#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['wheel', 'wheel.cli', 'wheel.vendored', 'wheel.vendored.packaging']

package_data = \
{'': ['*']}

package_dir = \
{'': 'src'}

extras_require = \
{'test': ['pytest >= 6.0.0', 'setuptools >= 65']}

entry_points = \
{'console_scripts': ['wheel = wheel.cli:main'],
 'distutils.commands': ['bdist_wheel = wheel.bdist_wheel:bdist_wheel']}

setup(name='wheel',
      version='0.41.2',
      description='A built-package format for Python',
      author=None,
      author_email='Daniel Holth <dholth@fastmail.fm>',
      url=None,
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.7',
     )
