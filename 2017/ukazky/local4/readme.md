So far, we've kept the library near our RF test scripts. In case we have a
bigger project, we can move the library into it's own git repo and utilize
pip as dependency manager. In `requirements.txt` we can specify this line

    git+https://github.com/mirobeka/PyCoffee.git#egg=pycoffee-library

And pip will install this dependency into our virtualenv automagically. We can
even specify git tag, to freeze library version. This is way how to do things
properly...

Above mentioned repo will probably be gone. You can take PyCoffee python module
and add it into your git server. You know, to play around...
