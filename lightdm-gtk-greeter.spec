Summary:	GTK+ greeter for lightdm
Name:		lightdm-gtk-greeter
Version:	1.1.1
Release:	2
License:	GPL v3
Group:		Themes
Source0:	https://launchpad.net/lightdm-gtk-greeter/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	6dcbcd2b8e71ab510fd16550368b4996
URL:		https://launchpad.net/lightdm-gtk-greeter
BuildRequires:	gtk+3-devel
BuildRequires:	lightdm-devel
Provides:	lightdm-greeter
Obsoletes:	lightdm-greeter-gtk < 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reference GTK+ greeter for LightDM.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{lb,wae}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lightdm/%{name}.conf
%attr(755,root,root) %{_sbindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/xgreeters/%{name}.desktop
