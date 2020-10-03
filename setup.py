import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyPasswordGenerator",
    version="1.0.2",
    description="create random password with varies passcode set",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cove9988/PasswordGenerator",
    author="Paulguo",
    author_email="cove9988@gmail.com",
    license="MIT",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable

        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
        'Operating System :: POSIX'
    ],
    keywords='random password generator different lengths with customized character set',
    packages=["pyPasswordGenerator"],
    include_package_data=False,
    py_modules=['pyPasswordGenerator'],
    entry_points={
        "console_scripts": [
            "passgen=pyPasswordGenerator.password:generator",
        ]
    },
)