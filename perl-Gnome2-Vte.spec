%define	module	Gnome2-Vte
%define	fmodule	Gnome2/Vte

Summary:	Perl binding for the vte widget
Name:		perl-%module
Version:	0.08
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	%module-%version.tar.bz2
URL:		http://gtk2-perl.sf.net/
BuildRequires:	vte-devel => 0.11.10, perl-Glib => 1.00, perl-Gtk2 XFree86-Xvfb
BuildRequires:	perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig
Requires:	perl-Glib >= 1.00
Conflicts:	drakxtools < 9.1-15mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Patch: Gnome2-Vte-0.05-drop-test--get_has_selection--which-should-return-false.patch

%description
This module provides perl access to vte libraries.

VTE is an experimental terminal emulator widget for use with GTK+ 2.:.

%prep
%setup -q -n %module-%version
#%patch0 -p1

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE 
%{_mandir}/*/*
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule


