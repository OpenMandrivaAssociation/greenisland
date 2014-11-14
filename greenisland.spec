%define major 0
%define libname %mklibname GreenIsland %{major}
%define develname %mklibname GreenIsland -d
%define Werror_cflags %nil

Summary:	Compositor and shell for the Hawaii desktop environment
Name:		greenisland
Version:	0.3.0
Release:	1
Group:		Graphical desktop/Other
License:	BSD and LGPLv2+ and GPLv3+
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/mauios/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Designer)
BuildRequires:	pkgconfig(Qt5Compositor)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	cmake
BuildRequires:	python
BuildRequires:	bzip2-devel
BuildRequires:	qt5-devel
BuildRequires:	qtaccountsservice-devel
Requires:	hawaii-icon-theme
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
%setup -q

%build
export CC=gcc
export CXX=g++

%cmake
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
