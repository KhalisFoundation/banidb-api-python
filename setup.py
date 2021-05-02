from setuptools import find_packages, setup
setup(
    name='banidb',
    packages=['banidb'],
    version='0.1',
    license='MIT',
    description='BaniDB API for Python',
    author='Khalis Foundation',
    url='https://github.com/KhalisFoundation/banidb-api-python',
    keywords=['BaniDB','API','Amrit Keertan','Sundar Gutka','SikhiToTheMax','Gurbani','KhalisFoundation'],
    install_requires=[
        'requests',
        'time',
        'pickle'
        ]
)