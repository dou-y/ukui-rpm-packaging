# enable download source
%undefine _disable_source_fetch

Name:           ukui-control-center
Version:        2.0.4
Release:        1%{?dist}
Summary:        utilities to configure the UKUI desktop


License:        GPLv2+
URL:            https://github.com/ukui/%{name}
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  glib2-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libxklavier-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  dconf-devel
BuildRequires:  redshift
BuildRequires:  edid-decode
BuildRequires:  libmatemixer-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  libxml2-devel
BuildRequires:  libkscreen-qt5-devel
BuildRequires:  kf5-ki18n-devel
Recommends: edid-decode
Recommends: redshift
Recommends: qml-module-qtquick-controls


Suggests: gsettings-desktop-schemas
Suggests: mate-desktop-common
Suggests: ukui-power-manager
Suggests: ukui-session-manager
Suggests: ukui-screensaver
Suggests: ukui-settings-daemon
Suggests: qml-module-qtgraphicaleffects


%description
utilities to configure the UKUI desktop
 The UKUI control center contains configuration applets for the UKUI desktop,
 allowing to set accessibility configuration, desktop fonts, keyboard
 and mouse properties, sound setup, desktop theme and background, user
 interface properties, screen resolution, and other UKUI parameters.

%prep
%setup -q
find . -name "*.pro" | xargs sed -i '/inst2.path/s/lib/lib64/g' 

%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ukui-control-center.pro	
  make
%install
rm -rf %{buildroot} 
%{make_install}  INSTALL_ROOT=%{buildroot} 

%files
%{_bindir}/launchSysDbus
%{_bindir}/ukui-control-center
%{_libdir}/control-center/pluginlibs
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.experienceplan.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.keybinding.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.notice.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.panel.plugins.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.control-center.wifi.switch.gschema.xml
%{_datadir}/applications/ukui-control-center.desktop
%{_datadir}/ukui/faces/