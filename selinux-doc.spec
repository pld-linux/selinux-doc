Summary:	SELinux documentation
Summary(pl):	Dokumentacja do SELinuksa
Name:		selinux-doc
Version:	1.10
Release:	1
License:	Public Use License v1.0
Group:		Documentation
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	b9d20eaf4e387185b35f4f517a16f828
URL:		http://www.nsa.gov/selinux/
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
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
CREDITS file for SELinux.  Some of these files will be split up into
per-package files in the future, and other documentation will be added
to this package (e.g. an updated form of the Configuring the SELinux
Policy report).

%description -l pl
Security-enhanced Linux jest prototypem j�dra Linuksa i wielu
aplikacji u�ytkowych o funkcjach podwy�szonego bezpiecze�stwa.
Zaprojektowany jest tak, aby w prosty spos�b ukaza� znaczenie
obowi�zkowej kontroli dost�pu dla spo�eczno�ci Linuksowej. Ukazuje
r�wnie� jak tak� kontrol� mo�na doda� do istniej�cego systemu typu
Linux. J�dro SELinux zawiera nowe sk�adniki architektury pierwotnie
opracowane w celu ulepszenia bezpiecze�stwa systemu operacyjnego
Flask. Te elementy zapewniaj� og�lne wsparcie we wdra�aniu wielu typ�w
polityk obowi�zkowej kontroli dost�pu, w��czaj�c te wzorowane na: Type
Enforcement (TE), kontroli dost�pu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

Ten pakiet zawiera instrukcje budowania, informacje o portowaniu oraz
plik CREDITS dla SELinuksa. Cz�� z tych plik�w w przysz�o�ci b�dzie
rozrzucona po pakietach, a dodana zostanie nowa dokumentacja (np.
uaktualniona posta� raportu o konfigurowaniu polityki SELinuksa).

%prep
%setup -q

%build
%{__make} -C module main.pdf
%{__make} -C policy main.pdf

%install
rm -rf $RPM_BUILD_ROOT
# must stay for rpm.macros < 1.144
install -d $RPM_BUILD_ROOT

mv -f module/main.pdf module.pdf
mv -f policy/main.pdf policy.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog LICENSE PORTING README README.MLS README.CONDITIONAL module.pdf policy.pdf