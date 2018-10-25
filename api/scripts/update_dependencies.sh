#!/bin/bash
set -e

update_packages(){
    packages=$(pip list --outdated --local --format=freeze | \
        grep -v '^\-e' | cut -d = -f 1  )

    for package in $(echo $packages);
    do
        pip install -U $package;
    done;
};

update_requirements(){
    temp_file=$(mktemp)
    requirements_file=${1:=requirements.txt}
    echo Update $requirements_file
    for i in $(cat $requirements_file);
    do
        package_name=$(echo $i | cut -d= -f1)
        pip freeze --local | egrep ^${package_name} | grep ${package_name}= >> $temp_file;
    done;
    cp $temp_file $requirements_file;
};

echo Update packages
update_packages

echo Run unit tests
make test

update_requirements requirements.txt
