from setuptools import setup, find_packages

setup(
    name='streetview-image-downloader',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'Pillow>=8.0.0'
    ],
    author='Sijie Yang',
    author_email='sijiey@u.nus.edu',
    description='A module to download images from Google Street View.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/Sijie-Yang/streetview-downloader',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
