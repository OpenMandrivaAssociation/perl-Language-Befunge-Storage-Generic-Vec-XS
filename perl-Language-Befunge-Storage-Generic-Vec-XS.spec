%define upstream_name    Language-Befunge-Storage-Generic-Vec-XS
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Language::Befunge::Storage::Generic::Vec rewritten for speed
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Language/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Language::Befunge)
BuildRequires: perl(Language::Befunge::Vector::XS)
BuildRequires: perl(Test::More)
BuildRequires: perl(aliased)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: perl(aliased)

%description
Language::Befunge::Storage::Generic::Vec implements a linear storage model,
where a perl string is used to store a (potentially very large) integer
array. The integers are accessed from perl with vec().

Unfortunately, vec() operates on unsigned integers, which means some extra
calculations are necessary to convert between unsigned and signed integers.

If the access was done from C, using a signed integer pointer, the access
would be much faster, and the conversion would be unnecessary.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*

