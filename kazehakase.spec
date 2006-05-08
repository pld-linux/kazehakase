# TODO: add subpackage for libs
#
# Conditional build:
%bcond_without	firefox		# build upon mozilla 1.7 libs instead of firefox
#
Summary:	A browser with gecko engine
Summary(pl):	Przegl±darka na silniku gecko
Name:		kazehakase
Version:	0.3.7
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://prdownloads.sourceforge.jp/kazehakase/20010/%{name}-%{version}.tar.gz
# Source0-md5:	3379ac7977d5bc34b024cdadbf37857e
Patch0:		%{name}-desktop.patch
URL:		http://kazehakase.sourceforge.jp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
%{?without_firefox:BuildRequires:	mozilla-devel >= 5:1.7}
%{?with_firefox:BuildRequires:	mozilla-firefox-devel >= 1.5.0.2}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kazehakase is a browser with gecko engine like Epiphany or Galeon.

%description -l pl
Kazehakase jest przegl±dark± na silniku gecko podobnie do Epiphany lub
Galeona.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.ja AUTHORS ChangeLog COPYING.README TODO.ja
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man?/*
