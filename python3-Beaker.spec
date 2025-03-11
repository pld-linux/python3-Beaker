#
# Conditional build:
%bcond_with	tests	# unit tests (TODO: dependencies)

%define		module	Beaker
Summary:	Session (and caching soon) WSGI Middleware
Summary(pl.UTF-8):	Middleware WSGI obsługi sesji (i wkrótce pamięci podręcznej)
Name:		python3-%{module}
Version:	1.12.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/beaker/
Source0:	https://files.pythonhosted.org/packages/source/B/Beaker/%{module}-%{version}.tar.gz
# Source0-md5:	68b406115ea9fef858b8aeba514c9d39
URL:		https://beaker.readthedocs.io/
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography
BuildRequires:	python3-memcached
BuildRequires:	python3-modules-sqlite
BuildRequires:	python3-nose
BuildRequires:	python3-pycparser = 2.18
BuildRequires:	python3-pycryptodome
BuildRequires:	python3-pylibmc
BuildRequires:	python3-pymongo
BuildRequires:	python3-redis
BuildRequires:	python3-sqlalchemy
BuildRequires:	python3-webtest < 2.0.24
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beaker is a simple WSGI middleware to use the Myghty Container API.

MyghtyUtils contains a very robust Container API for storing data
using various backends. Beaker uses those APIs to implement common web
application wrappers, like sessions and caching, in WSGI middleware.
Currently the only middleware implemented is that for sessions but
more is coming soon.

%description -l pl.UTF-8
Beaker jest prostym middleware WSGI do użytku API Myghty Container.

MythtyUtils zawiera bardzo mocne API Container do przechowywania
danych przy użyciu różnych backendów. Beaker używa tych API do
implementacji ogólnych wrapperów aplikacji WWW, takich jak sesje czy
pamięć podręczna wewnątrz middleware WSGI. Aktualnie zaimplementowane
jest jedynie middleware dla sesji, ale wkrótce będzie więcej.

%prep
%setup -qn %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/beaker
%{py3_sitescriptdir}/Beaker-%{version}-py*.egg-info
