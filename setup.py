from setuptools import setup

with open('README.md', 'r') as f:
    README = f.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='banidb',
    version='0.4.1',
    license='Open Software License 3.0 (OSL-3.0)',
    description='Python Package for Sikh Gurbani - BaniDB API',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Khalis Foundation',
    url='https://github.com/KhalisFoundation/banidb-api-python',
    keywords=[
        'BaniDB',
        'SikhiToTheMax',
        'Gurbani',
        'KhalisFoundation',
        'Sikh',
        'Guru Granth Sahib',
        'API',
        'Amrit Keertan',
        'Sundar Gutka'
    ],
    install_requires=required,
    author_email='python@khalis.info',
    download_url='https://github.com/KhalisFoundation/banidb-api-python/archive/refs/tags/v_0.2.tar.gz',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Religion',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=['banidb'],
    include_package_data=True,
    project_urls={
        'Source': 'https://github.com/KhalisFoundation/banidb-api-python',
        'Issues': 'https://git.io/JG4II'
    },
)
