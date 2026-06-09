from setuptools import setup, find_packages

setup(
    name="help_cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            # O Windows vai atrelar o comando 'help-cli' ao 'app' dentro do 'main.py'
            "help_cli=help_cli.main:app",
        ],
    },
)