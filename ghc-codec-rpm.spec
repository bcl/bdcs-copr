# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name codec-rpm
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.1.3
Release:        1%{?dist}
Summary:        A library for manipulating RPM files

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-attoparsec-binary-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-combinators-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hspec-attoparsec-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
This module provides a library for reading RPM files and converting them into
useful data structures. There is currently no way to operate in reverse - that
is, for building an RPM file out of a data structure.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md examples


%changelog
* Mon Aug 28 2017 David Shea <dshea@redhat.com> - 0.1.3-1
- New version 0.1.3: Derive Ord for DepRequirement

* Tue Jul 25 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.2-1
- spec file generated by cabal-rpm-0.11.1
