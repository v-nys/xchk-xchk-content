# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xchk_xchk_content']

package_data = \
{'': ['*'],
 'xchk_xchk_content': ['static/xchk_xchk_content/images/*', 'templates/xchk_xchk_content/*']}

install_requires = \
[]

setup_kwargs = {
    'name': 'xchk_xchk_content',
    'version': '0.0.1',
    'description': 'Course material related to Xchk for the xchk teaching framework',
    'long_description': None,
    'author': 'Vincent Nys',
    'author_email': 'vincentnys@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
