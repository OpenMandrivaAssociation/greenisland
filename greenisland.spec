%define major 0
%define libname %mklibname GreenIsland %{major}
%define develname %mklibname GreenIsland -d
%define Werror_cflags %nil
%define _disable_ld_no_undefined 1
%define snap 20150516

Summary:	QtQuick-based Wayland compositor in library form
Name:		greenisland
Version:	0.5.93
Release:	0.%{snap}.1
Group:		Graphical desktop/Other
License:	BSD and LGPLv2+ and GPLv3+
URL:		https://hawaii-desktop.github.io
# git archive --format=tar --prefix=greenisland-0.5.93-$(date +%Y%m%d)/ HEAD | xz -vf > greenisland-0.5.93-$(date +%Y%m%d).tar.xz
Source0:	https://github.com/greenisland/%{name}/archive/%{name}-%{version}-%{snap}.tar.xz
#Source0:	https://github.com/greenisland/%{name}/archive/v%{version}-%{snap}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Compositor)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(EGL)
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	qt5-qtcompositor-private-devel
Requires:	%{libname} = %{EVRD}
Requires:	qt5-output-driver-eglfs
Requires:	qt5-qtgraphicaleffects

%track
prog %{name} = {
    url = https://github.com/greenisland/%{name}/archive/
    regex = "v(__VER__)\.tar\.gz"
    version = %{version}
}

%description
QtQuick-based Wayland compositor in library form.

The API extends QtCompositor with additional features needed by any real world
Wayland compositor.

Green Island offers multiple screen support and it also implements specific
protocols such as xdg-shell, gtk-shell and those for Plasma 5.

Also include a screencaster protocol and command line application, plus a
minimal Wayland compositor written with QML.

Green Island can be used by any desktop environment that wish to implement
its compositor by using QML or for shells deeply integrated with the compositor
in the same process.

%package -n %{libname}
Summary:	Main package for %{name}
Group:		System/Libraries

%description -n %{libname}
Main library for %{name}.

%package -n %{develname}
Summary:	Devel files for %{name}
Group:		Development/C++
Requires:	%{name} = %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -qn %{name}-%{version}-%{snap}
%apply_patches

%build
%global optflags %{optflags} -fno-permissive

%cmake_qt5 \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
    -DQtWaylandScanner_EXECUTABLE=%{_libdir}/qt5/bin/qtwaylandscanner

%make

%install
%makeinstall_std -C build

%files
%doc LICENSE.BSD LICENSE.GPL LICENSE.LGPL
%dir %{_libdir}/qt5/qml/GreenIsland
%dir %{_datadir}/greenisland
%dir %{_datadir}/greenisland/org.greenisland.simple
%dir %{_datadir}/greenisland/org.greenisland.simple/images
%dir %{_datadir}/greenisland/org.greenisland.simple/overlays
%{_bindir}/greenisland*
%{_libdir}/qt5/plugins/greenisland/plasma.so
%{_libdir}/qt5/qml/GreenIsland/*.qml
%{_libdir}/qt5/qml/GreenIsland/libgreenislandplugin.so
%{_libdir}/qt5/qml/GreenIsland/qmldir
%{_datadir}/greenisland/org.greenisland.simple/*.qml
%{_datadir}/greenisland/org.greenisland.simple/overlays/*.qml
%{_datadir}/greenisland/org.greenisland.simple/*.js
%{_datadir}/greenisland/org.greenisland.simple/images/*.png

%files -n %{libname}
%{_libdir}/libGreenIsland.so.%{major}*

%files -n %{develname}
%doc AUTHORS README.md
%{_includedir}/GreenIsland
%{_libdir}/cmake/GreenIsland
%{_libdir}/libGreenIsland.so
