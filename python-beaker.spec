Summary:	WSGI middleware layer to provide sessions
Name:		python-beaker
Version:	1.11.0
Release:	3
Group:		Development/Python
License:	BSD
Url:		http://pypi.python.org/pypi/Beaker
Source0:	https://files.pythonhosted.org/packages/source/B/Beaker/Beaker-1.11.0.tar.gz
BuildArch:	noarch
BuildRequires:	python2-setuptools
BuildRequires:	python-distribute
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
%rename		python3-beaker

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%package -n python2-beaker
Summary:	WSGI middleware layer to provide sessions
Group:		Development/Python
 
%description -n python2-beaker
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%prep
%autosetup -p0 -c Beaker-%{version}

mv Beaker-%{version} python2
cp -r python2 python3

%build
pushd python2
python2 setup.py build
popd

pushd python3
python setup.py build
popd


%install
pushd python2
python2 setup.py install --skip-build --root %{buildroot}
popd

pushd python3
python setup.py install --skip-build --root %{buildroot}
popd

%files
#doc python3/LICENSE python3/CHANGELOG
%{py_puresitedir}/beaker/
%{py_puresitedir}/Beaker*

%files -n python2-beaker
#doc python2/LICENSE python2/CHANGELOG
%{py2_puresitedir}/beaker/
%{py2_puresitedir}/Beaker*
