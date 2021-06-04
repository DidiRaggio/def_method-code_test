from setuptools import setup
from setuptools import find_packages

setup(
    name="def_method",
    version="1.0.0",
    description="Diego Raggio's Def Method code test.",
    author="Diego Raggio",
    author_email="didiraggio@gmail.com",
    url="https://github.com/DidiRaggio/def_method-code_test",
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'text_processor = text_processor.main:main',
        ],
    },
    install_requires=[
        "pytest",
        "pytest-mock"
    ],
    python_requires='>=3.7',
)
