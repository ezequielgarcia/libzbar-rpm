Name: libzbar
Summary: bar code scanning and decoding
Version: 0.23.90
Release: 1
License: LGPL
Group: Development/Libraries
URL: https://git.linuxtv.org/zbar.git/
Packager: Vit Hrachovy <fangorn34@users.sourceforge.net>
Source0:  https://linuxtv.org/downloads/zbar/zbar-0.23.90.tar.gz
Requires: ImageMagick-c++
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
The ZBar Bar Code Reader is a library for scanning and decoding bar
codes from various sources such as video streams, image files or raw
intensity sensors.  It supports EAN, UPC, Code 128, Code 93, Code 39
and Interleaved 2 of 5. The flexible, layered architecture features a
fast, streaming interface with a minimal memory footprint.

%package devel
Group: Development/Libraries
Summary: bar code library extra development files
Requires: %{name} = %{version}

%description devel
The ZBar Bar Code Reader is a library for scanning and decoding bar
codes from various sources such as video streams, image files or raw
intensity sensors.  It supports EAN, UPC, Code 128, Code 93, Code 39
and Interleaved 2 of 5. The flexible, layered architecture features a
fast, streaming interface with a minimal memory footprint.

This package contains header files and additional libraries used for
developing applications that read bar codes with this library.

%prep
%setup -q -n zbar-%{version}

%build
./configure --prefix=%{_prefix} --libdir=%{_prefix}/lib64 \
  --enable-shared --disable-static \
  --without-gtk --without-python --without-qt --without-dbus --disable-doc --disable-video \
  CFLAGS="${CFLAGS:-%optflags}" \
  CXXFLAGS="${CXXFLAGS:-%optflags}"
make

%install
%make_install
rm -rf %{buildroot}/usr/share/*

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_libdir}/*.la

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_includedir}/zbar.h
%{_includedir}/zbar/*.h

%changelog
