
%define realname   Language-Befunge-Storage-Generic-Vec-XS
%define version    0.02
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Language::Befunge::Storage::Generic::Vec rewritten for speed
Source:     http://www.cpan.org/modules/by-module/Language/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Language::Befunge)
BuildRequires: perl(Language::Befunge::Vector::XS)
BuildRequires: perl(Test::More)



%description
Language::Befunge::Storage::Generic::Vec implements a linear storage model,
where a perl string is used to store a (potentially very large) integer
array. The integers are accessed from perl with vec().

Unfortunately, vec() operates on unsigned integers, which means some extra
calculations are necessary to convert between unsigned and signed integers.

If the access was done from C, using a signed integer pointer, the access
would be much faster, and the conversion would be unnecessary.

%prep
%setup -q -n %{realname}-%{version} 

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


