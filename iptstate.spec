Summary:	IP Tables State - like top
Summary(pl.UTF-8):	Stan Tablic IP - wyświetlający jak top
Name:		iptstate
Version:	2.2.2
Release:	1
License:	zlib/libpng license
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/iptstate/%{name}-%{version}.tar.bz2
# Source0-md5:	b3f2e89ef38d6e8a85c8ab88a9c514d8
URL:		http://phildev.net/iptstate/
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
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CONTRIB Changelog LICENSE README WISHLIST
%attr(755,root,root) %{_sbindir}/iptstate
%{_mandir}/man8/iptstate.8*
