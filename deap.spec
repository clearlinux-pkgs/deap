#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deap
Version  : 1.2.2
Release  : 21
URL      : https://github.com/DEAP/deap/archive/1.2.2.tar.gz
Source0  : https://github.com/DEAP/deap/archive/1.2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: deap-python3
Requires: deap-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
# DEAP
[![Build status](https://travis-ci.org/DEAP/deap.svg?branch=master)](https://travis-ci.org/DEAP/deap) [![Download](https://img.shields.io/pypi/dm/deap.svg)](https://pypi.python.org/pypi/deap) [![Join the chat at https://gitter.im/DEAP/deap](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/DEAP/deap?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package python
Summary: python components for the deap package.
Group: Default
Requires: deap-python3

%description python
python components for the deap package.


%package python3
Summary: python3 components for the deap package.
Group: Default
Requires: python3-core

%description python3
python3 components for the deap package.


%prep
%setup -q -n deap-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523287711
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
