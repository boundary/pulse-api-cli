#/bin/bash
#
# Installs a Python 2.7 on centos operating systems without disturbing 2.6 whichimpacts yum
# Receipe comes from the following:
# https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4
#

function DetectPackageManager() {

  VERSION=$(cat /proc/version)  > /dev/null
  echo $VERSION | grep -i ubuntu > /dev/null

  if [ $? -eq 0 ]
  then
    package_manager=apt
  fi

  echo $VERSION | grep -i centos > /dev/null
  if [ $? -eq 0 ]
  then
    package_manager=rpm
  fi

  echo $package_manager
}

function UpdatePackages() {

    case $(DetectPackageManager) in
    apt) sudo apt-get update -y 
       ;;
    rpm) sudo rpm update -y 
       ;;
    esac
}

function InstallPackage() {
    typeset -r package_name=$1

    case $(DetectPackageManager) in
    apt) sudo apt-get install -y $package_name
       ;;
    rpm) sudo rpm install -y $package_name
       ;;
    *) echo "Unknown package manager, exiting" >&2
       exit 1
       ;;
    esac
}

typeset -r PACKAGE_MANAGER=$(DetectPackageManager)
set -x

#sudo yum update -y
UpdatePackages

#sudo yum install -y epel-release
if $PACKAGE_MANAGER == 'rpm'
then
    sudo yum groupinstall -y development
fi

if $PACKAGE_MANAGER == 'apt'
then
   InstallPackage gcc 
fi


#sudo yum install -y zlib-dev openssl-devel sqlite-devel bzip2-devel wget xz-libs
InstallPackage zlib-dev
InstallPackage openssl-devel
InstallPackage sqlite-devel
InstallPackage bzip2-devel
InstallPackage wget
InstallPackage xz-libs

PYTHON_VERSION=2.7.9

wget http://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz


# Let's decode (-d) the XZ encoded tar archive:
xz -d Python-$PYTHON_VERSION.tar.xz


# Now we can perform the extraction:
tar -xvf Python-$PYTHON_VERSION.tar

# Enter the file directory:
pushd Python-$PYTHON_VERSION

# Start the configuration (setting the installation directory)
# By default files are installed in /usr/local.
# You can modify the --prefix to modify it (e.g. for $HOME).
./configure --prefix=/usr/local    


# Let's build (compile) the source
# This procedure can take awhile (~a few minutes)
make

# After building everything:
sudo make altinstall

popd


# Example: export PATH="[/path/to/installation]:$PATH"
export PATH="/usr/local/bin:$PATH"


# Let's download the installation file using wget:
wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz

# Extract the files from the archive:
tar -xvf setuptools-1.4.2.tar.gz

# Enter the extracted directory:
pushd setuptools-1.4.2

# Install setuptools using the Python we've installed (2.7.9)
sudo /usr/bin/local/bin/python2.7 setup.py install

popd

wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py

sudo /usr/local/bin/python2.7 get-pip.py

sudo /usr/local/bin/python2.7 /usr/local/bin/pip install virtualenv

echo 'export PATH="/usr/local/bin:$PATH"' >> /home/vagrant/.bash_profile

