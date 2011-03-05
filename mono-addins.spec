%include	/usr/lib/rpm/macros.mono
Summary:	Mono.Addins - framework for creating extensible applications and libraries
Summary(pl.UTF-8):	Mono.Addins - framework do tworzenia elastycznych aplikacji i bibliotek
Name:		mono-addins
Version:	0.6
Release:	1
License:	MIT
Group:		Development/Tools
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/mono-addins/%{name}-%{version}.tar.bz2
# Source0-md5:	d6a1fd2b233c3f1c69b6dd32f8f0e7a4
Patch0:		%{name}-monodir.patch
URL:		http://www.mono-project.com/Mono.Addins
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.9.0
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
%patch0 -p1

%build
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
%dir %{_prefix}/lib/mono/mono-addins
%{_prefix}/lib/mono/mono-addins/mautil.exe
%{_prefix}/lib/mono/gac/Mono.Addins
%{_prefix}/lib/mono/gac/Mono.Addins.CecilReflector
%{_prefix}/lib/mono/gac/Mono.Addins.Gui
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
%{_mandir}/man1/mautil.1*

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/mono-addins/Mono.Addins.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.CecilReflector.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Gui.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.MSBuild.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Setup.dll
%{_prefix}/lib/mono/xbuild/Mono.Addins.targets
%{_pkgconfigdir}/mono-addins.pc
%{_pkgconfigdir}/mono-addins-gui.pc
%{_pkgconfigdir}/mono-addins-msbuild.pc
%{_pkgconfigdir}/mono-addins-setup.pc
