%define major 0
%define libname %mklibname GreenIsland %{major}
%define develname %mklibname GreenIsland -d
%define Werror_cflags %nil
%define _disable_ld_no_undefined 1
%define snap 20150328

Summary:	Compositor and shell for the Hawaii desktop environment
Name:		greenisland
Version:	0.5.90
Release:	0.%{snap}.1
Group:		Graphical desktop/Other
License:	BSD and LGPLv2+ and GPLv3+
URL:		http://www.maui-project.org
# git archive --format=tar --prefix=greenisland-0.5.90-$(date +%Y%m%d)/ HEAD | xz -vf > greenisland-0.5.90-$(date +%Y%m%d).tar.xz
Source0:	http://downloads.sourceforge.net/mauios/%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Compositor)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Screen)
BuildRequires:	cmake(KF5Package)
Requires:	%{libname} = %{EVRD}

%track
prog %{name} = {
    url = http://downloads.sourceforge.net/project/mauios/hawaii/
    regex = "%{name}-(__VER__)\.tar\.gz"
    version = %{version}
}

%description
Wayland compositor and shell library for the Hawaii desktop environment.

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
%setup -qc

%build
%global optflags %{optflags} -fno-permissive
%{_libdir}/qt5/bin/qtwaylandscanner server-header /usr/share/wayland/protocol/wayland.xml > src/plugins/compositors/system/qwayland-server-wayland.h

%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_libdir}/hawaii

%files -n %{libname}
%{_libdir}/libGreenIsland.so.%{major}*

%files -n %{develname}
%doc AUTHORS README.md
%{_includedir}/GreenIsland
%{_libdir}/cmake/GreenIsland
%{_libdir}/libGreenIsland.so
