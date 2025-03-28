%define		module		colorama
Summary:	Cross-platform colored terminal text
Summary(pl.UTF-8):	Wieloplatformowe kolorowanie tekstu na terminalu
Name:		python3-%{module}
Version:	0.4.6
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/colorama/
Source0:	https://files.pythonhosted.org/packages/source/c/colorama/%{module}-%{version}.tar.gz
# Source0-md5:	11fe1cbf8299798551ac88f824ea11c4
URL:		https://github.com/tartley/colorama
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-build
BuildRequires:	python3-installer
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

%prep
%setup -q -n %{module}-%{version}

%{__sed} -i -e '1s,/usr/bin/env bash,/bin/sh,' demos/demo.sh

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a demos/*.{py,sh} $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__sed} -i -e '1s,/usr/bin/python,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}/*.py
%{__sed} -i -e 's,^python ,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}/demo.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
%{_examplesdir}/python3-%{module}-%{version}
