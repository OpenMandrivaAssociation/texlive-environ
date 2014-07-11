# revision 33821
# category Package
# catalog-ctan /macros/latex/contrib/environ
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-environ
Version:	0.3
Release:	8
Summary:	A new interface for environments in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/environ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the \collect@body command (as in amsmath),
as well as a \long version \Collect@Body, for collecting the
body text of an environment. These commands are used to define
a new author interface to creating new environments. For
example: \NewEnviron{test} wraps the entire environment body in
square brackets, doing the right thing in ignoring leading and
trailing spaces.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/environ/environ.sty
%doc %{_texmfdistdir}/doc/latex/environ/README
%doc %{_texmfdistdir}/doc/latex/environ/environ.pdf
#- source
%doc %{_texmfdistdir}/source/latex/environ/environ.dtx
%doc %{_texmfdistdir}/source/latex/environ/environ.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
