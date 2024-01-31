from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pylgnetcast',
    version='0.3.9',
    maintainer='Artem Draft',
    maintainer_email='artemon_93@mail.ru',
    description='Client for the LG Smart TV running NetCast 3 or 4.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Drafteed/python-lgnetcast',
    license='MIT',
    packages=['pylgnetcast'],
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False
)
