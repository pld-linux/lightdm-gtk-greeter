Summary:	GTK+ greeter for lightdm
Name:		lightdm-gtk-greeter
Version:	2.0.0
Release:	1
License:	GPL v3
Group:		Themes
Source0:	https://launchpad.net/lightdm-gtk-greeter/2.0/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	bae8175cabffe1bca43fb4990c8632af
Patch0:		paths.patch
URL:		https://launchpad.net/lightdm-gtk-greeter
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.35.0
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
