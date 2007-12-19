
%include	/usr/lib/rpm/macros.mono
Summary:	Mono.Addins - framework for creating extensible applications and libraries
Summary(pl.UTF-8):	Mono.Addins - framework do tworzenia elastycznych aplikacji i bibliotek
Name:		mono-addins
Version:	0.3
Release:	0.5
License:	GPL/MIT
Group:		Development/Tools
#Source0Download: http://go-mono.com/sources-stable/
Source0:	http://go-mono.com/sources/mono-addins/%{name}-%{version}.tar.bz2
# Source0-md5:	4bc524df81dca65bca05271e89a96b90
URL:		http://www.mono-project.com/Mono.Addins
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:  dotnet-gtk-sharp2-devel >= 2.9.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
%{?with_asp:BuildRequires:	xsp}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mono.Addins has been designed to be easy to use and useful for a wide
range of applications: from simple applications with small
extensibility needs, to complex applications which need support for
large add-in structures. This new framework intends to set an standard
for building extensible applications and add-ins in Mono.

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

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

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
%{_prefix}/lib/mono/mono-addins
%{_prefix}/lib/mono/gac/Mono.Addins
%{_prefix}/lib/mono/gac/Mono.Addins.Gui
%{_prefix}/lib/mono/gac/Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Setup

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/mono-addins
%{_prefix}/lib/mono/gac/Mono.Addins
%{_prefix}/lib/mono/gac/Mono.Addins.Gui
%{_prefix}/lib/mono/gac/Mono.Addins.Setup
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Gui
%{_prefix}/lib/mono/gac/policy.0.2.Mono.Addins.Setup
%{_pkgconfigdir}/*
