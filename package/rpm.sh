#!/bin/sh

topdir=~/rpmbuild
#rm -rf $topdir
mkdir -p $topdir/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

#echo "%_topdir ~/rpmbuild" > ~/.rpmmacros
#echo "%_tmppath /tmp" > ~/.rpmmacros
#echo "%packager Neo Chen <netkiller@msn.com>" > ~/.rpmmacros
#cat ~/.rpmmacros

cat << EOF >> ~/.rpmmacros
%_signature gpg
%_gpg_name Neo Chen (netkiller) <netkiller@msn.com>
%_gpgpath ~/.gnupg
%_gpgbin /usr/bin/gpg
EOF

#rpm -Vp