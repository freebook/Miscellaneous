
yum -y install createrepo
mkdir -p pub/{5,6}/{i386,x86_64}
createrepo -p -d -o pub/6/i386 pub/centos/6/i386
