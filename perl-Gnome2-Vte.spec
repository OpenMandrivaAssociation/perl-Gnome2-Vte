%define	modname	Gnome2-Vte
%define modver 0.11

Summary:	Perl binding for the vte widget

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Gnome2/%{modname}-%{modver}.tar.gz
Source100: %{name}.rpmlintrc
BuildRequires:	perl-Glib => 1.00
BuildRequires:	perl-Gtk2
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(vte)
Requires:	perl-Glib >= 1.00

%description
This module provides perl access to vte libraries.

VTE is an experimental terminal emulator widget for use with GTK+ 2.:.

%prep
%autosetup -p1 -n %{modname}-%{modver}
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="%{optflags} -Os -s"
export GTK2_PERL_CFLAGS="%{optflags}"
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
# (tv) disabled b/c of "Xlib:	extension "RANDR" missing on display ":99.0"."
#xvfb-run %make test

%install
%make_install

%files
%doc LICENSE 
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/Gnome2/*
%doc %{_mandir}/man3/*


