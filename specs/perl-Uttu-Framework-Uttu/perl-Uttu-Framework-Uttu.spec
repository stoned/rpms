# $Id$
# Authority: dag
# Upstream: James G Smith <cpan$jamesmith,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Uttu-Framework-Uttu

Summary: Perl module that implements a framework for Uttu site
Name: perl-Uttu-Framework-Uttu
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Uttu-Framework-Uttu/

Source: http://www.cpan.org/authors/id/J/JS/JSMITH/Uttu-Framework-Uttu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Uttu-Framework-Uttu is a Perl module that implements
a framework for Uttu site.

This package contains the following Perl module:

    Uttu::Framework::Uttu

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/Uttu::Framework::Uttu.3pm*
%dir %{perl_vendorlib}/Uttu/
%dir %{perl_vendorlib}/Uttu/Framework/
#%{perl_vendorlib}/Uttu/Framework/Uttu/
%{perl_vendorlib}/Uttu/Framework/Uttu.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
