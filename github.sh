#!/bin/bash
PUBLIC_HTML=~/public_html

init(){
    sudo apt-get install git
    git config --global user.name "Neo Chan"
    git config --global user.email netkiller@msn.com
    git init
    git remote add origin git@github.com:netkiller/netkiller.github.com.git
}

clone(){
    git clone git@github.com:netkiller/netkiller.github.com.git
}
sitemap(){
	gunzip sitemaps.xml.gz

	:%s/netkiller.sourceforge.net/netkiller.github.com/g

	gzip sitemaps.xml
}

./sitemaps http://www.netkiller.cn > ${PUBLIC_HTML}/sitemap.xml
cat ${PUBLIC_HTML}/sitemap.xml | gzip > ${PUBLIC_HTML}/sitemaps.xml.gz
./sitemap.txt > ${PUBLIC_HTML}/sitemap.txt

cd ${PUBLIC_HTML}

git add *

if [ -z $1 ]; then
	git commit --all
else
	git commit --all -m "$1"
fi

git push origin master
#git push origin gh-pages
cd -

./sourceforge

#echo "Sync..."
#rsync -azv ../netkiller.github.io/* www@www.netkiller.cn:/www/test
