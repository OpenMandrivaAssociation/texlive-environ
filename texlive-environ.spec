Name:		texlive-environ
Version:	56615
Release:	1
Summary:	A new interface for environments in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/environ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
