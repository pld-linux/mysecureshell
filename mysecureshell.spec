#
Summary:	MySecureShell is a shell which adds more features to sftp-server
Name:		mysecureshell
Version:	1.20
Release:	1
License:	GNU GPL v2
Group:		Applications
Source0:	http://mysecureshell.free.fr/repository/index.php/source/%{name}_%{version}.tar.gz
# Source0-md5:	e6720c036775745ff2d7db34e2ade17c
Patch0:		%{name}-needs-no-root.patch
URL:		http://mysecureshell.sourceforge.net
Requires:	openssh-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySecureShell is a shell which will help add more features to sftp-server 
which will bring major FTP servers like proftpd.

Possibilities of MySecureShell :
- Control bandwidth.
- Secure viewing rights.
- Administration of server by GUI.
- Management of the activity the server with logging.
- Control by user ip, groups ...

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build

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
%doc README* LICENSE  
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
/etc/ssh/sftp_config
/etc/logrotate.d/*
/bin/MySecureShell
