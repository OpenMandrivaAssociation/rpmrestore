Name:           rpmrestore
Version:        1.3
Release:        6
Epoch:          0
Summary:        Restores install attributes from the RPM database
Group:          System/Configuration/Packaging
License:        GPL
URL:            https://rpmrestore.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/rpmrestore/rpmrestore-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The RPM database stores the user, group, time, mode for all files,
and offers a command to display the changes between install state (database)
and current disk state. rpmrestore will help you to restore these install
attributes.

%prep
%setup -q

%build
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%{__mv} %{buildroot}%{_bindir}/{rpmrestore.pl,rpmrestore}
%{__perl} -pi -e 's/^rpmrestore\.pl/rpmrestore/g' %{buildroot}%{_bindir}/rpmrestore %{buildroot}%{_mandir}/man1/rpmrestore.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc rpmrestore.lsm Authors COPYING Changelog NEWS Todo Readme
%attr(0755,root,root) %{_bindir}/rpmrestore
%{_mandir}/man1/rpmrestore.1*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:1.3-5mdv2010.0
+ Revision: 433455
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.3-4mdv2009.0
+ Revision: 260335
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.3-3mdv2009.0
+ Revision: 251499
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 16 2007 David Walluck <walluck@mandriva.org> 0:1.3-1mdv2008.1
+ Revision: 109030
- 1.3

* Thu Aug 16 2007 David Walluck <walluck@mandriva.org> 0:1.2-2mdv2008.0
+ Revision: 64096
- remove duplicate docs
- reflect the name that we install as


* Tue Mar 20 2007 David Walluck <walluck@mandriva.org> 1.2-1mdv2007.1
+ Revision: 147050
- 1.2

* Tue Jan 09 2007 David Walluck <walluck@mandriva.org> 0:1.1-1mdv2007.1
+ Revision: 106265
- 1.1

* Fri Dec 08 2006 David Walluck <walluck@mandriva.org> 0:1.0-1mdv2007.1
+ Revision: 92215
- 1.0

* Thu Nov 16 2006 David Walluck <walluck@mandriva.org> 0:0.9-1mdv2007.1
+ Revision: 84678
- 0.9

* Thu Nov 09 2006 David Walluck <walluck@mandriva.org> 0:0.8-1mdv2007.0
+ Revision: 79896
- 0.8
- 0.3

* Sun Oct 15 2006 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2006.0
+ Revision: 64946
- Import rpmrestore

* Wed Oct 11 2006 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2007.1
- release

