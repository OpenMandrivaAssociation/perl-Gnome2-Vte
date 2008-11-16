%define	module	Gnome2-Vte
%define	fmodule	Gnome2/Vte

Name:		perl-%module
Version:	0.09
Release:	%mkrel 1
Summary:	Perl binding for the vte widget
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Gnome2/%{module}-%{version}.tar.gz
BuildRequires:	vte-devel => 0.11.10
BuildRequires:	perl-Glib => 1.00
BuildRequires:	perl-Gtk2
BuildRequires:	XFree86-Xvfb
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
Requires:	perl-Glib >= 1.00
Conflicts:	drakxtools < 9.1-15mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides perl access to vte libraries.

VTE is an experimental terminal emulator widget for use with GTK+ 2.:.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
XDISPLAY=$(i=2; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
Xvfb :$XDISPLAY & xvfb_pid=$!
DISPLAY=:$XDISPLAY %make test
kill $xvfb_pid ||:

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc LICENSE 
%{_mandir}/*/*
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule


