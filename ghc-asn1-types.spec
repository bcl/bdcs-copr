# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name asn1-types
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.3.2
Release:        1%{?dist}
Summary:        ASN.1 types

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-hourglass-devel
BuildRequires:  ghc-memory-devel
# End cabal-rpm deps

%description
ASN.1 standard types.


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


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files


%changelog
* Wed Jul 26 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.3.2-1
- spec file generated by cabal-rpm-0.11.1
