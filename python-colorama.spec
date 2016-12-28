#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	colorama
Summary:	Cross-platform colored terminal text
Name:		python-%{module}
Version:	0.3.1
Release:	7
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/c/colorama/%{module}-%{version}.tar.gz
# Source0-md5:	95ce8bf32f5c25adea14b809db3509cb
URL:		https://pypi.python.org/pypi/colorama
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI
sequences it finds (which otherwise show up as gobbledygook in your
output), and converting them into the appropriate win32 calls to
modify the state of the terminal. On other platforms, Colorama does
nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor (http://pypi.python.org/pypi/termcolor.)

This has the upshot of providing a simple cross-platform API for
printing colored terminal text from Python, and has the happy
side-effect that existing applications or libraries which use ANSI
sequences to produce colored output on Linux or Macs can now also
work on Windows, simply by calling colorama.init().

%package -n python3-%{module}
Summary:	Cross-platform colored terminal text
Group:		Libraries/Python

%description -n python3-%{module}
ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI
sequences it finds (which otherwise show up as gobbledygook in your
output), and converting them into the appropriate win32 calls to
modify the state of the terminal. On other platforms, Colorama does
nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor (http://pypi.python.org/pypi/termcolor.)

This has the upshot of providing a simple cross-platform API for
printing colored terminal text from Python, and has the happy
side-effect that existing applications or libraries which use ANSI
sequences to produce colored output on Linux or Macs can now also
work on Windows, simply by calling colorama.init().

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a demos/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*python\b|#!%{__python3}|'
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.txt
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
