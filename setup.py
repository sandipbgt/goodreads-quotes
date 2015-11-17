from setuptools import setup

setup(
  name = 'goodreads_quotes',
  description = 'Fetches popular quotes and quote of the day from goodreads.com website',
  long_description = open('README.rst').read(),
  author = 'Sandip Bhagat',
  author_email = 'sandipbgt@gmail.com',
  url = 'https://github.com/sandipbgt/goodreads-quotes',
  version = '0.1.0',
  install_requires = ['requests', 'lxml', 'six'],
  packages = ['goodreads_quotes'],
  license = 'MIT',
  keywords = ['goodreads', 'quotes', 'motivation', 'daily-quotes', 'popular-quotes'],
)