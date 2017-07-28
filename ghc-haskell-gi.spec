# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name haskell-gi
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.20.2
Release:        1%{?dist}
Summary:        Generate Haskell bindings for GObject Introspection capable libraries

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  chrpath
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskell-gi-base-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-xdg-basedir-devel
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if %{with tests}
BuildRequires:  ghc-doctest-devel
%endif
# End cabal-rpm deps

%description
Generate Haskell bindings for GObject Introspection capable libraries.
This includes most notably Gtk+, but many other libraries in the GObject
ecosystem provide introspection data too.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gobject-2.0)
Requires:       pkgconfig(gobject-introspection-1.0)
# End cabal-rpm deps

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install
%ghc_fix_rpath %{pkgver}


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc ChangeLog.md DocTests.hs
%{_bindir}/%{pkg_name}


%changelog
* Tue Jul 25 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.20.2-1
- spec file generated by cabal-rpm-0.11.1