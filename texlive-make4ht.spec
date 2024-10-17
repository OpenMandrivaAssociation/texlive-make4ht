Name:		texlive-make4ht
Version:	62953
Release:	2
Summary:	A build system for tex4ht
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/make4ht
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/make4ht.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/make4ht.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
make4ht is a simple build system for tex4ht, a TeX to XML
converter. It provides a command line tool that drives the
conversion process. It also provides a library which can be
used to create customized conversion tools.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/make4ht
%doc %{_texmfdistdir}/texmf-dist/doc/support/make4ht

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
