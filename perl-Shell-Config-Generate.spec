#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Shell
%define		pnam	Config-Generate
Summary:	Shell::Config::Generate - portably generate config for any shell
Summary(pl.UTF-8):	Shell::Config::Generate - przenośne generowanie konfiguracji dla dowolnej powłoki
Name:		perl-Shell-Config-Generate
Version:	0.34
Release:	2
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Shell/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1068869e6ae124abdd7a20b5c901ccb8
URL:		https://metacpan.org/release/Shell-Config-Generate
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Test2::API) >= 1.302015
BuildRequires:	perl-Shell-Guess >= 0.02
BuildRequires:	perl-Test2-Suite >= 0.000060
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface for specifying shell configurations
for different shell environments without having to worry about the
arcane differences between shells such as csh, sh, cmd.exe and
command.com.

It does not modify the current environment, but it can be used to
create shell configurations which do modify the environment.

%description -l pl.UTF-8
Ten moduł udostępnia interfejs do opisywania konfiguracji powłoki dla
środowisk różnych powłok bez przejmowania się różnicami między
powłokami, takimi jak csh, sh, cmd.exe czy command.com.

Moduł nie modyfikuje bieżącego środowiska, ale może być użyty do
tworzenia konfiguracji powłok modyfikujących środowiko.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p example/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Shell/Config
%{perl_vendorlib}/Shell/Config/Generate.pm
%{_mandir}/man3/Shell::Config::Generate.3pm*
%{_examplesdir}/%{name}-%{version}
