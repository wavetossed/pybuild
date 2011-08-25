Portable Python build script for Linux
======================================

This is a build script that will build a portable Python distro for either 321 bit or 64 bit
Linux distros. This Python is portable which means that it can be copied to any directory
on any Linux install (that is not too much older than your build machine) and it will all work.

This Python distro contains Python 2.7.2 and the standard library as well as a bunch of other
modules that I find useful. Many of the modules have binary shared libraries as part of them
and the main challenge of building is to arrange things so that all binary shared library
dependencies are included in the Python distro and are used in place of any similar
system libraries. This means that you can use the lxml module even on a Linux install
that does not have libxml installed.

Building binary modules is a real adventure and if you look through the script you 
will see many divergences from the simple ./configure;make;sudo make install that
are the ideal way to do a build. Hopefully you will be able to use these as
examples to add your own binary modules to the script.

Pure Python modules are a non-issue. Once you have the portable Python distro
built (and PATH variable set) then just run pip install mymodule and then remake the tarball.
In fact, many binary modules can be built by pip as long as you first set some environment
variables and then do the binary fixups afterward.

RPATH
-----

The portable magic is all done by using the RUNPATH and RPATH headers in the Python
binary and in all of the shared libraries. If you have tried using RPATH before and
written it off as too complex, then have a look at the technique that I used because
it manages the complexity. First of all, the magic name of $ORIGIN that is used in
RUNPATH headers to direct the dynamic linking process, is a bad design choice and
causes lots of issues in building code. My solution is to use XORIGIN instead, and
then patch it back to $ORIGIN after the binary libraries have been built. To do the
patching I use a utility called patchelf that is part of a very interesting Linux
distro called Nixos.

The build process has only been tested on Ubuntu and Debian installs, and the easiest
way to try it out is to install a fresh VM of Ubuntu Lucid (using VirtualBox) and then
check out pybuild and run it. It should just work and will pull in (via apt-get)
any OS dependencies needed. If you have local mirrors for Ubuntu or PyPi then you can
set a couple of variables in pybuild.sh and it will keep your traffic off the Internet.
I have also run the build on Debian Etch.

