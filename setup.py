from setuptools  import setup

setup(
    name='gql-guard',
    version='0.9',
    packages=['gql_guard'],
    license='Apache 2.0',
    author='Samuel Ostholm',
    description="Provides a JWT token based access restrictions to graphql queries and mutations",
    install_requires=['graphene', 'starlette', 'starlette-jwt']
)