# $Id$
# Authority: matthias

Summary: Fast Assembly MPEG Encoding library
Name: libfame
Version: 0.9.1
Release: 2
License: LGPL
Group: System Environment/Libraries
URL: http://fame.sourceforge.net/
Source: http://dl.sf.net/fame/%{name}-%{version}.tar.gz
Patch: libfame-0.9.1-fstrict-aliasing.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A library for fast (real-time) MPEG video encoding, written in C and assembly.
It currently allows encoding of fast MPEG-1 video, as well as MPEG-4 (OpenDivX
compatible) rectangular and arbitrary shaped video.


%package devel
Summary: Development files and static libraries for libfame
Group: Development/Libraries
Requires: %{name} = %{version}
BuildRequires: autoconf, automake, libtool

%description devel
A library for fast (real-time) MPEG video encoding, written in C and assembly.
It currently allows encoding of fast MPEG-1 video, as well as MPEG-4 (OpenDivX
compatible) rectangular and arbitrary shaped video.

This package contains the files necessary to build programs that use the
libfame library.


%prep
%setup
%patch -p1 -b .fstrict-aliasing


%build
for file in ChangeLog NEWS; do
    test -e ${file} || touch ${file}
done
autoreconf --force --install --symlink
# Compile a special MMX & SSE enabled lib first
%ifarch %{ix86}
    %configure --enable-sse --enable-mmx
    %{__make} %{?_smp_mflags}
    %{__mkdir} sse2/
    %{__mv} src/.libs/libfame*.so.* sse2/
    %{__make} clean
%endif

# Now, the normal build
%configure --disable-mmx
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Install the MMX & SSE build in its special dir
%ifarch %{ix86}
    %{__mkdir_p} %{buildroot}%{_libdir}/sse2
    %{__cp} -a sse2/* %{buildroot}%{_libdir}/sse2/
%endif

# Workaround for direct <libfame/fame.h> includes (include/libfame -> .)
%{__ln_s} . %{buildroot}%{_includedir}/%{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING README TODO 
%{_libdir}/*.so.*
%ifarch %{ix86}
    %{_libdir}/sse2/*.so.*
%endif

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/%{name}-config
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man3/*


%changelog
* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-3
- Add libfame-0.9.1-fstrict-aliasing.patch to actually make the lib work,
  thanks to Nicholas Miell.

* Tue Aug 31 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-2
- Add specially compiled MMX & SSE lib on x86.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-1
- Update to 0.9.1.
- Updated the Source URL.

* Fri Dec  5 2003 Matthias Saou <http://freshrpms.net/> 0.9.0-4
- Added /usr/include/libfame -> . symlink as a workaround for MPlayer.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.9.0-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- release 2

* Mon Jun 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adapted from PLD spec file for GStreamer packaging

