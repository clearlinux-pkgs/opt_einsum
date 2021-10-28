#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : opt_einsum
Version  : 3.2.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/11/ef/e0f8f7379f3d81040232c20c31289032af618df37717bce53d947e540e85/opt_einsum-3.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/ef/e0f8f7379f3d81040232c20c31289032af618df37717bce53d947e540e85/opt_einsum-3.2.1.tar.gz
Summary  : Optimizing numpys einsum function
Group    : Development/Tools
License  : MIT
Requires: opt_einsum-license = %{version}-%{release}
Requires: opt_einsum-python = %{version}-%{release}
Requires: opt_einsum-python3 = %{version}-%{release}
Requires: numpy
BuildRequires : buildreq-distutils3
BuildRequires : numpy

%description
[![Build Status](https://travis-ci.org/dgasmith/opt_einsum.svg?branch=master)](https://travis-ci.org/dgasmith/opt_einsum)
[![codecov](https://codecov.io/gh/dgasmith/opt_einsum/branch/master/graph/badge.svg)](https://codecov.io/gh/dgasmith/opt_einsum)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/opt_einsum/badges/version.svg)](https://anaconda.org/conda-forge/opt_einsum)
[![PyPI](https://img.shields.io/pypi/v/opt_einsum.svg)](https://pypi.org/project/opt-einsum/#description)
[![PyPIStats](https://img.shields.io/pypi/dm/opt_einsum)](https://pypistats.org/packages/opt-einsum)
[![Documentation Status](https://readthedocs.org/projects/optimized-einsum/badge/?version=latest)](http://optimized-einsum.readthedocs.io/en/latest/?badge=latest)
[![DOI](http://joss.theoj.org/papers/10.21105/joss.00753/status.svg)](https://doi.org/10.21105/joss.00753)

%package license
Summary: license components for the opt_einsum package.
Group: Default

%description license
license components for the opt_einsum package.


%package python
Summary: python components for the opt_einsum package.
Group: Default
Requires: opt_einsum-python3 = %{version}-%{release}

%description python
python components for the opt_einsum package.


%package python3
Summary: python3 components for the opt_einsum package.
Group: Default
Requires: python3-core
Provides: pypi(opt_einsum)
Requires: pypi(numpy)

%description python3
python3 components for the opt_einsum package.


%prep
%setup -q -n opt_einsum-3.2.1
cd %{_builddir}/opt_einsum-3.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587001837
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/opt_einsum
cp %{_builddir}/opt_einsum-3.2.1/LICENSE %{buildroot}/usr/share/package-licenses/opt_einsum/a2545d1b3d4d2470b78d1563425520cb7bf34dea
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/opt_einsum/a2545d1b3d4d2470b78d1563425520cb7bf34dea

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
