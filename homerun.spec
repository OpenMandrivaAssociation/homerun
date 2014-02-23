%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Fullscreen Launcher for KDE
Name:		homerun
Version:	1.2.0
Release:	3
License:	GPLv2+, LGPLv2.1+, BSD
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Homerun
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/src/%{name}-%{version}.tar.xz
Patch0:		homerun-1.2.0-use-openmandriva-icon.patch
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-devel
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime

%description
Homerun is a fullscreen launcher with content organized in tabs. A tab is
composedof several "sources". A source can provide one or more sections to
a tab. Homerun comes with a few built-in sources, but custom sources can be
written using libhomerun.

%files -f plasma_applet_org.kde.homerun.lang
%doc COPYING LICENSE.BSD LICENSE.GPL-2 LICENSE.LGPL-2.1 NEWS README.md
%{_kde_bindir}/homerunviewer
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/plasma/plasmoids/org.kde.homerun
%{_kde_appsdir}/plasma/plasmoids/org.kde.homerun-kicker
%{_kde_configdir}/homerunrc
%{_kde_iconsdir}/hicolor/*/apps/homerun.*
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/kde4/imports/org/kde/homerun
%{_kde_services}/*.desktop
%{_kde_servicetypes}/homerun-source.desktop
%{_datadir}/config/homerunkickerrc


#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libname}
This package provides libraries, data engines, and icons needed by all public
transport plasma applets.

%files -n %{libname}
%{_kde_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	KDE 4 core library
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides development libraries and headers needed to build
software using Homerun.

%files -n %{devname}
%{_kde_libdir}/lib%{name}.so
%{_kde_libdir}/cmake/Homerun
%{_kde_includedir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang plasma_applet_org.kde.homerun

