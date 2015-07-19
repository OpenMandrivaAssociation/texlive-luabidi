# revision 30790
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-luabidi
Version:	20131014
Release:	9
Summary:	TeXLive luabidi package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabidi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luabidi.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive luabidi package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/luabidi/arabmaths.tex
%{_texmfdistdir}/tex/lualatex/luabidi/autofootnoterule.tex
%{_texmfdistdir}/tex/lualatex/luabidi/luabidi.sty
%{_texmfdistdir}/tex/lualatex/luabidi/textwidthfootnoterule.tex
%doc %{_texmfdistdir}/doc/lualatex/luabidi/README
%doc %{_texmfdistdir}/doc/lualatex/luabidi/test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
