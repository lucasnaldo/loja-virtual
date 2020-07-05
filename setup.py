import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='loja',
    version='0.0.1',
    license='Proprietary',
    maintainer='Lucas Naldo Falotico',
    maintainer_email='',
    description='Loja Virtual',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'marshmallow',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
