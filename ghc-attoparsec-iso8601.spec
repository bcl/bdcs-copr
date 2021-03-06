# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name attoparsec-iso8601
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.0.0.0
Release:        1%{?dist}
Summary:        Parsing of ISO 8601 dates, originally from aeson

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
# End cabal-rpm deps

%description
Parsing of ISO 8601 dates, originally from aeson.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc README.md


%changelog
* Tue Jul 25 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.0.0.0-1
- spec file generated by cabal-rpm-0.11.1
