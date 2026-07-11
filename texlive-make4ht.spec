%global tl_name make4ht
%global tl_revision 78133

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4e
Release:	%{tl_revision}.1
Summary:	A build system for tex4ht
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/make4ht
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/make4ht.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/make4ht.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(make4ht.bin)
Requires:	tex4ht
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
make4ht is a simple build system for tex4ht, a TeX to XML converter. It
provides a command line tool that drives the conversion process. It also
provides a library which can be used to create customized conversion
tools.

