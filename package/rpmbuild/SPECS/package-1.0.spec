Summary: Netkiller‘s eBook
Name: netkiller
Version: 1.1.0
Release: centos
License: CC
# group you want your package in, mostly for GUI package browsers
# some example groups used by vendors:
# http://www.rpmfind.net/linux/RPM/Groups.html
Group: Books/Computer books
# your name for example
Packager: Neo Chen <netkiller@msn.com>
#
#Source: http://netkiller.github.com/package/%{name}-%{version}.tar.gz
Source: %{name}-%{version}-%{release}.tar.gz
# list all your patches here:
#Patch:
# list all packages required to build this package
#BuildRequires:
#Provides:
# list all packages that conflict with this one:
#BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}


####
# full length description
%description

http://netkiller.sourceforge.net
http://netkiller.github.com

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

#####
# this prepares a fresh build directory in ~/build/BUILD, useful macros here
# are:
# %setup - cleans any previous builds and untargzips the source
# %patch - applies patches
# any other commands here are executed as standard sh commands
%prep
#if [ ! -f ../SOURCES/%{name}-%{version}-%{release}.tar.gz ]; then
rsync -auzv --exclude=.git --exclude=.svn /home/neo/public_html/%{book} %{name}-%{version}-%{release}
tar -zcvf ../SOURCES/%{name}-%{version}-%{release}.tar.gz %{name}-%{version}-%{release}
#fi

#%setup
#%patch


#####
# this tells rpmbuild how to build your package, rpmbuild runs it as a sh
# script
%build
#make

#####
# all the steps necessary to install your package into $RPM_BUILD_ROOT
# first step is to clear $RPM_BUILD_ROOT
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/
#cp -r ../* %{_tmppath}
#install all files under RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
# now you can remove uneeded stuff
#rm -f $RPM_BUILD_ROOT{_prefix}
rsync -auzv ../BUILD/* $RPM_BUILD_ROOT/usr/share/doc/
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
#/usr/bin/test
#/usr/sbin/test
# this will package the dir and all directories inside it
#/example/of/a/dir
/
# this will package only the 'dir' directory
#%dir /example/of/a/dir
#%dir /$RPM_BUILD_ROOT

#####
# document changes between package releases
%changelog
