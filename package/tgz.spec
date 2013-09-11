Summary: Netkiller's eBook
Name: netkiller
Version: 1.0.1
Release: 1
License: CC
Group: Books/Computer books
Packager: Neo Chen <netkiller@msn.com>
Source: %{name}-%{version}.tar.gz
URL: http://netkiller.github.io

%description

http://netkiller.github.io
http://netkiller.sourceforge.net

- Network: Firewall, Router, Switch, Cisco, H3C, Juniper,F5 Big-IP, Array
- Security: OpenVPN, L2TP, PPTP, IPSec IP Tunnel
- Cluster: SmartDNS, LVS, HAproxy, Keepalived, Heartbeat, MooseFS, GlusterFS
- Web: Apache, Lighttpd, Nginx, Tomcat, Resin
- Database: PostgreSQL, MySQL Cluster, MySQL Replication, Cassandra, MongoDB
- Cache: APC Cache, XCache, Memcached, Squid, Varnish
- Frameworks: PHP(CodeIgniter, Prado, Mach II, Qcodo, Smarty)
- Python(Django, Pylons) Perl(Catalyst)
- Search Engine: Solr, Sphinx, Crawler: Nutch
- DIV-CSS, JQuery, Prototype, Google Map API
- Virtualization: Xen, Kvm, OpenVZ

%prep

%setup


%build

mkdir -p %{_buildrootdir}/%{name}-%{version}-%{release}.x86_64/usr/share/doc/netkiller

%install

rsync -auzv %{_builddir}/%{name}-%{version}/* %{_buildrootdir}/%{name}-%{version}-%{release}.x86_64/usr/share/doc/netkiller



%pre

%preun

%post

%postun

%files
/usr/share/doc


%changelog
