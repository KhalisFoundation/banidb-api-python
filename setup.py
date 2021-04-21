from setuptools import find_packages, setup
setup(
    name='bani_db',
    packages=find_packages(include=['bani_db']),
    version='0.1.0',
    description='BaniDB API for Python',
    author='Khalis Foundation',
    license='MIT',
    install_requires=['requests','time']
)