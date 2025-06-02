from setuptools import setup, find_packages


scripts = ['./src/super_resolution.py']


setup(
    name='super_resolution',
    version='0.1.0',
    python_requires='>=3.10',
    packages=find_packages(),
    install_requires=open('requirements.txt').read(),
    entry_points='''
        [console_scripts]
        super_resolution=src.super_resolution:super_resolution_cli

    ''',
    scripts=scripts,
    test_suite='tests'
)
