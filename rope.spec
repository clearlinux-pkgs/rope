#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rope
Version  : 0.10.7
Release  : 8
URL      : https://pypi.python.org/packages/7e/fc/702c0293b57edd4d70146e36f9413c40339a701a43c8fa6918fb9d834913/rope-0.10.7.tar.gz
Source0  : https://pypi.python.org/packages/7e/fc/702c0293b57edd4d70146e36f9413c40339a701a43c8fa6918fb9d834913/rope-0.10.7.tar.gz
Summary  : a python refactoring library...
Group    : Development/Tools
License  : GPL-2.0
Requires: rope-python3
Requires: rope-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. _GitHub python-rope / rope: https://github.com/python-rope/rope
========================================
rope, a python refactoring library ...
========================================

%package python
Summary: python components for the rope package.
Group: Default
Requires: rope-python3

%description python
python components for the rope package.


%package python3
Summary: python3 components for the rope package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rope package.


%prep
%setup -q -n rope-0.10.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515337664
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
