#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Resolver-CVS
Summary:	MasonX::Resolver::CVS - component path resolver for components in CVS
#Summary(pl):	
Name:		perl-MasonX-Resolver-CVS
Version:	0.02
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	390dae143a49b653827e3448901d7e5f
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Mason
BuildRequires:	perl-Params-Validate
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This L<HTML::Mason::Resolver(3)|HTML::Mason::Resolver(3)> subclass
is used when components are stored in the Concurrent Version System
(L<cvs(1)|cvs(1)>).  Currently, this subclass only supports local CVS
repositories.  As such, it is able to deliver component source without
checking the files out into a working directory (see L<"IMPLEMENTATION
NOTES">).

# %description -l pl
# TODO

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
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
