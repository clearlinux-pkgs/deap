#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deap
Version  : 1.0.1
Release  : 3
URL      : https://github.com/DEAP/deap/archive/1.0.1.tar.gz
Source0  : https://github.com/DEAP/deap/archive/1.0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: deap-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
DEAP stands for Distributed Evolutionary Algorithm in Python, it is dedicated to people who
wish to learn how to use evolutionary algorithms and to those who wish to
rediscover evolutionary algorithms. DEAP is the proof that evolutionary
algorithms do **not** need to be neither complex or complicated.

%package python
Summary: python components for the deap package.
Group: Default

%description python
python components for the deap package.


%prep
%setup -q -n deap-1.0.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1493237168
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1493237168
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
