from setuptools import setup, find_packages

setup(
    name="pycoffee-library",
    version='0.3',
    packages = find_packages('src'),
    package_dir = {'' : 'src'},
)
