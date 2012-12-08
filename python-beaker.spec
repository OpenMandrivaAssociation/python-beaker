Name: python-beaker
Version: 1.5.3
Release: %mkrel 5
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.3-3mdv2011.0
+ Revision: 667912
- mass rebuild

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 1.5.3-2mdv2011.0
+ Revision: 589931
- rebuild for python 2.7

* Wed Mar 03 2010 Frederik Himpe <fhimpe@mandriva.org> 1.5.3-1mdv2010.1
+ Revision: 514015
- update to new version 1.5.3

* Fri Jan 08 2010 Frederik Himpe <fhimpe@mandriva.org> 1.5.1-1mdv2010.1
+ Revision: 487767
- update to new version 1.5.1

* Thu Aug 20 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4-1mdv2010.0
+ Revision: 418609
- update to new version 1.4

* Sun Jul 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 395150
- First Mandriva package based on Fedora's SPEC
- create python-beaker

