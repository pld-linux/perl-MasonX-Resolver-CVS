#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MasonX
%define		pnam	Resolver-CVS
Summary:	MasonX::Resolver::CVS - component path resolver for components in CVS
Summary(pl.UTF-8):   MasonX::Resolver::CVS - resolver ścieżek komponentów dla komponentów w CVS-ie
Name:		perl-MasonX-Resolver-CVS
Version:	0.02
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	390dae143a49b653827e3448901d7e5f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Mason
BuildRequires:	perl-Params-Validate
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This HTML::Mason::Resolver(3) subclass is used when components are
stored in the Concurrent Version System (cvs(1)). Currently, this
subclass only supports local CVS repositories. As such, it is able to
deliver component source without checking the files out into a working
directory.

%description -l pl.UTF-8
Ta podklasa HTML::Mason::Resolver jest używana gdy komponenty są
zapisane w systemie CVS. Aktualnie podklasa ta obsługuje tylko lokalne
repozytoria CVS. Jako taka, jest w stanie dostarczać źródło
komponentów bez pobierania plików do bieżącego katalogu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
