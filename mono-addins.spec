#
# Conditional build:
%bcond_without	monodoc	# monodoc documentation
%bcond_with	tests	# "make test" call [fails on UnitTests load???]
#
%include	/usr/lib/rpm/macros.mono
Summary:	Mono.Addins - framework for creating extensible applications and libraries
Summary(pl.UTF-8):	Mono.Addins - framework do tworzenia elastycznych aplikacji i bibliotek
Name:		mono-addins
Version:	1.0
Release:	1
License:	MIT
Group:		Development/Tools
# latest is 0.6.2 here
#Source0:	http://download.mono-project.com/sources/mono-addins/%{name}-%{version}.tar.bz2
# newer releases available on http://monoaddins.codeplex.com/ (requiring JS and POST forms) or github
Source0:	https://github.com/mono/mono-addins/archive/mono-addins-1.0.tar.gz
# Source0-md5:	d4c87fbfd46584a0f1fb56169e78f6d7
Patch0:		%{name}-monodir.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-destdir.patch
URL:		http://www.mono-project.com/Mono.Addins
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.9.0
BuildRequires:	mono-csharp >= 1.1.13
# mono-nunit
%{?with_tests:BuildRequires:	mono-devel}
%{?with_monodoc:BuildRequires:	mono-monodoc}
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
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	%{?with_monodoc:--enable-docs} \
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
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Gui.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.MSBuild.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Setup.dll
%if %{with monodoc}
%{_prefix}/lib/monodoc/sources/mono-addins-docs.*
%endif
%{_pkgconfigdir}/mono-addins.pc
%{_pkgconfigdir}/mono-addins-gui.pc
%{_pkgconfigdir}/mono-addins-msbuild.pc
%{_pkgconfigdir}/mono-addins-setup.pc
