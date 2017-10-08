try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    	'description': 'This is a test project, I want this module to add a varying amount of numbers',
	'author': 'Vivek Shah',
	'url': 'n/a',
	'download_url': 'n/a',
	'author_email': 'vivekagal1998@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['sum_stuff'],
	'scripts': [],
	'name': 'sum_stuff'
	}

setup(**config)
