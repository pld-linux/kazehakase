Summary:	A browser with gecko engine
Summary(pl):	Przegl±darka na silniku gecko
Name:		kazehakase
Version:	0.1.9
Release:	6
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.jp/kazehakase/11115/%{name}-%{version}.tar.gz
# Source0-md5:	72a733327f0cdef740996b6f9efdfeba
Patch0:		%{name}-mozilla_five_home.patch
Patch1:		%{name}-mozilla-1.7.3.patch
Patch2:		%{name}-desktop.patch
URL:		http://kazehakase.sourceforge.jp/
BuildRequires:	automake
BuildRequires:	mozilla-devel >= 1.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kazehakase is a browser with gecko engine like Epiphany or Galeon.

%description -l pl
Kazehakase jest przegl±dark± na silniku gecko podobnie do Epiphany lub
Galeona.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.ja AUTHORS ChangeLog COPYING.README TODO.ja
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
