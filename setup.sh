
ln -s /opt/workspace/netkiller.github.com /home/neo/public_html
ln -s /opt/workspace /home/neo/workspace

sudo apt-get install -y make cconv xsltproc docbook-xsl docbook-website

sudo apt-get install -y rpm
echo "%_topdir ~/rpmbuild" >> ~/.rpmmacros
echo "%packager Neo Chen <netkiller@msn.com>" >> ~/.rpmmacros
echo "%_gpg_name Neo Chen (http://www.netkiller.cn) <netkiller@msn.com>" >> ~/.rpmmacros
cat ~/.rpmmacros

gpg --gen-key
gpg --list-keys
