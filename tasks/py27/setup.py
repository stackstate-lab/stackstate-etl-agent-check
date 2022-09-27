# -*- coding: utf-8 -*-
from setuptools import setup
packages = [
    'stackstate_etl_check_processor',
]
package_data = {'': ['*']}
install_requires = []
setup_kwargs = {
   'name': 'stackstate-etl-agent-check',
   'version': '__version__',
   'description': 'StackState Extract-Transform-Load Agent Check for 4T data ingestion',
   'long_description': 'None',
   'author': 'Ravan Naidoo',
   'author_email': 'rnaidoo@stackstate.com',
   'maintainer': 'None',
   'maintainer_email': 'None',
   'url': 'None',
   'packages': packages,
   'package_data': package_data,
   'install_requires': install_requires,
   'python_requires': '>=2.7, <=2.8',
}

setup(**setup_kwargs)
