%bcond_with bootstrap
%global packname  lmtest
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9_29
Release:          2
Summary:          Testing Linear Regression Models
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-29.tar.gz
Requires:         R-stats R-zoo 
Requires:         R-stats R-graphics 
%if %{with bootstrap}
Requires:         R-car R-survival
%else
Requires:         R-car R-strucchange R-sandwich R-dynlm R-survival R-AER 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-zoo
BuildRequires:    R-stats R-graphics 
%if %{with bootstrap}
BuildRequires:    R-car R-survival
%else
BuildRequires:    R-car R-strucchange R-sandwich R-dynlm R-survival R-AER 
%endif
%rename R-cran-lmtest

%description
A collection of tests, data sets, and examples for diagnostic checking in
linear regression models. Furthermore, some generic tools for inference in
parametric models are provided.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/help
