Summary:	A browser with gecko engine
Summary(pl):	Przegl±darka na silniku gecko
Name:		kazehakase
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.jp/kazehakase/12026/%{name}-%{version}.tar.gz
# Source0-md5:	c89f80966fc30b233a7cea92d22f7fa0
Patch0:		%{name}-mozilla_five_home.patch
Patch1:		%{name}-desktop.patch
URL:		http://kazehakase.sourceforge.jp/
BuildRequires:	autoconf
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
%patch1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README README.ja AUTHORS ChangeLog COPYING.README TODO.ja
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
