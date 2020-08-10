Summary:	GTK+ greeter for lightdm
Name:		lightdm-gtk-greeter
Version:	2.0.8
Release:	1
License:	GPL v3
Group:		Themes
Source0:	https://github.com/Xubuntu/lightdm-gtk-greeter/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	373c73c67367df511eb544e09a2da281
Patch0:		paths.patch
URL:		https://github.com/Xubuntu/lightdm-gtk-greeter
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk+3-devel
BuildRequires:	libtool
BuildRequires:	lightdm-libs-gobject-devel >= 1.19.2
BuildRequires:	xfce4-dev-tools
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
