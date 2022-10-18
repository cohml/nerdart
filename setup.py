from setuptools import find_packages, setup

setup(
    name='nerdart',
    version='1.0.0',
    description='Nerdy art made with math and code.',
    url='https://github.com/cohml/nerdart',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts' : [
            'nerdart = nerdart.src.util.nerdart:main'
        ]
    }
)
