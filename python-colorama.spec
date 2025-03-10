#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		colorama
Summary:	Cross-platform colored terminal text
Summary(pl.UTF-8):	Wieloplatformowe kolorowanie tekstu na terminalu
Name:		python-%{module}
Version:	0.4.5
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/colorama/
Source0:	https://files.pythonhosted.org/packages/source/c/colorama/%{module}-%{version}.tar.gz
# Source0-md5:	6abed05fb23a857a3ab22576148e7a4c
URL:		https://github.com/tartley/colorama
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	sed >= 4.0
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI
sequences it finds (which otherwise show up as gobbledygook in your
output), and converting them into the appropriate Win32 calls to
modify the state of the terminal. On other platforms, Colorama does
nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor (<https://pypi.org/project/termcolor/>).

This has the upshot of providing a simple cross-platform API for
printing colored terminal text from Python, and has the happy
side-effect that existing applications or libraries which use ANSI
sequences to produce colored output on Linux or Macs can now also work
on Windows, simply by calling colorama.init().

%description -l pl.UTF-8
Do wyświetlania kolorowego tekstu na terminalu oraz przesuwania
kursora w systemach Unix i Mac od dawna używane są sekwencje ANSI.
Colorama sprawia, że działa to także pod Windows - poprzez
przechwycenie stdout, wycinanie znalezionych sekwencji ANSI (które w
przeciwnym wypadku wyświetliłyby się jako bełkot) i przekształcanie
ich na odpowiednie wywołania Win32, modyfikujące stan terminala. Na
innych platformach Colorama nie robi nic.

Colorama zapewnia też pewne ułatwienia do generowania sekwencji ANSI,
ale działa dobrze w połączeniu z dowolną inną biblioteką generującą
sekwencje ANSI, taką jak Termcolor
(<https://pypi.org/project/termcolor/>).

Efektem jest zapewnienie prostego, wieloplatformowego API do
wypisywania kolorowego tekstu z Pythona, co ma miły efekt uboczny, że
istniejące aplikacje czy biblioteki wykorzystujące sekwencje ANSI do
tworzenia kolorowego wyjścia pod systemem Linux czy Mac będą teraz
działać także pod Windows dzięki prostemu wywołaniu colorama.init().

%package -n python3-%{module}
Summary:	Cross-platform colored terminal text
Summary(pl.UTF-8):	Wieloplatformowe kolorowanie tekstu na terminalu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

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
library, such as Termcolor (<https://pypi.org/project/termcolor/>).

This has the upshot of providing a simple cross-platform API for
printing colored terminal text from Python, and has the happy
side-effect that existing applications or libraries which use ANSI
sequences to produce colored output on Linux or Macs can now also work
on Windows, simply by calling colorama.init().

%description -n python3-%{module} -l pl.UTF-8
Do wyświetlania kolorowego tekstu na terminalu oraz przesuwania
kursora w systemach Unix i Mac od dawna używane są sekwencje ANSI.
Colorama sprawia, że działa to także pod Windows - poprzez
przechwycenie stdout, wycinanie znalezionych sekwencji ANSI (które w
przeciwnym wypadku wyświetliłyby się jako bełkot) i przekształcanie
ich na odpowiednie wywołania Win32, modyfikujące stan terminala. Na
innych platformach Colorama nie robi nic.

Colorama zapewnia też pewne ułatwienia do generowania sekwencji ANSI,
ale działa dobrze w połączeniu z dowolną inną biblioteką generującą
sekwencje ANSI, taką jak Termcolor
(<https://pypi.org/project/termcolor/>).

Efektem jest zapewnienie prostego, wieloplatformowego API do
wypisywania kolorowego tekstu z Pythona, co ma miły efekt uboczny, że
istniejące aplikacje czy biblioteki wykorzystujące sekwencje ANSI do
tworzenia kolorowego wyjścia pod systemem Linux czy Mac będą teraz
działać także pod Windows dzięki prostemu wywołaniu colorama.init().

%prep
%setup -q -n %{module}-%{version}

%{__sed} -i -e '1s,/usr/bin/env bash,/bin/sh,' demos/demo.sh

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos/*.{py,sh} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__sed} -i -e '1s,/usr/bin/python,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.py
%{__sed} -i -e 's,^python ,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/demo.sh
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a demos/*.{py,sh} $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__sed} -i -e '1s,/usr/bin/python,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}/*.py
%{__sed} -i -e 's,^python ,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}/demo.sh
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.txt README.rst
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
