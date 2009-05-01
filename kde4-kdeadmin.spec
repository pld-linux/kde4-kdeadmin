# TODO
#   %{_pkgconfigdir}/system-tools-backends.pc
%define		_state		stable
%define		orgname		kdeadmin
%define		qtver		4.5.0

%include	/usr/lib/rpm/macros.perl

Summary:	K Desktop Environment - administrative tools
Summary(es.UTF-8):	K Desktop Environment - herramientas administrativas
Summary(ko.UTF-8):	K 데스크탑 환경 - 관리 도구
Summary(pl.UTF-8):	K Desktop Environment - narzędzia administratora
Summary(pt_BR.UTF-8):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN.UTF-8):	KDE管理工具
Name:		kde4-kdeadmin
Version:	4.2.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	dc352ccb03c285a87fcc68d7d18e9d43
Patch0:		%{name}-liloconfig.patch
Patch1:		%{name}-printer.patch
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	pam-devel
BuildRequires:	python-PyQt4-devel
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	xorg-lib-libXxf86misc-devel
Requires:	shadow
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

%package knetworkconf
Summary:	KDE Network Configurator
Summary(pl.UTF-8):	Konfigurator sieci dla KDE
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}

%description knetworkconf
KDE Network Configurator.

%description knetworkconf -l pl.UTF-8
Konfigurator sieci dla KDE.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p0
%patch1 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DINSTALL_SYSTEM_CONFIG_PRINTER=TRUE \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang kcron	--with-kde
#%find_lang kdat		--with-kde
%find_lang kpackage	--with-kde
%find_lang kuser	--with-kde
#%find_lang knetworkconf --with-kde
%ifarch %{ix86} %{x8664}
%find_lang lilo-config	--with-kde
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%ifarch %{ix86} %{x8664}
%files kcmlilo -f lilo-config.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_lilo.so
%{_datadir}/kde4/services/lilo.desktop
%endif

%files kcron -f kcron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_cron.so
%{_datadir}/kde4/services/kcm_cron.desktop
#%{_kdedocdir}/en/kcron

%files kpackage -f kpackage.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage
#%attr(755,root,root) %{_libdir}/kde4/kfile*.so
%{_datadir}/apps/kpackage
#%{_datadir}/services/kfile*
%{_desktopdir}/kde4/kpackage.desktop
%{_iconsdir}/*/*/*/kpackage.png
%{_datadir}/config.kcfg/kpackageSettings.kcfg
%{_kdedocdir}/en/kcontrol

%files kprinter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/system-config-printer-kde
%{_desktopdir}/kde4/system-config-printer-kde.desktop
%dir %{_datadir}/apps/system-config-printer-kde
%{_datadir}/apps/system-config-printer-kde/new-printer.ui
%{_datadir}/apps/system-config-printer-kde/system-config-printer-kde.py
%{_datadir}/apps/system-config-printer-kde/system-config-printer.ui

%files ksystemlog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksystemlog
%dir %{_datadir}/apps/ksystemlog
%{_desktopdir}/kde4/ksystemlog.desktop
%{_datadir}/apps/ksystemlog/ksystemlogui.rc
%{_iconsdir}/hicolor/*/apps/ksystemlog.png
#%{_iconsdir}/hicolor/scalable/apps/ksystemlog.svgz
%{_kdedocdir}/en/ksystemlog

%files kuser -f kuser.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_datadir}/config.kcfg/kuser.kcfg
%{_desktopdir}/kde4/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png

%files knetworkconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_knetworkconf*.so
%dir %{_datadir}/apps/knetworkconf
%dir %{_datadir}/apps/knetworkconf/backends
%attr(755,root,root) %{_datadir}/apps/knetworkconf/backends/*
%{_datadir}/apps/knetworkconf/pixmaps
%{_datadir}/kde4/services/kcm_knetworkconfmodule.desktop
%{_iconsdir}/*/*/*/knetworkconf.png
%{_iconsdir}/*/*/actions/network_*.png
# -devel?
#%{_pkgconfigdir}/system-tools-backends.pc
