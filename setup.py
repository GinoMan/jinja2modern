import os
from setuptools import setup, find_packages


def read(fname):
	with open(os.path.join(os.path.dirname(__file__), fname)) as f:
		return f.read()


setup(
	name='jinja2modern',
	version='0.4.0',
	author='Gino Vincenzini',
	author_email='gino@ginovincenzini.com',
	include_package_data=True,
	packages=find_packages(),
	install_requires=["jinja2"],
	url='https://github.com/GinoMan/jinja2modern',
	license='BSD',
	description='Jinja2 tags for modern web. Includes sass, scss, less, coffee, uglify. Can be easily extended for any command line tools.',
	long_description=read('README.md'),
	zip_safe=False,
)
