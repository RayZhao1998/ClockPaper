from setuptools import setup, find_packages

setup(
	name = 'ClockPaper',
	version = '1.0',
	packages = find_packages(),
	license = 'MIT',
	author = 'Ray Zhao',
	author_email = 'rayzhao98@163.com',
	url = 'https://github.com/RayZhao1998/clockPy',
	description = 'A python application in shell to show current time and date',
	
	install_requires = [
		'AlphabetPy>=1.0.1',
	],
	
	entry_points = {
		'console_scripts': [
		    'ClockPaper = ClockPaper:start'
		],
	},
	
)