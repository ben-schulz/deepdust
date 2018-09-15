import setuptools

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

    include_package_data=True,
    zip_safe=False
)
