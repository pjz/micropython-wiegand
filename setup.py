
from setuptools import setup

setup(
    name='micropython-wiegand',

    description='MicroPython class to read from a Wiegand card reader',
    long_description='MicroPython class to read from a Wiegand card reader',

    # The project's main homepage.
    url='https://github.com/pjz/micropython-wiegand',

    # Author details
    author='Paul Jimenez',
    author_email='pj@place.org',

    # Choose your license
    license='LGPLv3+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='micropython wiegand keycard',

    # SemVer
    version='1.0.0',

    # a single-file module
    py_modules=['wiegand'],
)
