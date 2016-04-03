%define major 0
%define GreenIslandCompositor %mklibname GreenIslandCompositor %{major}
%define GreenIslandPlatform %mklibname GreenIslandPlatform %{major}
%define GreenIslandServer %mklibname GreenIslandServer %{major}
%define snap 20160314
%define _wayland 1.8.1

Summary:	QtQuick-based Wayland compositor in library form
Name:		greenisland
Version:	0.7.90
Release:	2.%{snap}.1
Group:		Graphical desktop/Other
License:	BSD and LGPLv2+ and GPLv3+
URL:		https://hawaii-desktop.github.io
Source0:	https://github.com/greenisland/greenisland/releases/download/v%{version}/%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Compositor)
#BuildRequires:	pkgconfig(Qt5PlatformSupport)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-client) >= %{_wayland}
BuildRequires:	pkgconfig(wayland-cursor) >= %{_wayland}
BuildRequires:	pkgconfig(wayland-server) >= %{_wayland}
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libsystemd-daemon)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb-xfixes)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(xcb-composite)
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(xcb-shape)
BuildRequires:	pkgconfig(xcb-damage)
BuildRequires:	pkgconfig(xcb-sync)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(EGL)
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	qt5-qtcompositor-private-devel
BuildRequires:	qt5-qtquick-private-devel
Requires:	%{GreenIslandCompositor} = %{EVRD}
Requires:	%{GreenIslandPlatform} = %{EVRD}
Requires:	%{GreenIslandServer} = %{EVRD}
Requires:	qt5-output-driver-eglfs
Requires:	qt5-qtgraphicaleffects

%track
prog %{name} = {
    url = https://github.com/greenisland/greenisland/releases/download/v%{version}/
    regex = "v(__VER__)\.tar\.xz"
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

%package -n %{GreenIslandCompositor}
Summary:	GreenIslandCompositor package for %{name}
Group:		System/Libraries

%description -n %{GreenIslandCompositor}
GreenIslandCompositor library for %{name}.

%package -n %{GreenIslandPlatform}
Summary:	GreenIslandPlatform package for %{name}
Group:		System/Libraries

%description -n %{GreenIslandPlatform}
GreenIslandPlatform library for %{name}.

%package -n %{GreenIslandServer}
Summary:	GreenIslandServer package for %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname GreenIsland 0} < 0.7.1
Provides:	%{mklibname GreenIsland 0} = 0.7.1

%description -n %{GreenIslandServer}
GreenIslandServer library for %{name}.

%package devel
Summary:	Devel files for %{name}
Group:		Development/C++
Requires:	%{name} = %{EVRD}

%description devel
Development files and headers for %{name}.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%global optflags %{optflags} -fno-permissive

%cmake_qt5 \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
    -DQtWaylandScanner_EXECUTABLE=%{_libdir}/qt5/bin/qtwaylandscanner

%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS README.md
%dir %{_libdir}/qt5/qml/GreenIsland
%dir %{_datadir}/greenisland
%dir %{_datadir}/greenisland/screen-data
%dir %{_datadir}/greenisland/shells
%dir %{_datadir}/greenisland/shells/org.hawaiios.greenisland
%dir %{_datadir}/greenisland/shells/org.hawaiios.greenisland/images
%dir %{_datadir}/greenisland/shells/org.hawaiios.greenisland/overlays
%{_bindir}/greenisland*
%{_libdir}/qt5/qml/GreenIsland/*.qml
%{_libdir}/qt5/qml/GreenIsland/libgreenislandplugin.so
%{_libdir}/qt5/qml/GreenIsland/qmldir
%{_libdir}/qt5/plugins/greenisland/egldeviceintegration/*.so
%{_libdir}/qt5/plugins/greenisland/extensions/*.so
%{_libdir}/qt5/plugins/greenisland/hardwareintegration/*.so
%{_libdir}/qt5/plugins/platforms/*.so
%{_datadir}/greenisland/screen-data/*.json
%{_datadir}/greenisland/shells/org.hawaiios.greenisland/metadata.desktop
%{_datadir}/greenisland/shells/org.hawaiios.greenisland/*.js
%{_datadir}/greenisland/shells/org.hawaiios.greenisland/*.qml
%{_datadir}/greenisland/shells/org.hawaiios.greenisland/images/wallpaper.png
%{_datadir}/greenisland/shells/org.hawaiios.greenisland/overlays/*.qml

%files -n %{GreenIslandCompositor}
%{_libdir}/libGreenIslandCompositor.so.%{major}*

%files -n %{GreenIslandPlatform}
%{_libdir}/libGreenIslandPlatform.so.%{major}*

%files -n %{GreenIslandServer}
%{_libdir}/libGreenIslandServer.so.%{major}*

%files devel
%dir %{_includedir}/Hawaii/GreenIsland
%{_includedir}/Hawaii/GreenIsland/*
%{_includedir}/Hawaii/*.h
%{_libdir}/libGreenIsland*.so
%{_libdir}/cmake/GreenIsland
%{_libdir}/pkgconfig/GreenIsland*.pc
%{_libdir}/qt5/mkspecs/modules/*.pri
