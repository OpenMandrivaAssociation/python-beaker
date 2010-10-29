Name: python-beaker
Version: 1.5.3
Release: %mkrel 2
Summary: WSGI middleware layer to provide sessions

Group: Development/Python
License: BSD
URL: http://beaker.groovie.org/
Source0: http://pypi.python.org/packages/source/B/Beaker/Beaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildArch: noarch
BuildRequires: python-setuptools

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.


%prep
%setup -q -n Beaker-%{version}
# Fix rpmlint warning
sed -i -e '/\/usr\/bin\/python/d' beaker/crypto/pbkdf2.py


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE CHANGELOG
%{python_sitelib}/beaker/
%{python_sitelib}/Beaker*
