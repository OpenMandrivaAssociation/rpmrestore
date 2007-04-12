Name:           rpmrestore
Version:        1.2
Release:        %mkrel 1
Epoch:          0
Summary:        Restores install attributes from the RPM database
Group:          System/Configuration/Packaging
License:        GPL
URL:            http://rpmrestore.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/rpmrestore/rpmrestore-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The rpm database stores the user, group, time, mode for all files,
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
%{__mv} %{buildroot}%{_bindir}/{rpmrestore.pl,rpmrestore}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc rpmrestore.lsm Authors COPYING Changelog NEWS Todo Readme
%attr(0755,root,root) %{_bindir}/rpmrestore
%{_mandir}/man1/rpmrestore.1*


