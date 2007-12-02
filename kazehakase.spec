# 
#
Summary:	A browser with gecko engine
Summary(pl.UTF-8):	Przeglądarka na silniku gecko
Name:		kazehakase
Version:	0.5.0
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.jp/kazehakase/27774/%{name}-%{version}.tar.gz
# Source0-md5:	27cb87e89a76a104630bf5838852d80b
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-agent.patch
Patch2:		%{name}-deprecated.patch
URL:		http://kazehakase.sourceforge.jp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xulrunner-devel
Requires:	%{name}-libs = %{version}-%{release}
%requires_eq_to	xulrunner xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# we have strict deps for it
%define		_noautoreq	libxpcom.so

%description
Kazehakase is a browser with gecko engine like Epiphany or Galeon.

%description -l pl.UTF-8
Kazehakase jest przeglądarką na silniku gecko podobnie do Epiphany lub
Galeona.

%package libs
Summary:	Kazehakase libraries
Summary(pl.UTF-8):	Biblioteki Kazehakase
Group:		Libraries

%description libs
This package contains Kazehakase libraries.

%description libs -l pl.UTF-8
Pakiet zawiera biblioteki Kazehakase.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	libkazehakasedir=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

# unnecessary
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/embed/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.ja AUTHORS ChangeLog COPYING.README TODO.ja
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man?/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/embed
%attr(755,root,root) %{_libdir}/%{name}/embed/*.so
