Name:           raidix
Version:        1.0
Release:        1%{?dist}
Summary:        Simple output program

License:        GPLv3+
URL:            https://github.com/dakopecky/raidix-rpm
Source0:        %{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc 

%description
The simple program that prints "Test Task in RAIDIX!" to stdout

%prep
%autosetup


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Mon Nov 14 2022 Daniel Kopecky <danielkopecky@proton.me> - 1.0
- First raidix package
