%define module beaker

Name:		python-beaker
Summary:	WSGI middleware layer to provide sessions
Version:	1.14.1
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://beaker.readthedocs.org/
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# repo - https://github.com/bbangert/beaker

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%rename		python3-beaker

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
