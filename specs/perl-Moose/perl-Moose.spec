# $Id$
# Authority: shuff
# Upstream: Stevan Little <stevan.little$iinteractive,com>
# ExcludeDist: el2 el3 el4 el5
# Rationale: requires a newer Class::MOP

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Moose

Summary: Postmodern object system for Perl 5
Name: perl-Moose
Version: 1.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Moose/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Moose-%{version}.tar.gz
Patch0: %{name}_checkconflicts.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP) >= 1.11
BuildRequires: perl(Data::OptList)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils) >= 0.12
BuildRequires: perl(Package::DeprecationManager) >= 0.10
BuildRequires: perl(Params::Util) >= 1.00
BuildRequires: perl(Scalar::Util) >= 1.19
BuildRequires: perl(Sub::Exporter) >= 0.980
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Task::Weaken)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny) >= 0.02
BuildRequires: perl >= 5.8.3
Requires: perl(Carp)
Requires: perl(Class::MOP) >= 1.11
Requires: perl(Data::OptList)
Requires: perl(List::MoreUtils) >= 0.12
Requires: perl(Package::DeprecationManager) >= 0.10
Requires: perl(Params::Util) >= 1.00
Requires: perl(Scalar::Util) >= 1.19
Requires: perl(Sub::Exporter) >= 0.980
Requires: perl(Sub::Name)
Requires: perl(Task::Weaken)
Requires: perl(Try::Tiny) >= 0.02
Requires: perl >= 5.8.3

Conflicts: perl(Catalyst) <= 5.80028
Conflicts: perl(Devel::REPL) <= 1.003008
Conflicts: perl(Fey) <= 0.36
Conflicts: perl(Fey::ORM) <= 0.34
Conflicts: perl(File::ChangeNotify) <= 0.15
Conflicts: perl(KiokuDB) <= 0.49
Conflicts: perl(Markdent) <= 0.16
Conflicts: perl(MooseX::Aliases) <= 0.07
Conflicts: perl(MooseX::AlwaysCoerce) <= 0.05
Conflicts: perl(MooseX::AttributeHelpers) <= 0.22
Conflicts: perl(MooseX::AttributeInflate) <= 0.02
Conflicts: perl(MooseX::Attribute::Prototype) <= 0.10
Conflicts: perl(MooseX::ClassAttribute) <= 0.17
Conflicts: perl(MooseX::FollowPBP) <= 0.02
Conflicts: perl(MooseX::NonMoose) <= 0.55
Conflicts: perl(MooseX::Params::Validate) <= 0.05
Conflicts: perl(MooseX::POE) <= 0.205
Conflicts: perl(MooseX::Role::Cmd) <= 0.06
Conflicts: perl(MooseX::Role::WithOverloading) <= 0.07
Conflicts: perl(MooseX::Singleton) <= 0.24
Conflicts: perl(MooseX::StrictConstructor) <= 0.08
Conflicts: perl(MooseX::Types) <= 0.19
Conflicts: perl(MooseX::UndefTolerant) <= 0.04
Conflicts: perl(namespace::autoclean) <= 0.08
Conflicts: perl(Pod::Elemental) <= 0.093280

%filter_from_requires /^perl*/d
%filter_setup


%description
Moose is a Perl module that implements a complete modern object system.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Moose/
%{perl_vendorarch}/Moose.pm
%{perl_vendorarch}/oose.pm
%dir %{perl_vendorarch}/Test/
%{perl_vendorarch}/Test/Moose.pm
%{perl_vendorarch}/auto/Moose/Moose.bs
%{perl_vendorarch}/auto/Moose/Moose.so

%changelog
* Tue Aug 23 2011 Steve Huff <shuff@vecna.org> - 1.25-1
- Updated to version 1.25 (el6 only) - last pre-2.0 Moose release.
- Split out perl-Moose-1.02 as a separate spec.

* Fri Oct 08 2010 Steve Huff <shuff@vecna.org> - 1.02-2
- Fixed a mis-specified conflict.

* Tue Jun 08 2010 Steve Huff <shuff@vecna.org> - 1.02-1
- Updated to version 1.02.
- Later versions require an updated Class::MOP.

* Fri Mar 26 2010 Steve Huff <shuff@vecna.org> - 1.00-1
- Updated to version 1.00!
- Upstream is back to Stevan Little.
- oose.pm requires Filter::Simple.
- Captured conflicts defined in Makefile.PL.
- Patched out check_conflicts() call.

* Fri Feb 05 2010 Steve Huff <shuff@vecna.org> - 0.95-1
- Updated to version 0.95.
- Upstream is now Florian Ragwitz.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.94-1
- Updated to version 0.94.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.93-2
- Change Source: Tag
- dependencies from yaml

* Tue Dec 01 2009 Steve Huff <shuff@vecna.org> - 0.93-1
- Updated to version 0.93.

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 0.89-2
- Remove version from Scalar::Util dependency

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 0.89-1
- Updated to version 0.89.

* Fri Jul 31 2009 Christoph Maser <cmr@financial.com> - 0.88-1
- Updated to version 0.88.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.87-1
- Updated to version 0.87.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.86-1
- Updated to version 0.86.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.85-1
- Updated to version 0.85.

* Thu May 28 2009 Christoph Maser <cmr@financial.com> - 0.79-1
- Updated to release 0.79.

* Wed Nov 26 2008 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.59-1
- Updated to release 0.59.

* Thu Aug 21 2008 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Fri Jul 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Wed Jun 25 2008 Dag Wieers <dag@wieers.com> - 0.50-1
- Updated to release 0.50.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.44-1
- Updated to release 0.44.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.38-1
- Updated to release 0.38.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
