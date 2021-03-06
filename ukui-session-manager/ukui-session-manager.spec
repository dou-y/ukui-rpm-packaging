# enable download source
%undefine _disable_source_fetch

Name:           ukui-session-manager
Version:        master
Release:        1%{?dist}
Summary:        Session manager of the UKUI desktop environment


License:        LGPL-2.1 License
URL:            https://github.com/ukui/ukui-session-manager
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

BuildArch:      x86_64
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  qt5-qttools-devel 
BuildRequires:  qt5-qttools
BuildRequires:  qt5-linguist
BuildRequires:  gsettings-qt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  systemd-devel

Requires: peony
Requires: ukui-kwin
Requires: ukui-panel
Requires: ukui-polkit
Requires: ukui-screensaver
Requires: ukui-settings-daemon

Provides: x-session-manager


%description
 This package contains a session that can be started from a display
 manager such as lightdm. It will load all necessary applications for
 a full-featured user session.
 This package contain the session manager component.

%prep
%setup -q

%build
mkdir cmake-build
pushd cmake-build
%cmake3 ..
%{make_build}
popd

%install
pushd cmake-build
%make_install INSTALL_ROOT=%{buildroot}
popd
mkdir -p %{buildroot}/etc/X11/Xsession.d/    %{buildroot}/usr/share/man/man1/
install -m644  debian/99ukui-environment %{buildroot}/etc/X11/Xsession.d/99ukui-environment
gzip -c man/ukui-session.1 >  %{buildroot}/usr/share/man/man1/ukui-session.1.gz 
gzip -c man/ukui-session-tools.1 > %{buildroot}/usr/share/man/man1/ukui-session-tools.1.gz


%files
%doc debian/changelog debian/copyright
%{_datadir}/ukui/translations/ukui-session-manager/
%{_datadir}/xsessions/ukui.desktop
%{_datadir}/glib-2.0/schemas/org.ukui.session.gschema.xml
%{_bindir}/ukui-session
%{_bindir}/ukui-session-tools
%{_sysconfdir}/X11/Xsession.d/99ukui-environment
%{_datadir}/man/man1/ukui-session.1.gz 
%{_datadir}/man/man1/ukui-session-tools.1.gz