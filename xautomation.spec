Summary:	Tools for controling X from the command line
Summary(pl.UTF-8):   Narzędzia do sterowania X Window System z linii poleceń
Name:		xautomation
Version:	0.96
Release:	1
Epoch:		0
License:	GPL v2+
Vendor:		Steve Slaven <bpk@hoopajoo.net>
Group:		X11/Applications
Source0:	http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz
# Source0-md5:	55f1247f9e25d57ba23e9e9f3cf5f87e
URL:		http://hoopajoo.net/projects/xautomation.html
BuildRequires:	XFree86-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The control interface allows mouse movement, clicking, button up/down,
key up/down, etc. The visgrep program find images inside of images and
reports the coordinates, allowing progams to find buttons, etc, on the
screen to click on.

Useful with tools like <http://bur.st/~benc/index.pl?p=external-edit>.

%description -l pl.UTF-8
Narzędzia pozwalają na poruszanie wskaźnikiem myszy, ,,naciskanie''
przycisków na klawiaturze itd. visgrep szuka obrazów w obrazach, by
można było zlokalizować przyciski do kliknięcia.

Użyteczne z narzędziami w rodzaju
<http://bur.st/~benc/index.pl?p=external-edit>.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
