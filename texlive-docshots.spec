%global tl_name docshots
%global tl_revision 69676

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4.3
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
Requires:	texlive(pdfcrop)
Requires:	texlive(pgf)
Requires:	texlive(pgf-blur)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package helps you show TeX code next to the corresponding PDF
snapshots, in two-column formatting. You can use it either in .dtx
documentation or in .tex files.

