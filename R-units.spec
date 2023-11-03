#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-units
Version  : 0.8.4
Release  : 49
URL      : https://cran.r-project.org/src/contrib/units_0.8-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/units_0.8-4.tar.gz
Summary  : Measurement Units for R Vectors
Group    : Development/Tools
License  : GPL-2.0
Requires: R-units-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
BuildRequires : expat-dev
BuildRequires : udunits-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-units package.
Group: Libraries

%description lib
lib components for the R-units package.


%prep
%setup -q -n units
pushd ..
cp -a units buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694709272

%install
export SOURCE_DATE_EPOCH=1694709272
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/units/CITATION
/usr/lib64/R/library/units/DESCRIPTION
/usr/lib64/R/library/units/INDEX
/usr/lib64/R/library/units/Meta/Rd.rds
/usr/lib64/R/library/units/Meta/demo.rds
/usr/lib64/R/library/units/Meta/features.rds
/usr/lib64/R/library/units/Meta/hsearch.rds
/usr/lib64/R/library/units/Meta/links.rds
/usr/lib64/R/library/units/Meta/nsInfo.rds
/usr/lib64/R/library/units/Meta/package.rds
/usr/lib64/R/library/units/Meta/vignette.rds
/usr/lib64/R/library/units/NAMESPACE
/usr/lib64/R/library/units/NEWS.md
/usr/lib64/R/library/units/R/units
/usr/lib64/R/library/units/R/units.rdb
/usr/lib64/R/library/units/R/units.rdx
/usr/lib64/R/library/units/demo/cf.R
/usr/lib64/R/library/units/demo/ggplot2.R
/usr/lib64/R/library/units/demo/year.R
/usr/lib64/R/library/units/doc/index.html
/usr/lib64/R/library/units/doc/measurement_units_in_R.R
/usr/lib64/R/library/units/doc/measurement_units_in_R.Rmd
/usr/lib64/R/library/units/doc/measurement_units_in_R.html
/usr/lib64/R/library/units/doc/units.R
/usr/lib64/R/library/units/doc/units.Rmd
/usr/lib64/R/library/units/doc/units.html
/usr/lib64/R/library/units/help/AnIndex
/usr/lib64/R/library/units/help/aliases.rds
/usr/lib64/R/library/units/help/paths.rds
/usr/lib64/R/library/units/help/units.rdb
/usr/lib64/R/library/units/help/units.rdx
/usr/lib64/R/library/units/html/00Index.html
/usr/lib64/R/library/units/html/R.css
/usr/lib64/R/library/units/share/udunits/udunits2-accepted.xml
/usr/lib64/R/library/units/share/udunits/udunits2-base.xml
/usr/lib64/R/library/units/share/udunits/udunits2-common.xml
/usr/lib64/R/library/units/share/udunits/udunits2-derived.xml
/usr/lib64/R/library/units/share/udunits/udunits2-prefixes.xml
/usr/lib64/R/library/units/share/udunits/udunits2.xml
/usr/lib64/R/library/units/tests/testthat.R
/usr/lib64/R/library/units/tests/testthat/_snaps/misc.md
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/ggplot2-automatic.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/ggplot2-default.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/ggplot2-lab.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/ggplot2-manual.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/ggplot2-nolab.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/ggplot2-trans-unit.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/ggplot2-transformed.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-boxplot.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-default.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-degree-c.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-division.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-hist.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-inverse.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-lab.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-line.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-nothing.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-npower.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/plot/plot-parentheses.svg
/usr/lib64/R/library/units/tests/testthat/_snaps/tidyverse.md
/usr/lib64/R/library/units/tests/testthat/test_arith.R
/usr/lib64/R/library/units/tests/testthat/test_conversion.R
/usr/lib64/R/library/units/tests/testthat/test_helpers.R
/usr/lib64/R/library/units/tests/testthat/test_math.R
/usr/lib64/R/library/units/tests/testthat/test_misc.R
/usr/lib64/R/library/units/tests/testthat/test_mixed.R
/usr/lib64/R/library/units/tests/testthat/test_plot.R
/usr/lib64/R/library/units/tests/testthat/test_summaries.R
/usr/lib64/R/library/units/tests/testthat/test_symbolic_units.R
/usr/lib64/R/library/units/tests/testthat/test_tidyverse.R
/usr/lib64/R/library/units/tests/testthat/test_time.R
/usr/lib64/R/library/units/tests/testthat/test_unit_creation.R
/usr/lib64/R/library/units/tests/testthat/test_user_conversion.R
/usr/lib64/R/library/units/tests/testthat/test_valid_udunits.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/units/libs/units.so
/usr/lib64/R/library/units/libs/units.so.avx2
/usr/lib64/R/library/units/libs/units.so.avx512
