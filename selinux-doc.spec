Summary:	SELinux documentation
Summary(pl):	Dokumentacja do SELinuksa
Name:		selinux-doc
Version:	1.16
Release:	1
License:	Public Use License v1.0
Group:		Documentation
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	fd1a22082420592619c4756d4fdc9ca3
URL:		http://www.nsa.gov/selinux/
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
BuildRequires:	rpmbuild(macros) >= 1.144
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains build instructions, porting information, and a
CREDITS file for SELinux. Some of these files will be split up into
per-package files in the future, and other documentation will be added
to this package (e.g. an updated form of the Configuring the SELinux
Policy report).

%description -l pl
Security-enhanced Linux jest prototypem j±dra Linuksa i wielu
aplikacji u¿ytkowych o funkcjach podwy¿szonego bezpieczeñstwa.
Zaprojektowany jest tak, aby w prosty sposób ukazaæ znaczenie
obowi±zkowej kontroli dostêpu dla spo³eczno¶ci linuksowej. Ukazuje
równie¿ jak tak± kontrolê mo¿na dodaæ do istniej±cego systemu typu
Linux. J±dro SELinux zawiera nowe sk³adniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeñstwa systemu operacyjnego
Flask. Te elementy zapewniaj± ogólne wsparcie we wdra¿aniu wielu typów
polityk obowi±zkowej kontroli dostêpu, w³±czaj±c te wzorowane na: Type
Enforcement (TE), kontroli dostêpu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

Ten pakiet zawiera instrukcje budowania, informacje o portowaniu oraz
plik CREDITS dla SELinuksa. Czê¶æ z tych plików w przysz³o¶ci bêdzie
rozrzucona po pakietach, a dodana zostanie nowa dokumentacja (np.
uaktualniona postaæ raportu o konfigurowaniu polityki SELinuksa).

%prep
%setup -q

%build
%{__make} -C module main.pdf main
%{__make} -C policy main.pdf main

%install
rm -rf $RPM_BUILD_ROOT

rm -rf module/module policy/policy

cp -f module/main.pdf module.pdf 
cp -f policy/main.pdf policy.pdf
cp -a module/main module/module
ln -s t1.html module/module/index.html
cp -a policy/main policy/policy
ln -s t1.html policy/policy/index.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog LICENSE PORTING README README.MLS README.CONDITIONAL module.pdf policy.pdf
%doc module/module policy/policy
