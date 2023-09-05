from setuptools import setup, find_packages

setup(
    name='streetview-downloader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'PIL',
        'csv',
        'os',
        'io'
    ],
    author='Sijie Yang',
    author_email='sijiey@u.nus.edu',
    description='A module to download images from Google Street View.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/sijie-yang/streetview-downloader',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
