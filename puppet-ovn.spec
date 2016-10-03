%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-ovn
Version:                9.4.0
Release:                1%{?dist}
Summary:                Puppet module to setup ovn-northd and ovn-controller
License:                Apache-2.0

URL:                    https://launchpad.net/puppet-ovn

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet >= 2.7.0

%description
Puppet module to install and configure ovn

%prep
%setup -q -n openstack-ovn-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/ovn/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/ovn/



%files
%{_datadir}/openstack-puppet/modules/ovn/


%changelog
* Thu Sep 29 2016 Alfredo Moralejo <amoralej@redhat.com> 9.4.0-1
- Update to 9.4.0

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.3.0-1
- Update to 9.3.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.2.0-1
- Update to 9.2.0


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-ovn/commit/?id=5f13128b308f754d6d5ae20c3929ef1fe8e4085d
