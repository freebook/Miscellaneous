PATH=$PATH:/Applications/calibre.app/Contents/MacOS
#ebook-convert netkiller.epub netkiller.mobi 
DOWNLOAD=~/git/netkiller.github.io/download/
EPUB=${DOWNLOAD}/epub

cd ${DOWNLOAD}

for book in $(find ${EPUB} -type f -name "*.epub" -exec basename -s .epub {} \;)
do

ebook-convert epub/${book}.epub mobi/${book}.mobi
ebook-convert epub/${book}.epub pdf/${book}.pdf

done