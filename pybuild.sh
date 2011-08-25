#!/bin/bash

dist=`lsb_release -si`
if [ $dist = "Ubuntu" ] ; then # need pattern matching to check cpu bitsize
	shopt -s compat40
fi

export TARG=/data1/packages/python272

# this line uses an Ubuntu or Debian mirror (or a proxy like http-replicator)
#export WEBPROXY=http://192.168.12.175:8080

# the following use a PyPi mirror (or proxy server like collective.eggproxy)
#export PIPPROXY=http://192.168.12.175:8888
#export PIP_INDEX_URL=$PIPPROXY

export WGET=echo
#uncomment the following if you are running for the first time
export WGET=wget

cd `dirname $0`
export RUNDIR=`pwd` # get the absolute path of the script directory
run_scripts()
{
echo "+++++++++++++++++++++"
echo $1/*
echo "+++++++++++++++++++++"
    for script in $RUNDIR/$1/*; do

        # skip non-executable snippets
        [ -x "$script" ] || echo $script not executable || continue

        # execute $script in the context of the current shell
	echo "========" Executing $script
	date
        . $script
    done
}

echo $RUNDIR
cd ~  # we really want to use ~ as the home directory for running the scripts
run_scripts pybuild.d

# note that many of the scripts in pybuild.d are a bit misleading. They appear
# to install a set of specific extension modules, but in fact, they may
# be installing many other modules that are dependencies. Don't take the
# filenames too seriously. They are somewhat grouped, but only loosely

