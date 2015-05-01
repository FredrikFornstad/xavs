%lib_package xavs 1

Summary: Audio Video Standard of China
Name: xavs
Version: 0.1.51
Release: 2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://xavs.sourceforge.net/
Source0: %{name}-trunk.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
AVS is the Audio Video Standard of China.  This project aims to
implement high quality AVS encoder and decoder.

%prep
%setup -q -n trunk

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/*.txt
%{_bindir}/xavs

%changelog
* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.1.51-2
- Initial build.

