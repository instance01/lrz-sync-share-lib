from setuptools import setup


setup(name='lrz-sync-share',
    version='0.1',
    description='LRZ Sync+Share library for uploads and other file management',
    url='https://github.com/instance01/lrz-sync-share-lib',
    author='Instance01',
    author_email='Use the github issues',
    license='MIT',
    packages=['lrz_sync_share'],
    install_requires=["requests"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    long_description=open('README.rst').read(),
    zip_safe=False)
