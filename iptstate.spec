Summary:	IP Tables State - like top
Summary(pl.UTF-8):	Stan Tablic IP - wyświetlający jak top
Name:		iptstate
Version:	2.2.6
Release:	1
License:	Zlib
Group:		Networking/Utilities
#Source0Download: https://github.com/jaymzh/iptstate/releases
Source0:	https://github.com/jaymzh/iptstate/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ec96c93b43976960d2e2ba3306cd09e6
URL:		https://www.phildev.net/iptstate/
BuildRequires:	libnetfilter_conntrack-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IP Tables State (iptstate) was originally written to implement the
"state top" feature of IP Filter in IP Tables. "State top" displays
the states held by your stateful firewall in a top-like manner.

%description -l pl.UTF-8
Stan Tablic IP (iptstate) oryginalnie został napisany, by
zaimplementować możliwość ,,state top'' filtra pakietów IP. ,,state
top'' wyświetla stany pamiętane przez Twój stateful firewall w sposób
podobny do topa.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti -Wall" \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses" \
	LIBS="%{rpmldflags} -lncurses -ltinfo -lnetfilter_conntrack"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	SBIN=$RPM_BUILD_ROOT%{_sbindir} \
	MAN=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CONTRIB Changelog LICENSE README.md WISHLIST
%attr(755,root,root) %{_sbindir}/iptstate
%{_mandir}/man8/iptstate.8*
