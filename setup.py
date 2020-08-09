import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sosi_crawler_object_factory',
<<<<<<< HEAD
    version='__version__',
=======
    version='#{package.version}#',
>>>>>>> e3dd2c406d0b8b1932cc0e2e5bb725cb24fb99ad
    author='SoSI',
    author_email='contato@sosi.com.br',
    description="Object facotry responsible to create SoSI's components objects (DIP)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/leonidasnascimento/sosi_crawler_object_factory',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
