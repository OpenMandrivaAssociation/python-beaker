Summary:	WSGI middleware layer to provide sessions
Name:		python-beaker
Version:	1.11.0
Release:	5
Group:		Development/Python
License:	BSD
Url:		http://pypi.python.org/pypi/Beaker
Source0:	https://files.pythonhosted.org/packages/source/B/Beaker/Beaker-1.11.0.tar.gz
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	pkgconfig(python)
%rename		python3-beaker

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%prep
%autosetup -p1 -n Beaker-%{version}

%build
%py_build

%install
python setup.py install --skip-build --root %{buildroot}
%py_install

%files
%dir %{py_puresitedir}/beaker
%{py_puresitedir}/beaker/*
%{py_puresitedir}/Beaker*
