from distutils.core import setup
setup(
    name='boundary',
    version='0.0.2',
    url="https://github.com/boundary/boundary-api-cli",
    author='David Gwartney',
    author_email='davidg@boundary.com',
    packages=['boundary',],
    scripts=[
      'bin/action-list',
      'bin/metric-create',
      'bin/metric-export',
      'bin/metric-get',
      'bin/metric-import',
      'bin/metric-list',
      'bin/metric-markdown',
      'bin/relay-list',
      'bin/user-get',
    ],
    license='LICENSE.txt',
    description='Command line interface to Boundary REST APIs',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.3.0",
    ],
)

