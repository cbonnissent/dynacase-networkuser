#! /bin/rpm
#
#  File: 
#  $Id: FREEDOM-AD.spec,v 1.1 2007/01/31 17:48:24 eric Exp $
#
#  This is the SPEC file for the What Users Module
#  Anakeen What Application
#

%define cerbere         %(rpm -q --queryformat '%{VENDOR}' rpm |grep -q 'none' && echo 1 || echo 0)
%define pld		%(rpm -q --queryformat '%{VENDOR}' rpm |grep -q 'PLD' && echo 1 || echo 0)
%define redhat	        %(rpm -q --queryformat '%{VENDOR}' rpm | grep -q 'Red Hat, Inc.' && echo 1 || echo 0)

%{?ncerbere:%define cerbere 1}
%{?ncerbere:%define redhat 0}
%{?ncerbere:%define pld 0}
%{?nredhat:%define cerbere 0}
%{?nredhat:%define redhat 1}
%{?nredhat:%define pld 0}
%{?npld:%define cerbere 0}
%{?npld:%define redhat 0}
%{?npld:%define pld 1}

%if %{cerbere}
%define destdir /home/httpd/what
%define httpuser http
%define releasepostfix %(echo)
%endif
%if %{pld}
%define destdir /usr/share/what
%define httpuser http
%define releasepostfix cb
%endif
%if %{redhat}
%define destdir /usr/share/what
%define httpuser apache
%define releasepostfix fc%(cat /etc/fedora-release | sed -e 's/.* release \\([[:digit:]]\\+\\) .*/\\1/')
%endif

%{?ndestdir:%define destdir %{ndestdir}}
%{?nhttpuser:%define httpuser %{nhttpuser}}
%{?rpost:%define releasepostfix %{rpost}}

%define dirname AD
Summary: Active directory functions to authenticate with Windows
Name: FREEDOM-AD
Version: 0.0.0
Release: 0%{releasepostfix}
License: GPL
Group: Applications/Web
Source: ftp://ftp.souillac.anakeen.com/pub/anakeen/%{name}-%{version}.tar.gz
Vendor: Anakeen           
URL: http://www.anakeen.com/
Packager: Yannick Le Briquer <yannick.lebriquer@anakeen.com>
BuildArchitectures: noarch
BuildRoot: /tmp/anakeen-root
Prereq: gettext


%description
Active Directory functions to be use with a Microsoft Windows authentification


%prep
%setup -q -n %{name}-%{version}

%build

%install
autoconf
./configure --with-pubrule=`pwd` \
	     --with-httpuser=%{httpuser} \
	     --prefix=%{destdir}
make  pubdir=$RPM_BUILD_ROOT%{destdir} 
install -d $RPM_BUILD_ROOT/%{destdir}/FDL
cd $RPM_BUILD_ROOT/%{destdir}/FDL
ln -s ../%{dirname}/Method.*.php  .

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post





%preun
%postun



%files
%defattr(-,%{httpuser},%{httpuser})
%dir %{destdir}/%{dirname}
%{destdir}/%{dirname}/*
%{destdir}/FDL/*
%{destdir}/ad.php
#%{destdir}/locale/*



%changelog
* Fri Apr 30 2004 Yannick Le Briquer <yannick.lebriquer@anakeen.com>
- Build first RPM

