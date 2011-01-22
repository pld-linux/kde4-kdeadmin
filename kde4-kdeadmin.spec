# TODO
#   %{_pkgconfigdir}/system-tools-backends.pc
%define		_state		stable
%define		orgname		kdeadmin
%define		qtver		4.7.1

%include	/usr/lib/rpm/macros.perl

Summary:	K Desktop Environment - administrative tools
Summary(es.UTF-8):	K Desktop Environment - herramientas administrativas
Summary(ko.UTF-8):	K 데스크탑 환경 - 괄1�7름1�7도구
Summary(pl.UTF-8):	K Desktop Environment - narzędzia administratora
Summary(pt_BR.UTF-8):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN.UTF-8):	KDE管理工具
Name:		kde4-kdeadmin
Version:	4.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	6b7102d8907c4cd44e172e8229f00ee9
Patch0:		%{name}-liloconfig.patch
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libpng-devel
BuildRequires:	pam-devel
BuildRequires:	python-PyKDE4 >= %{version}
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-pycups
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	system-config-printer
Requires:	shadow
Obsoletes:	%{name}-kcmlilo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE administrative tools. Package includes:
- KCron - KDE Task Scheduler (cron GUI),
- KDat - Tape backup tool,
- KNetworkConf - KControl module for TCP/IP settings configuration,
- KPackage - KDE support for package management,
- KSysV - SysV-style init configuration,
- KUser - KDE user setup tool,
- lilo-config - KControl plugin for LILO configuration (x86 only).

%description -l pl.UTF-8
Aplikacje administratorskie dla KDE. Pakiet zawiera:
- KCron - program do zlecania zadań (interfejs do crona),
- KDat - narzędzie do wykonywania kopii zapasowych na taśmie,
- KNetworkConf - moduł KControl do konfiguracji ustawień TCP/IP,
- KPackage - program do zarządzania pakietami,
- KSysV - program do konfiguracji startu systemu w stylu SysV,
- KUser - program do zarządzania kontami użytkowników,
- lilo-config - moduł KControl do konfiguracji LILO (tylko x86).

%package kcmlilo
Summary:	LILO Configurator
Summary(pl.UTF-8):	Konfigurator LILO
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Requires:	lilo
Obsoletes:	kdeadmin-kcmlinuz < 8:3.4.0

%description kcmlilo
LILO configuration module for KDE Control Centre.

%description kcmlilo -l pl.UTF-8
Konfigurator LILO dla Centrum Sterowania KDE.

%package kcron
Summary:	KDE Task Scheduler (cron GUI)
Summary(pl.UTF-8):	Program do zlecania zadań dla KDE (graficzny interfejs do crona)
Summary(pt_BR.UTF-8):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kcron
KCron is an application for scheduling programs to run in the
background. It is a graphical user interface to cron, the UNIX system
scheduler.

%description kcron -l pl.UTF-8
KCron to aplikacja do planowania uruchamiania programów w tle. Jest to
graficzny interfejs do crona - systemowego programu do planowego
uruchamiania programów w systemach uniksowych.

%description kcron -l pt_BR.UTF-8
Gerenciador/agendador de tarefas e interface para o cron.

%package kpackage
Summary:	Package management front-end KDE
Summary(pl.UTF-8):	Program do zarządzania pakietami
Summary(pt_BR.UTF-8):	Interface para gerenciamento de pacotes RPM/DEB
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Provides:	kpackage
Obsoletes:	kpackage

%description kpackage
KPackage is a GUI interface to the RPM, Debian, Slackware and BSD
package managers. KPackage is part of the K Desktop Environment and,
as a result, it is designed to integrate with the KDE file manager.

%description kpackage -l pl.UTF-8
KPackage to graficzny interfejs do zarządców pakietów RPM, Debiana,
Slackware'a i BSD. KPackage to część środowiska KDE, dzięki czemu
integruje się z zarządcą plików KDE.

%description kpackage -l pt_BR.UTF-8
Interface para gerenciamento de pacotes RPM/DEB.

%package kprinter
Summary:	Printer configuration for KDE
Summary(pl.UTF-8):	Konfigurator drukarek dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Requires:	poppler-progs
Requires:	system-config-printer

%description kprinter
Printer configuration for KDE.

%description kprinter -l pl.UTF-8
Konfigurator drukarek dla KDE.

%package ksystemlog
Summary:	System log viewer for KDE
Summary(pl.UTF-8):	Przeglądarka logów systemowych dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description ksystemlog
KSystemLog is a system log viewer for KDE.

%description ksystemlog -l pl.UTF-8
KSystemLog to przeglądarka logów systemowych dla KDE.

%package kuser
Summary:	KDE User management tool
Summary(pl.UTF-8):	Administracja kontami dla KDE
Summary(pt_BR.UTF-8):	Ferramenta para administração de usuários
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kuser
A simple tool for managin system groups and user accounts from system.

%description kuser -l pl.UTF-8
Narzędzie do dodawania/usuwania użytkowników oraz do zmiany danych o
nich.

%description kuser -l pt_BR.UTF-8
Ferramenta para administração de usuários do sistema.

%prep
%setup -q -n %{orgname}-%{version}
# consider it obsolete?
#%patch0 -p0

%build
install -d build
cd build
%cmake \
	-DINSTALL_SYSTEM_CONFIG_PRINTER=TRUE \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang kcron	--with-kde
#%find_lang kdat		--with-kde
#%find_lang kpackage	--with-kde
%find_lang kuser	--with-kde
%ifarch %{ix86} %{x8664}
#%find_lang lilo-config	--with-kde
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%ifarch %{ix86} %{x8664}
#%files kcmlilo -f lilo-config.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_lilo.so
#%{_datadir}/kde4/services/lilo.desktop
%endif

%files kcron -f kcron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_cron.so
%{_datadir}/kde4/services/kcm_cron.desktop
#%{_kdedocdir}/en/kcron

#%files kpackage -f kpackage.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kpackage
##%attr(755,root,root) %{_libdir}/kde4/kfile*.so
#%{_datadir}/apps/kpackage
##%{_datadir}/services/kfile*
#%{_desktopdir}/kde4/kpackage.desktop
#%{_iconsdir}/*/*/*/kpackage.png
#%{_datadir}/config.kcfg/kpackageSettings.kcfg

%files kprinter
%defattr(644,root,root,755)
%dir %{_datadir}/apps/system-config-printer-kde
%{_datadir}/apps/system-config-printer-kde/new-printer.ui
%{_datadir}/apps/system-config-printer-kde/system-config-printer-kde.py
%{_datadir}/apps/system-config-printer-kde/system-config-printer.ui
%{_datadir}/apps/system-config-printer-kde/ipp-browse-dialog.ui
%{_datadir}/apps/system-config-printer-kde/options.py
%{_datadir}/apps/system-config-printer-kde/optionwidgets.py
%{_datadir}/apps/system-config-printer-kde/smb-browse-dialog.ui
%{_datadir}/kde4/services/system-config-printer-kde.desktop

%files ksystemlog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksystemlog
%dir %{_datadir}/apps/ksystemlog
%{_desktopdir}/kde4/ksystemlog.desktop
%{_datadir}/apps/ksystemlog/ksystemlogui.rc
#%{_iconsdir}/hicolor/scalable/apps/ksystemlog.svgz
%{_kdedocdir}/en/ksystemlog

%files kuser -f kuser.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_datadir}/config.kcfg/kuser.kcfg
%{_desktopdir}/kde4/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png

knetworkconf, removed incomplete base es desc
- use find_lang for kdedoc

Revision 1.4  2008-01-14 11:16:28  pascalek
- files fixes

Revision 1.3  2008-01-12 20:45:10  rotom
- up to 4.0.0 stable (NFY)

Revision 1.2  2007-12-11 22:56:44  glen
- no ed needed

Revision 1.1  2007-12-11 22:09:51  rotom
- now as kdeadmin4.spec (NFY)

Revision 1.163.2.4  2007/02/12 13:20:13  baggins
- converted to UTF-8

Revision 1.163.2.3  2006/12/19 12:05:50  shadzik
- BR qt4-qmake

Revision 1.163.2.2  2006/12/19 11:23:24  rotom
- adaptized

Revision 1.163.2.1  2006/12/19 10:06:05  rotom
- kde4 (3.80.2)

Revision 1.163  2006/11/28 23:07:21  arekm
- disable R: libtool() stuff

Revision 1.162  2006/11/03 11:06:55  glen
- rel 1

Revision 1.161  2006/10/10 22:18:37  glen
- added kde-common-PLD.patch

Revision 1.160  2006/10/05 06:53:12  arekm
- add kde-ac260-lt.patch

Revision 1.159  2006/10/04 21:14:54  adgor
- 3.5.5 .hidden

Revision 1.158  2006/08/08 11:15:32  glen
- rel 2

Revision 1.157  2006/08/04 02:45:45  glen
- perl autodeps for knetworkconf

Revision 1.156  2006/08/04 02:42:01  glen
- identify PLD Ac in knetworkconf
- correct permissions in knetworkconf

Revision 1.155  2006/07/31 16:04:02  glen
- use macro in todo

Revision 1.154  2006/07/31 07:02:56  arekm
- 3.5.4

Revision 1.153  2006/05/25 16:32:31  arekm
- up to 3.5.3

Revision 1.152  2006/03/29 13:27:43  glen
- really update to 3.5.2 (previous commit was error)

Revision 1.151  2006/03/29 11:28:58  glen
- 3.5.2

Revision 1.150  2006/02/28 23:37:25  glen
- adapterized (killed trailing spaces/tabs)

Revision 1.149  2006/01/25 16:35:10  pluto
- disable all-in-one compilation.

Revision 1.148  2006/01/22 22:32:30  arekm
- up to 3.5.1

Revision 1.147  2006/01/21 00:01:16  arekm
- kill Icon: field (support for these is obsolete says jbj)

Revision 1.146  2006/01/09 17:49:30  arekm
- rel 2; lilo is not available on sparc

Revision 1.145  2005/11/24 14:53:57  arekm
- rel 1

Revision 1.144  2005/10/09 20:08:34  arekm
- rel 1

Revision 1.143  2005/10/06 20:35:19  arekm
- up to 3.4.3

Revision 1.142  2005/07/29 06:20:18  arekm
- kcmlilo exists also on sparc

Revision 1.141  2005/07/28 20:27:42  arekm
- rel 1

Revision 1.140  2005/07/21 20:33:06  arekm
- up to 3.4.2

Revision 1.139  2005/06/17 22:25:00  arekm
- rel up; bump BR to rpm-devel >= 4.4.1

Revision 1.138  2005/06/17 16:29:20  baggins
- release 2 to rebuild with rpm 4.4.1 in AC

Revision 1.137  2005/06/01 06:09:08  arekm
- rel 1

Revision 1.136  2005/05/26 10:05:37  arekm
- up to 3.4.1

Revision 1.135  2005/05/25 08:19:04  ankry
- enable kcmlilo on amd64, rel. 2

Revision 1.134  2005/05/24 17:02:47  arekm
- kcmlinuz no longer exists.

Revision 1.133  2005/03/26 16:56:33  arekm
- rel 1; add missing requires (mkochano)

Revision 1.132  2005/03/16 21:25:24  qboosh
- adjusted -kcmlinuz Obsoletes

Revision 1.131  2005/03/16 18:30:23  arekm
- on ftp it sits in 3.4 dir

Revision 1.130  2005/03/16 17:24:01  arekm
- merge from DEVEL

Revision 1.129.2.3  2005/03/05 19:01:15  arekm
- up to 3.4.0

Revision 1.129.2.2  2005/02/24 08:05:39  adgor
- No unsermake BR at this moment

Revision 1.129.2.1  2005/02/20 12:03:54  adgor
- 3.3.92.050217
