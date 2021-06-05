from setuptools  import setup, find_packages

setup(
    name='gql-guard',
    version='0.9',
    packages=find_packages(),
    license='Apache 2.0',
    author='Samuel Ostholm',
    description="Provides a JWT token based access restrictions to graphql queries and mutations",
    install_requires=['graphene', 'starlette', 'starlette-jwt']
)