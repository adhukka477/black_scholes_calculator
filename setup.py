import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='options_calculator',
    version='0.0.2',
    author='Alishan Dhukka',
    author_email='alishandhukka@gmail.com',
    description='Tool for calculating the premiums for put and call options',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/adhukka477/black_scholes_calculator',
    project_urls = {
        "Bug Tracker": "https://github.com/adhukka477/black_scholes_calculator"
    },
    license='MIT',
    packages=['options_calculator'],
    install_requires=['numpy', 'pandas', 'datetime', 'bs4', 'scipy', 'ta', 'yahoo-finance @ git+https://github.com/adhukka477/yahoo_finance.git'],
)
