Name:		texlive-environ
Version:	0.2
Release:	1
Summary:	A new interface for environments in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/environ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the \collect@body command (as in amsmath),
as well as a \long version \Collect@Body, for collecting the
body text of an environment. These commands are used to define
a new author interface to creating new environments. For
example: \NewEnviron{test} wraps the entire environment body in
square brackets, doing the right thing in ignoring leading and
trailing spaces.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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