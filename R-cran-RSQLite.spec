%define		fversion	%(echo %{version} |tr r -)
%define		modulename	RSQLite
Summary:	SQLite interface for R
Name:		R-cran-%{modulename}
Version:	0.11.2
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	102fbed07dc322e664dba13a5d694eb6
BuildRequires:	R >= 2.8.1
BuildRequires:	R-cran-DBI
BuildRequires:	sqlite3-devel
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-bibtex
BuildRequires:	texlive-xetex
%requires_ge	sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Database Interface R driver for SQLite.
This package embeds the SQLite database engine in R and provides an
interface compliant with the DBI package.  The source for the
SQLite engine (version 3.7.14) is included.

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
