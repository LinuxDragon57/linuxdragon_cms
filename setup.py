from setuptools import find_packages, setup

setup(
    name='LinuxDragon_CMS',
    version='0.0.1',
    description="A Blog CMS",
    author="E. L. Jackson",
    author_email="linuxdragon57@codedragon.dev",
    url="https://github.com/LinuxDragon57/linuxdragon_cms",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="AGPL",
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'itsdangerous',
        'Jinja2',
        'MarkupSafe',
        'mistune==2.0.2',
        'toml',
        'psycopg2-binary',
        'pycryptodomex',
        'pyotp',
        'python-dotenv',
        'pywarp',
        'segno',
        'sqlalchemy',
        'werkzeug'
    ],
)
