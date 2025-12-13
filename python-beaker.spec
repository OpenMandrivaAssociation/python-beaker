Summary:	WSGI middleware layer to provide sessions
Name:		python-beaker
Version:	1.13.0
Release:	1
Group:		Development/Python
License:	BSD
Url:		https://pypi.python.org/pypi/Beaker
Source0:	https://files.pythonhosted.org/packages/source/B/Beaker/Beaker-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
%rename		python3-beaker

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%files
%dir %{py_puresitedir}/beaker
%{py_puresitedir}/beaker/*
%{py_puresitedir}/Beaker*
