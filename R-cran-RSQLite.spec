%define		fversion	%(echo %{version} |tr r -)
%define		modulename	RSQLite
Summary:	SQLite interface for R
Name:		R-cran-%{modulename}
Version:	2.4.6
Release:	1
License:	LGPL v2.1+
Group:		Applications/Databases
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	1ed7fa10036f3409bac90dd1019d1f53
BuildRequires:	R >= 3.1.0
BuildRequires:	R-cran-bit64
BuildRequires:	R-cran-blob >= 1.2.0
BuildRequires:	R-cran-DBI >= 1.2.0
BuildRequires:	R-cran-memoise
BuildRequires:	R-cran-pkgconfig
BuildRequires:	R-cran-rlang
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-bibtex
BuildRequires:	texlive-xetex
Requires:	R-cran-bit64
Requires:	R-cran-blob >= 1.2.0
Requires:	R-cran-DBI >= 1.2.0
Requires:	R-cran-memoise
Requires:	R-cran-pkgconfig
Requires:	R-cran-rlang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Embeds the SQLite database engine in R and provides an interface
compliant with the DBI package. The source for the SQLite engine
(version 3.51.2) and for various extensions is included. System
libraries will never be consulted because this package relies on
static linking for the plugins it includes.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
