
This builds a bogus 'fake-python' rpm to require /usr/bin/python, so that the (erronious) requires in weewx-4.1.0 rpms can be met on a centos8 system, which does not 'have' such a file.

Basically we're faking the rpmdb out until the package can be updated and (re)released officially.

### how to build
rpmbuild -ba fake_python.spec
install the resulting noarch rpm

