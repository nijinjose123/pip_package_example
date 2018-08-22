from setuptools import setup


setup(name='piptutorial',
      version='0.1',
      description='The funniest job in the world',
      url= 'https://github.com/nijinjose123/pip_package_example.git',
      author='Nijin Thykkathu',
      author_email='nijin.thykkathu@stfc.ac.uk',
      packages=['piptutorial'],
      install_requires=[
          'markdown'
      ],
      zip_safe=False
      )
