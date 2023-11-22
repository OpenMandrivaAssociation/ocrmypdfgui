Summary:	Hobby Project GUI for the Python Program OCRmyPDF by James R. Barlow
Name:		ocrmypdfgui
Version:	0.9.15
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/ocrmypdfgui/ocrmypdfgui-%{version}.tar.gz
URL:		https://pypi.org/project/ocrmypdfgui/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Hobby Project GUI for the Python Program 'OCRmyPDF' by James R. Barlow

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/%{name}
%{py_sitedir}/ocrmypdfgui
%{py_sitedir}/ocrmypdfgui-*.*-info
