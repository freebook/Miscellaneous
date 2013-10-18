#!/bin/bash
for project in $(ls -1 ..)
do 

    cd ../$project
    pwd
    git pull
    cd -
done 
