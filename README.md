# Python Package Tutorial

This tutorial helps you understand how to package your Python Code

I used the following link as a guideline - https://python-packaging.readthedocs.io/en/latest/dependencies.html

The initial directory structure for funniest should look like this:

```
pip_package_example/
    piptutorial/
        __init__.py
        test.py
    setup.py
```

Requires a setup config file like so:

```
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
```


To prove this works, we need to run 

```
python3 setup.py develop
```

Now we can install the package locally (for use on our system), with:

```
pip install .
```

We can also install the package with a symlink, so that changes to the source files will be immediately available to other users of the package on our system:

```
pip install -e .
```

Anywhere else in our system, we can do this now:

```
import piptutorial
print (piptutorial.joke())
```