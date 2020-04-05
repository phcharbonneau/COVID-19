from setuptools import setup

setup(
   name='server',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='phcharbonneau@hotmail.com',
   packages=['server'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
)