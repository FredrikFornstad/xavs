%global libver 1
%define trunkname xavs-code-51-trunk

Summary: Audio Video Standard of China
Name: xavs
Version: 0.1.51
Release: 6%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://xavs.sourceforge.net/
Source0: %{trunkname}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: %{name}-libs_%{libver}

%description
AVS is the Audio Video Standard of China.  This project aims to
implement high quality AVS encoder and decoder.

%package libs_%{libver}
Summary: xavs codec shared library
Group: Development/Libraries
Obsoletes: libxavs*

%description libs_%{libver}
This package contains the xavs codec shared library

%package devel
Summary: xavs codec shared library development files
Group: Development/Libraries
Requires: %{name}-libs_%{libver}

%description devel
This package contain the xavs codec shared library development files

%prep
%setup -q -n %{trunkname}

%build
export CFLAGS="%{optflags}"
./configure \
  --bindir=%{_bindir} \
  --libdir=%{_libdir} \
  --includedir=%{_includedir} \
  --enable-pic --enable-shared

%install
rm -rf %{buildroot}
make install \
  DESTDIR=%{buildroot}

%post libs_%{libver} -p /sbin/ldconfig

%postun libs_%{libver} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/*.txt
%{_bindir}/xavs

%files libs_%{libver}
%defattr(-,root,root,-)
%{_libdir}/libxavs.so.%{libver}

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Sat Sep 5 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.51-6
- Changed source file

* Thu Jun 18 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.51-5
- Changed source file name to include version number to be accpted by the build system

* Sat Jun 13 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.51-4
- Removed dependency on atrpms scripts to comply with ClearOS policy

* Wed May 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.51-3
- Added atrpms-rpm-config as buildrequirement

* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.1.51-2
- Initial build.

