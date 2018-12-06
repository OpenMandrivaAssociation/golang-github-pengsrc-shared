# Run tests in check section
%bcond_without check

%global goipath         github.com/pengsrc/go-shared
%global commit          1ef04317652833067e47e2ee9815f1f254a7a1da

%global common_description %{expand:
Useful packages for the Go programming language.}

%gometa

Name:           %{goname}
Version:        0.2.0
Release:        3%{?dist}
Summary:        Useful packages for the Go programming language
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Jeffail/gabs)

%if %{with check}
BuildRequires:  golang(github.com/stretchr/testify)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Jul 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-3.20180718git1ef0431
- Bump to commit 1ef04317652833067e47e2ee9815f1f254a7a1da

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Bump to 0.2.0

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- First package for Fedora

