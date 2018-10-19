#!/bin/bash
set -e

update_packages(){
    packages=$(pip list --outdated --format=freeze | \
        grep -v '^\-e' | cut -d = -f 1  )

    for package in $(echo $packages);
    do
        pip install -U $package;
    done;
}

update_requirements(){
    temp_file=$(mktemp)
    requirements_file=${1:=requirements.txt}
    echo Update $requirements_file
    for i in $(cat $requirements_file);
    do
        pip freeze | egrep ^$(echo $i | cut -d= -f1) >> $temp_file;
    done;
    cp $temp_file $requirements_file;
};

echo Update packages
update_packages

echo Pass unit tests
bash scripts/unit_tests.sh

update_requirements requirements.txt
