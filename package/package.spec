%define public_html ~/public_html
#define book docbook
#%define version 1.0.1
Summary: Netkiller %{book} Cookbook 
Name: netkiller-%{book}
Version: 1.0.1
Release: 1
License: CC
# group you want your package in, mostly for GUI package browsers
# some example groups used by vendors:
# http://www.rpmfind.net/linux/RPM/Groups.html
Group: Books/Computer books
Packager: Neo Chen <netkiller@msn.com>
#Source: http://netkiller.github.com/package/%{name}-%{version}.tar.gz
Source: %{name}-%{version}.tar.gz
URL: http://netkiller.github.io
# list all your patches here:
#Patch:
# list all packages required to build this package
#BuildRequires:
#Requires:
#Provides:
# list all packages that conflict with this one:
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

####
# full length description
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

Netkiller Architect 手札		http://netkiller.github.io/architect/index.html
Netkiller Developer 手札		http://netkiller.github.io/developer/index.html
Netkiller PHP 手札			http://netkiller.github.io/php/index.html
Netkiller Python 手札			http://netkiller.github.io/python/index.html
Netkiller Testing 手札		http://netkiller.github.io/testing/index.html
Netkiller Cryptography 手札	http://netkiller.github.io/cryptography/index.html
Netkiller Linux 手札			http://netkiller.github.io/linux/index.html
Netkiller Debian 手札			http://netkiller.github.io/debian/index.html
Netkiller CentOS 手札			http://netkiller.github.io/centos/index.html
Netkiller FreeBSD 手札		http://netkiller.github.io/freebsd/index.html
Netkiller Security 手札		http://netkiller.github.io/security/index.html
Netkiller Version 手札		http://netkiller.github.io/version/index.html
Netkiller Web 手札			http://netkiller.github.io/www/index.html
Netkiller Monitoring 手札		http://netkiller.github.io/monitoring/index.html
Netkiller Storage 手札		http://netkiller.github.io/storage/index.html
Netkiller Mail 手札			http://netkiller.github.io/mail/index.html
Netkiller Shell 手札			http://netkiller.github.io/shell/index.html
Netkiller Network 手札		http://netkiller.github.io/network/index.html
Netkiller Database 手札		http://netkiller.github.io/database/index.html
Netkiller PostgreSQL 手札		http://netkiller.github.io/postgresql/index.html
Netkiller MySQL 手札			http://netkiller.github.io/mysql/index.html
Netkiller NoSQL 手札			http://netkiller.github.io/nosql/index.html
Netkiller LDAP 手札			http://netkiller.github.io/ldap/index.html
Netkiller Cisco IOS 手札		http://netkiller.github.io/cisco/index.html
Netkiller H3C 手札			http://netkiller.github.io/h3c/index.html
Netkiller Multimedia 手札		http://netkiller.github.io/multimedia/index.html
Netkiller Docbook 手札		http://netkiller.github.io/docbook/index.html

#####
# this prepares a fresh build directory in ~/build/BUILD, useful macros here
# are:
# %setup - cleans any previous builds and untargzips the source
# %patch - applies patches
# any other commands here are executed as standard sh commands
%prep
if [ ! -f %{_sourcedir}/%{name}-%{version}.tar.gz ]; then
tar -zcf %{_sourcedir}/%{name}-%{version}.tar.gz ~/public_html/%{book}/*
#cd ${PUBLIC_HTML} && tar -zcvf %{_sourcedir}/%{name}-%{version}-%{release}.tar.gz * --exclude .git --exclude .svn --exclude download && cd -
fi
#mkdir -p %{name}-%{version}
mkdir -p %{_buildrootdir}/%{name}-%{version}-%{release}.x86_64/usr/share/doc/netkiller
rsync -az --exclude=.git --exclude=download ~/public_html/%{book}/* %{name}-%{version}

#%setup -T -n /tmp/ssss

#%patch

#####
# this tells rpmbuild how to build your package, rpmbuild runs it as a sh
# script
%build

#####
# all the steps necessary to install your package into $RPM_BUILD_ROOT
# first step is to clear $RPM_BUILD_ROOT
%install

rsync -az %{_builddir}/%{name}-%{version}/* %{_buildrootdir}/%{name}-%{version}-%{release}.x86_64/usr/share/doc/netkiller/%{book}
#rsync -auzv ${PUBLIC_HTML}/mail/* %{_buildrootdir}/%{name}-%{version}-%{release}.x86_64/usr/share/doc/


#####
# NOTE: this section is optional
# commands run just before the package is installed
%pre
#/usr/sbin/useradd -c "test user" -r -s /bin/false -u 666 -d / neo 2> /dev/null

#####
# NOTE: this section is optional
# commands run before uninstalling the software
%preun
#/sbin/service test stop > /dev/null 2>&1
#/sbin/chkconfig --del test

#####
# NOTE: this section is optional
# commands run after installing the package
%post
#/sbin/chkconfig -add test
#touch /var/log/test

#####
# NOTE: this section is optional
# commands run after unistalling the package
%postun
#/sbin/service test stop
#/usr/sbin/userdel test

#####
# list all the files that are part of the package. If a file is not in the
# list rpmbuild won't put it in the package
# see below on how to automate the process of creating this list.
# some useful macros here:
# %doc /path/to/filename - installs filename into /path/to/filename and marks
# it as being documentation
# %config /etc/config_file - similar for configuration files
# %attr(mode, user, group) file - lets you specify file attributes applied
# during installation, use - if you want to use defaults
%files
# this will package the dir and all directories inside it
#/example/of/a/dir
/usr/share/doc

# this will package only the 'dir' directory
#%dir /example/of/a/dir
#%dir /

#####
# document changes between package releases
%changelog