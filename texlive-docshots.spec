Name:		texlive-docshots
Version:	69676
Release:	1
Summary:	TeX samples next to their PDF Snapshots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/docshots
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docshots.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docshots.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docshots.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package helps you show TeX code next to the
corresponding PDF snapshots, in two-column formatting. You can
use it either in .dtx documentation or in .tex files.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/docshots
%{_texmfdistdir}/tex/latex/docshots
%doc %{_texmfdistdir}/doc/latex/docshots

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
