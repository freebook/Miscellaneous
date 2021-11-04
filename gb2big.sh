#!/bin/bash
SOURCE_DIR="/home/neo/workspace/netkiller.github.io"
TARGET_DIR="/home/neo/workspace/netkiller.sourceforge.net"

mkdir -p $TARGET_DIR

#echo "find $SOURCE_DIR -type d | egrep -v '(zh-tw|.svn|.git)'"
    for dir in $(find $SOURCE_DIR -type d | egrep -v '(zh-tw|.svn|/.git)' | sed -e "s:^$SOURCE_DIR/::g"); 
    do
        mkdir -p $TARGET_DIR/$dir
    done

    for file in $(find $SOURCE_DIR -type f | egrep -v '(zh-tw|.svn|/.git)' )
    do
 	output_file=$(echo $file | sed -e "s:^$SOURCE_DIR:$TARGET_DIR:g") # -e "s:^/::g")
        if [ "${file##*.}" = "html" ]
        then 
            	cconv -f UTF8-CN -t UTF8-HK $file -o $output_file &
        else
        
        	cp $file $output_file &
        fi
	echo $file
    done 

