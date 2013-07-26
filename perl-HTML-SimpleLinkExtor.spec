%define upstream_name    HTML-SimpleLinkExtor
%define upstream_version 1.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.25
Release:	1

Summary:	A simple way to extract links
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-SimpleLinkExtor-1.25.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::LinkExtor)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::file)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/linktractor


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.230.0-2mdv2011.0
+ Revision: 655223
- update file list
- rebuild for updated spec-helper

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-1mdv2011.0
+ Revision: 480883
- import perl-HTML-SimpleLinkExtor


* Mon Dec 21 2009 cpan2dist 1.23-1mdv
- initial mdv release, generated with cpan2dist

