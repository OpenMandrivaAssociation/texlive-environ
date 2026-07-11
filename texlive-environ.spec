%global tl_name environ
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	A new interface for environments in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/environ
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/environ.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(trimspaces)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the \collect@body command (as in amsmath), as well
as a \long version \Collect@Body, for collecting the body text of an
environment. These commands are used to define a new author interface to
creating new environments. For example, \NewEnviron{test}, wraps the
entire environment body in square brackets, doing the right thing in
ignoring leading and trailing spaces.

