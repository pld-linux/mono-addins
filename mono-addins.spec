%include	/usr/lib/rpm/macros.mono
Summary:	Mono.Addins - framework for creating extensible applications and libraries
Summary(pl.UTF-8):	Mono.Addins - framework do tworzenia elastycznych aplikacji i bibliotek
Name:		mono-addins
Version:	0.4
Release:	2
License:	GPL/MIT
Group:		Development/Tools
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/mono-addins/%{name}-%{version}.tar.bz2
# Source0-md5:	3b7f3f6e55c95413df184d0e4c9233e4
Patch0:		%{name}-pkglibdir64.patch
Patch1:		%{name}-pkglibdir.patch
URL:		http://www.mono-project.com/Mono.Addins
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.9.0
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q
%ifarch %{x8664}
%patch0 -p1
%else
%patch1 -p1
%endif

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mautil
%if "%{pld_release}" == "ti"
%dir %{_prefix}/lib/mono/mono-addins
%{_prefix}/lib/mono/mono-addins/mautil.exe
%{_prefix}/lib/mono/mono-addins/Mono.Addins.CecilReflector.dll
%{_prefix}/lib/mono/gac/Mono.Addins
%{_prefix}/lib/mono/gac/Mono.Addins.Gui
%{_prefix}/lib/mono/gac/Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Setup
%{_prefix}/lib/mono/gac/Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/policy.0.3.Mono.Addins.Setup
%else
%dir %{_libdir}/mono/mono-addins
%{_libdir}/mono/mono-addins/mautil.exe
%{_libdir}/mono/mono-addins/Mono.Addins.CecilReflector.dll
%{_libdir}/mono/gac/Mono.Addins
%{_libdir}/mono/gac/Mono.Addins.Gui
%{_libdir}/mono/gac/Mono.Addins.Setup
%{_libdir}/mono/gac/policy.0.2.Mono.Addins
%{_libdir}/mono/gac/policy.0.2.Mono.Addins.Gui
%{_libdir}/mono/gac/policy.0.2.Mono.Addins.Setup
%{_libdir}/mono/gac/Mono.Addins.CecilReflector
%{_libdir}/mono/gac/policy.0.2.Mono.Addins.CecilReflector
%{_libdir}/mono/gac/policy.0.3.Mono.Addins.Gui
%{_libdir}/mono/gac/policy.0.3.Mono.Addins
%{_libdir}/mono/gac/policy.0.3.Mono.Addins.CecilReflector
%{_libdir}/mono/gac/policy.0.3.Mono.Addins.Setup
%endif
%{_mandir}/man1/mautil.1*

%files devel
%defattr(644,root,root,755)
%if "%{pld_release}" == "ti"
%{_prefix}/lib/mono/mono-addins/Mono.Addins.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Gui.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Setup.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.CecilReflector.dll
%else
%{_libdir}/mono/mono-addins/Mono.Addins.dll
%{_libdir}/mono/mono-addins/Mono.Addins.Gui.dll
%{_libdir}/mono/mono-addins/Mono.Addins.Setup.dll
%{_libdir}/mono/mono-addins/Mono.Addins.CecilReflector.dll
%endif
%{_pkgconfigdir}/mono-addins.pc
%{_pkgconfigdir}/mono-addins-gui.pc
%{_pkgconfigdir}/mono-addins-setup.pc
