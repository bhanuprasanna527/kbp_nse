from setuptools import find_packages, setup

setup(
    name='kbp_nse',
    packages=find_packages(include=['kbp_nse']),
    author_email='bhanuprasanna527@gmail.com',
    version='0.1.0',
    description='NSE BHAVCOPY STOCK DATE RETRIEVAL',
    author='kbp',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    test_require=['pytest'],
    test_suite='tests',
)