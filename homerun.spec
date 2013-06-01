Name:           homerun
Summary:        Fullscreen Launcher for KDE
Version:        1.0.0
Release:        1
License:        GPL-2.0+,LGPL-2.1+,BSD
Group:          Graphical desktop/KDE
Source0:        ftp://ftp.kde.org/pub/kde/stable/homerun/src/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://userbase.kde.org/Homerun
Requires:       kdebase4-runtime >= 4.9.3
Requires:       libqtgui4 >= 4.8.1
Requires:       libhomerun = %{version}
BuildRequires:  kdebase4-workspace-devel >= 4.8.0
BuildRequires:  desktop-file-utils
BuildRequires:  kdebase4-runtime-devel >= 4.8.0
BuildRequires:  kdebase4-devel >= 4.8.0

%description
Homerun is a fullscreen launcher with content organized in tabs. A tab is composed
of several "sources". A source can provide one or more sections to a tab. Homerun
comes with a few built-in sources, but custom sources can be written using libhomerun. 

%package -n libhomerun
Summary:        Libraries Needed by Homerun
Requires:       kdebase4-runtime >= 4.9.3
Requires:       libqtgui4 >= 4.8.1

%description -n libhomerun
This package provides libraries, data engines, and icons needed by all
public transport plasma applets.


%package -n homerun-devel
Summary:        Development Files for Homerun
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       libhomerun = %{version}

%description -n homerun-devel
This package provides development libraries and headers needed to build
software using Homerun.

%prep
%setup -q

%build
  %cmake
  %make

%install
%makeinstall_std -C build

%post   -n libhomerun -p /sbin/ldconfig
%postun -n libhomerun -p /sbin/ldconfig


%files
%doc COPYING LICENSE.BSD LICENSE.GPL-2 LICENSE.LGPL-2.1 NEWS README.md
%{_bindir}/homerunviewer
%{_libdir}/kde4/*.so
%{_libdir}/kde4/imports/org/kde/homerun
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/homerun-source.desktop
%{_datadir}/apps/*
%{_datadir}/config/homerunrc
%{_iconsdir}/hicolor/*/apps/homerun.*
%{_datadir}/locale/*

%files -n libhomerun
%{_libdir}/libhomerun.so.*

%files -n homerun-devel
%{_libdir}/libhomerun.so
%{_libdir}/cmake/Homerun
%{_includedir}/homerun

