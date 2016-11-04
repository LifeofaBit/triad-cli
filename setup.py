'''Package settings.'''

from setuptools import Command, find_packages, setup

from os.path import abspath, dirname, join
from codecs import open
from subprocess import call

from triad import __version__



curr_dir = abspath(dirname(__file__))
with open(join(curr_dir, 'README.md'), encoding='utf-8') as readme:
	long_description = readme.read()

class RunTests(Command):
	'''Run all tests.'''
	description = 'run tests'
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		'''Run all tests!'''
		errno = call(['py.test', '--cov=triad', '--cov-report=term-missing'])
		raise SystemExit(errno)

setup(
	name = 'triad',
	version = __version__,
	description = 'An experimental command line program',
	long_description = long_description,
	url = 'https://github.com/LifeofaBit/triad-cli',
	author = 'Matt Downs',
	author_email = 'm@downs.com',
	license = 'UNLICENSE',
	classifiers = [
		'Intended Audience :: Developers',
		'Topic :: Utilities',
		'License :: Public Domain',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
	],
	keywords = 'cli',
	packages = find_packages(exclude=['docs', 'tests*']),
	install_requires = ['docopt'],
	extras_require = {
		'test': ['coverage', 'pytest', 'pytest-cov'],
	},
	entry_points = {
		'console_scripts': [
			'triad=triad.cli:main',
		],
	},
	cmdclass = {'test': RunTests},
)
