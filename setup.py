from setuptools import setup, find_packages

setup(
    name='rolling-upgrades-during-test',
    version='0.0.1',
    description='Parses a given input and inserts into ElasticSearch.',
    author='Joshua White',
    author_email='joshua.l.white@intel.com',
    url='https://github.com/osic/rolling-upgrades-during-test',
    packages=['rolling-upgrades-during-test'],
    install_requires=open('requirements.txt').read(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'rolling-upgrades-during-test = rolling-upgrades-during-test.test:lcm']})
