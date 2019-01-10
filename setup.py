from distutils.core import setup

setup(
    name='libkloudtrader',
    version='0.1',
    author='KloudTrader',
    author_email='support@kloudtrader.com',
    packages=['libkloudtrader'],
    url='https://github.com/KloudTrader/kloudtrader',
    license='LICENSE',
    description="kloudTrader's in-house library that makes it much easier for you to code algorithms that can trade for you.",
    long_description=open('README.md').read(),
    install_requires=[
        "requests",
        "boto3",
        "pandas",
        "numpy",
        "sklearn",
        "pyti",
        "scipy",
        "empyrical",
        "tabulate",
        "ta",
        "TA-Lib",
    ],
)
