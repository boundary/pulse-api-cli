from distutils.core import setup
setup(
    name='boundary_cli',
    version='0.0.1',
    author='David Gwartney',
    author_email='davidg@boundary.com',
    packages=['boundary_cli',],
    scripts=[
      'bin/metric-export',
      'bin/metric-import',
      'bin/metric-markdown'
    ],
    license='LICENSE.txt',
    description='Command line interface to Boundary REST APIs',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.3.0",
    ],
)

