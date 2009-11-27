#
#   - force kazehakase to use old SSL dialogs using nsIBadCertListener, ie. port
#     EphyBadCertRejector from Epiphany, this will fix issues with https sites
#     using self signed and expired certificates or mismatches in domain names
#
# Conditional builds
%bcond_without	gecko	# build without gecko support
%bcond_without	webkit	# build without webkit support
#
Summary:	A browser with multiple rendering engines support
Summary(pl.UTF-8):	Przeglądarka obsługująca wiele silników renderujących
Name:		kazehakase
Version:	0.5.6
Release:	11
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.jp/kazehakase/33533/%{name}-%{version}.tar.gz
# Source0-md5:	b88257aa10dd53fd5d39c627f8f95890
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-deprecated.patch
Patch2:		%{name}-ti-agent.patch
Patch3:		%{name}-agent.patch
Patch4:		%{name}-libxul.patch
Patch5:		%{name}-xulappinfo.patch
Patch6:		%{name}-gnutls.patch
Patch7:		%{name}-xulrunner-1_9_1.patch
URL:		http://kazehakase.sourceforge.jp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	gtk+2-devel
%{?with_webkit:BuildRequires:	gtk-webkit-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
%{?with_gecko:BuildRequires:	xulrunner-devel}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kazehakase_engine
%requires_eq_to	xulrunner xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# we have strict deps for it
%define		_noautoreq	libxpcom.so

%description
Kazehakase is a browser which allow use many rendering engines. For
now it support only Gecko (like Epiphany or Galeon) and webkit engines.

%description -l pl.UTF-8
Kazehakase jest przeglądarką, która pozwala na używanie wielu
silników renderujących. Na dzień dzisiejszy obsługuje silniki Gecko
(taki jak w Epiphany lub Galeonie) oraz webkit.

%package libs
Summary:	Kazehakase libraries
Summary(pl.UTF-8):	Biblioteki Kazehakase
Group:		Libraries

%description libs
This package contains Kazehakase libraries.

%description libs -l pl.UTF-8
Pakiet zawiera biblioteki Kazehakase.

%package plugin-gecko
Summary:	Gecko plugin engine for Kazehakase
Summary(pl.UTF-8):	Wtyczka Gecko dla Kazehakase
Group:		X11/Applications/Networking
Requires:	xulrunner
Provides:	kazehakase_engine

%description plugin-gecko
This plugin provides Gecko rendering engine support.

%description plugin-gecko -l pl.UTF-8
Ta wtyczka dodaje obsługę silnika renderującego Gecko.

%package plugin-webkit
Summary:	Webkit plugin engine for Kazehakase
Summary(pl.UTF-8):	Wtyczka webkit dla Kazehakase
Group:		X11/Applications/Networking
Provides:	kazehakase_engine

%description plugin-webkit
This plugin provides webkit rendering engine support.

%description plugin-webkit -l pl.UTF-8
Ta wtyczka dodaje obsługę silnika renderującego webkit.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if "%{pld_release}" == "ti"
%patch2 -p1
%else
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gecko:--disable-gecko} \
	%{!?with_webkit:--disable-webkit}

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
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/embed

%if %{with gecko}
%files plugin-gecko
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/embed/gecko.so
%endif
%if %{with webkit}
%files plugin-webkit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/embed/webkit_gtk.so
%endif
