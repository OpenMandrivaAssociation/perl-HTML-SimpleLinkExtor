%define upstream_name    HTML-SimpleLinkExtor
%define upstream_version 1.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A simple way to extract links
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTML::LinkExtor)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::Output)
BuildRequires: perl(URI)
BuildRequires: perl(URI::file)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a simple HTML link extractor designed for the person who does not
want to deal with the intricacies of 'HTML::Parser' or the de-referencing
needed to get links out of 'HTML::LinkExtor'.

You can extract all the links or some of the links (based on the HTML tag
name or attribute name). If a <BASE HREF> tag is found, all of the relative
URLs will be resolved according to that reference.

This module is simply a subclass around 'HTML::LinkExtor', so it can only
parse what that module can handle. Invalid HTML or XHTML may cause
problems.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/linktractor
/usr/share/man/man1/linktractor.1.lzma

