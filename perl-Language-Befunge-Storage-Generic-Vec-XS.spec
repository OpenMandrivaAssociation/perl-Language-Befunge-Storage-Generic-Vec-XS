%define upstream_name Language-Befunge-Storage-Generic-Vec-XS
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Language::Befunge::Storage::Generic::Vec rewritten for speed
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Language/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	%{name}.rpmlintrc

BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Language::Befunge)
BuildRequires:	perl(Language::Befunge::Vector::XS)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(aliased)
BuildRequires:	perl-devel
Requires:	perl(aliased)

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.30.0-2
+ Revision: 773643
- clean out spec
- add filter exception on description-line-too-long for debug package
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1
+ Revision: 644753
- update to new version 0.03

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 401649
- rebuild using %%perl_convert_version
- fixed license field

* Sun Nov 16 2008 Jérôme Quelin <jquelin@mandriva.org> 0.02-1mdv2009.1
+ Revision: 303786
- another missing prereq
- missing prereq
- import perl-Language-Befunge-Storage-Generic-Vec-XS


* Sun Nov 16 2008 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

