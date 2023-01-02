import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='black_scholes_calculator',
    version='0.0.1',
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
    packages=['black_scholes_calculator'],
    install_requires=['numpy', 'pandas', 'datetime', 'bs4', 'scipy', 'ta', 'yahoo-finance @ git+https://github.com/adhukka477/yahoo_finance.git'],
)
