%define	upstream_name	 Gnome2-Vte
%define	upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl binding for the vte widget
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Gnome2/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Glib => 1.00
BuildRequires:	perl-Gtk2
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-devel
BuildRequires:	vte-devel => 0.11.10
BuildRequires:	x11-server-xvfb
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Conflicts:	drakxtools < 9.1-15mdk
Requires:	perl-Glib >= 1.00

%description
This module provides perl access to vte libraries.

VTE is an experimental terminal emulator widget for use with GTK+ 2.:.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
# (tv) disabled b/c of "Xlib:  extension "RANDR" missing on display ":99.0"."
xvfb-run %make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc LICENSE 
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/Gnome2/*
