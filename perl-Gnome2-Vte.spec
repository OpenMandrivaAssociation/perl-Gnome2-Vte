%define	upstream_name	 Gnome2-Vte
%define	upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	8

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
#xvfb-run %make test

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


%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.90.0-7
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-4
+ Revision: 702775
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.90.0-3
+ Revision: 667184
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 564480
- rebuild for perl 5.12.1

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 556671
- disable testsuite b/c of "Xlib:  extension "RANDR" missing on display ":99.0"."

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 408413
- rebuild using %%perl_convert_version

* Wed Jun 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.09-4mdv2010.0
+ Revision: 384702
- rebuild for new vte

* Tue Jun 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.09-3mdv2010.0
+ Revision: 382209
- rebuild for new libvte

* Sun Dec 14 2008 Christiaan Welvaart <spturtle@mandriva.org> 0.09-2mdv2009.1
+ Revision: 314125
- BuildRequires: x11-server-xvfb instead of XFree86-Xvfb, we do not need all of X11
- use xvfb-run

* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 303774
- new version

* Wed Sep 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.08-5mdv2009.0
+ Revision: 287782
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - reenable tests

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.08-3mdv2008.1
+ Revision: 152212
- temporary disable tests
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 0.08-2mdv2008.0
+ Revision: 44612
- rebuild


* Thu Nov 30 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.08-1mdv2007.0
+ Revision: 89425
- new release

* Wed Oct 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.07-1mdv2007.1
+ Revision: 65977
- new release
- Import perl-Gnome2-Vte

* Wed Jul 26 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.06-1mdv2007.0
- new release

* Thu Jul 13 2006 Pixel <pixel@mandriva.com> 0.05-4mdv2007.0
- add patch dropping test ->get_has_selection (which should return false, why?)
- fix using Xvfb for test
- kill Xvfb after use
- move test in %%check

* Sun Jul 09 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.05-3
- rebuild for libvte 9 on x86_64

* Sat Jul 08 2006 Pixel <pixel@mandriva.com> 0.05-2mdv2007.0
- rebuild for libvte 9

* Tue Jan 31 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.05-1mdk
- new release

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-4mdk
- Revert previous Buildrequires

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-3mdk
- Fix BuildRequires
- use mkrel

* Mon Nov 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.04-2mdk
- rebuild for new perl

* Tue Aug 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-1mdk
- new release
- fix build

* Mon Jun 07 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.03-1mdk
- new release
- fix build

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.02-2mdk
- fix build when there's no xdisplay available
- use %%make macro
- spec cosmetics

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-1mdk
- initial release

