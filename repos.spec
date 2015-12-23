Name:           repos
Version:        0.0.1
Release:        1%{?dist}
Summary:        RPM Package containing my repository file

License:        GPLv3
URL:            https://eptitude.github.io
Source0:        http://eptitude.github.io/repos.tar.gz

%description
Installs my custom made repo configuration file 

%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p docker.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p collectd.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/docker.repo
/etc/yum.repos.d/collectd.repo

%changelog
* Wed Dec 23 2015 Alessandro Vozza <alessandro@ams0.org> 0.0.1
- This is my custom RPM for my repo files and GPG key required to install

