Summary:	GTK+ greeter for lightdm
Name:		lightdm-gtk-greeter
Version:	2.0.5
Release:	1
License:	GPL v3
Group:		Themes
Source0:	https://launchpad.net/lightdm-gtk-greeter/2.0/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	0274c3bf4387944d322941f85bdf91b9
Patch0:		paths.patch
URL:		https://launchpad.net/lightdm-gtk-greeter
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.10.4-3
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk+3-devel
BuildRequires:	libtool
BuildRequires:	lightdm-libs-gobject-devel >= 1.3.5
BuildRequires:	xorg-lib-libX11-devel
Requires:	hicolor-icon-theme
Provides:	lightdm-greeter
Obsoletes:	lightdm-greeter-gtk < 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reference GTK+ greeter for LightDM.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-at-spi-command="%{_libdir}/at-spi-bus-launcher --launch-immediately" \
	--disable-indicator-services-command \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{lb,wae}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/lightdm-gtk-greeter

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lightdm/%{name}.conf
%attr(755,root,root) %{_sbindir}/%{name}
%{_iconsdir}/hicolor/scalable/places/*.svg
%{_datadir}/xgreeters/%{name}.desktop
