Summary:	A browser with gecko engine
Summary(pl):	Przegl±darka na silniku gecko
Name:		kazehakase
Version:	0.1.6
Release:	2
URL:		http://kazehakase.sourceforge.jp
Source0:	http://dl.sourceforge.jp/kazehakase/9697/%{name}-%{version}.tar.gz
# Source0-md5:	7b2d64f688909eaf3ef57a3d2df5fffd
Patch0:		%{name}-c++.patch
License:	GPL
Group:		X11/Applications/Networking
BuildRequires:	mozilla-devel >= 1.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kazehakase is a browser with gecko engine like Epiphany or Galeon.

%description -l pl
Kazehakase jest przegl±dark± na silniku gecko podobnie do Epiphany lub
Galeona.

%prep
%setup -q
%patch -p0

%build
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
