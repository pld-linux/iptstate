Summary:	IP Tables State - like top
Summary(pl.UTF-8):	Stan Tablic IP - wyświetlający jak top
Name:		iptstate
Version:	1.3
Release:	1
License:	zlib/libpng license
Group:		Networking/Utilities
Source0:	http://iptstate.phildev.net/%{name}-%{version}.tar.gz
# Source0-md5:	0fc7ce5e6803b18c73dcaadb4be2edd0
Patch0:		%{name}-c++.patch
URL:		http://iptstate.phildev.net/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IP Tables State (iptstate) was originally written to implement the
"state top" feature of IP Filter in IP Tables. "State top" displays
the states held by your stateful firewall in a top-like manner.

%description -l pl.UTF-8
Stan Tablic IP (iptstate) oryginalnie został napisany by
zaimplementować możliwość ,,state top'' filtra pakietów IP. ,,state
top'' wyświetla stany pamiętane przez Twój stateful firewall w sposób
podobny do top-a.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CONTRIB README WISHLIST
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
