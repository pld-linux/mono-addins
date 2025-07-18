#
# Conditional build:
%bcond_without	gtk2	# GTK# 2.x Mono.Addins.GUI
%bcond_without	gtk3	# GTK# 3.x Mono.Addins.GUI
%bcond_without	monodoc	# monodoc documentation
%bcond_with	tests	# "make test" call [fails on UnitTests load???]
#
Summary:	Mono.Addins - framework for creating extensible applications and libraries
Summary(pl.UTF-8):	Mono.Addins - framework do tworzenia elastycznych aplikacji i bibliotek
Name:		mono-addins
Version:	1.3.3
Release:	4
License:	MIT
Group:		Development/Tools
# old download site
#Source0:	http://download.mono-project.com/sources/mono-addins/%{name}-%{version}.tar.gz
# newer releases on github:
#Source0Download: https://github.com/mono/mono-addins/tags
Source0:	https://github.com/mono/mono-addins/archive/%{name}-%{version}.tar.gz
# Source0-md5:	7ac27ffa4616fd03dc299749f16bce2a
Patch0:		%{name}-monodir.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-gtk3.patch
URL:		https://www.mono-project.com/Mono.Addins
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
%{?with_gtk2:BuildRequires:	dotnet-gtk-sharp2-devel >= 2.9.0}
%{?with_gtk3:BuildRequires:	dotnet-gtk-sharp3-devel >= 3.22}
BuildRequires:	mono-csharp >= 1.1.13
# mono-nunit
%{?with_tests:BuildRequires:	mono-devel}
%{?with_monodoc:BuildRequires:	mono-monodoc}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.015
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no native code here
%define		_enable_debug_packages	0

%description
Mono.Addins has been designed to be easy to use and useful for a wide
range of applications: from simple applications with small
extensibility needs, to complex applications which need support for
large add-in structures. This new framework intends to set an standard
for building extensible applications and add-ins in Mono.

%description -l pl.UTF-8
Mono.Addins zostało zaprojektowane jako proste i użyteczne narzędzie
dla różnych aplikacji: od prostych, z niewielkimi potrzebami
rozszerzalności, po złożone, wymagające wsparcia dla dużych struktur
dodatków. Ten nowy framework w zamiarach ma wyznaczać standard przy
budowaniu elastycznych aplikacji i dodatków w Mono.

%package devel
Summary:	Mono.Addins development files
Summary(pl.UTF-8):	Pliki programistyczne Mono.Addins
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Mono.Addins development files.

%description devel -l pl.UTF-8
Pliki programistyczne Mono.Addins.

%package gui
Summary:	Mono.Addins.Gui library for GTK# 2
Summary(pl.UTF-8):	Biblioteka Mono.Addins.Gui dla GTK# 2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gui
Mono.Addins.Gui library for GTK# 2.

%description gui -l pl.UTF-8
Biblioteka Mono.Addins.Gui dla GTK# 2.

%package gui-devel
Summary:	Development files for Mono.Addins.Gui library for GTK# 2
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Mono.Addins.Gui dla GTK# 2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}

%description gui-devel
Development files for Mono.Addins.Gui library for GTK# 2.

%description gui-devel -l pl.UTF-8
Pliki programistyczne biblioteki Mono.Addins.Gui dla GTK# 2.

%package gui-gtk3
Summary:	Mono.Addins.Gui library for GTK# 3
Summary(pl.UTF-8):	Biblioteka Mono.Addins.Gui dla GTK# 3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gui-gtk3
Mono.Addins.Gui library for GTK# 3 (Mono.Addins.GuiGtk3).

%description gui-gtk3 -l pl.UTF-8
Biblioteka Mono.Addins.Gui dla GTK# 3 (Mono.Addins.GuiGtk3).

%package gui-gtk3-devel
Summary:	Development files for Mono.Addins.Gui library for GTK# 3
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Mono.Addins.Gui dla GTK# 3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gui-gtk3 = %{version}-%{release}

%description gui-gtk3-devel
Development files for Mono.Addins.Gui library for GTK# 3.

%description gui-gtk3-devel -l pl.UTF-8
Pliki programistyczne biblioteki Mono.Addins.Gui dla GTK# 3.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	MCS=/usr/bin/mcs \
	%{?with_monodoc:--enable-docs} \
	%{!?with_gtk2:--disable-gui} \
	%{?with_gtk3:--enable-gui-gtk3} \
	%{?with_tests:--enable-tests}

%{__make} -j1

%{?with_tests:%{__make} -C Test test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mautil
%dir %{_prefix}/lib/mono/mono-addins
%{_prefix}/lib/mono/mono-addins/mautil.exe
%{_prefix}/lib/mono/gac/Mono.Addins
%{_prefix}/lib/mono/gac/Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/Mono.Addins.MSBuild
%{_prefix}/lib/mono/gac/Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.MSBuild
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.MSBuild
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.4.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.4.Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.4.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.4.Mono.Addins.MSBuild
%{_prefix}/lib/mono/gac/policy.0.4.Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.5.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.5.Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.5.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.5.Mono.Addins.MSBuild
%{_prefix}/lib/mono/gac/policy.0.5.Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.6.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.6.Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.6.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.6.Mono.Addins.MSBuild
%{_prefix}/lib/mono/gac/policy.0.6.Mono.Addins.Setup
%{_mandir}/man1/mautil.1*

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/mono-addins/Mono.Addins.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.CecilReflector.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.MSBuild.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Setup.dll
%if %{with monodoc}
%{_prefix}/lib/monodoc/sources/mono-addins-docs.*
%endif
%{_pkgconfigdir}/mono-addins.pc
%{_pkgconfigdir}/mono-addins-msbuild.pc
%{_pkgconfigdir}/mono-addins-setup.pc

%if %{with gtk2}
%files gui
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/Mono.Addins.Gui

%files gui-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Gui.dll
%{_pkgconfigdir}/mono-addins-gui.pc
%endif

%if %{with gtk3}
%files gui-gtk3
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/Mono.Addins.GuiGtk3
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.GuiGtk3
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.GuiGtk3
%{_prefix}/lib/mono/gac/policy.0.4.Mono.Addins.GuiGtk3
%{_prefix}/lib/mono/gac/policy.0.5.Mono.Addins.GuiGtk3
%{_prefix}/lib/mono/gac/policy.0.6.Mono.Addins.GuiGtk3

%files gui-gtk3-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/mono-addins/Mono.Addins.GuiGtk3.dll
%{_pkgconfigdir}/mono-addins-gui-gtk3.pc
%endif
