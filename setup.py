import setuptools
import subprocess

import distutils.cmd

class BuildSpecTestCommand(distutils.cmd.Command):

    description = 're-generate spec tests from remote manifest.'

    user_options = [
        #format: (longarg, shortarg, description)
        ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        cmd = ['python3', 'deepdust/test/spec/get_latest.py']
        subprocess.check_call(cmd)


def readme():
    return ''


setuptools.setup(
    name='deepdust',
    version='0.0',
    description='JSON-LD utilities',
    long_description=readme(),
    
    url='https://github.com/ben-schulz/deepdust',
    author='Benjamin Schulz',
    author_email='benjamin.john.schulz@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        ],

    packages=[
    ],

    install_requires=[
    ],

    entry_points={
    },

    test_suite='deepdust.test.test_all',

    cmdclass={
        'jsonld_spec': BuildSpecTestCommand
        },
    
    include_package_data=True,
    zip_safe=False
)


