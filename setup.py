from setuptools import setup

with open('README.md', 'r') as f:
    README = f

setup(
    name='banidb',
    version='0.1',
    license='MIT',
    description='BaniDB API for Python',
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
    install_requires=['requests'],
    author_email='',
    download_url='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Punjabi',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=['banidb'],
    include_package_data=True,
    project_urls={
        'Documentation': '',
        'Source': 'https://github.com/KhalisFoundation/banidb-api-python',
    },
)
