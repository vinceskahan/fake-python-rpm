Name: fake_python
Version: 0.1
Release: 1
Summary: fake rpm to 'provide python' for weewx
AutoReqProv: no
BuildRoot: %buildroot
Prefix: /
BuildArch: noarch
Provides: /usr/bin/python
Provides: python

Group: default
License: none
Vendor: None
URL: None
Packager: vinceskahan@gmail.com

%description
This rpm 'provides' python to work around
a requirement in weewx-4.1.0 for centos8,
which does not have a package that provides
python.  It actually installs nothing other
than making the rpmdb 'think' python is there.

%prep

%build

%install

%clean




%files
%defattr(-,root,root,-)

%changelog

