%define	snap	20131204
Summary:	A optimized pool miner for primecoin
Name:		jhprimeminer
Version:	0.1
Release:	0.%{snap}.1
License:	GPL v2
Group:		Applications/Networking
URL:		https://github.com/tandyuk/jhPrimeminer.git
Source0:	jhPrimeminer-%{snap}.tar.bz2
# Source0-md5:	8e0aa5224499aec73f339fabe1179dfe
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	openssl-devel
BuildRequires:	gmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A optimized pool miner for primecoin.

%prep
%setup -q -n jhPrimeminer

%build
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install -m755 jhprimeminer $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md *.conf
%attr(755,root,root) %{_bindir}/%{name}
