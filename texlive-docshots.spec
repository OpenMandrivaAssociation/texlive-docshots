%global tl_name docshots
%global tl_revision 79688

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.0
Release:	%{tl_revision}.1
Summary:	TeX samples next to their PDF snapshots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/docshots
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docshots.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docshots.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docshots.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fancyvrb)
Requires:	texlive(iexec)
Requires:	texlive(lineno)
Requires:	texlive(listings)
Requires:	texlive(minted)
Requires:	texlive(pdfcrop)
Requires:	texlive(pdftexcmds)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package helps you render TeX examples from your DTX documentation
and then embed PDF snapshots into it, next to the source TeX code.

