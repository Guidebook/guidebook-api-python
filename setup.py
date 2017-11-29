from setuptools import setup

github_repo_url = 'https://github.com/Guidebook/guidebook-api-python'

setup(
    name='guidebook-api-python',
    version='0.0.2',
    author='Guidebook',
    author_email='web-team@guidebook.com',
    description='Python client for the Guidebook Open API.',
    long_description='See {} for installation and usage instructions.'.format(github_repo_url),
    url=github_repo_url,
    license='MIT',
    packages=['guidebook'],
    install_requires=['requests>=2.0.0'],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
)
