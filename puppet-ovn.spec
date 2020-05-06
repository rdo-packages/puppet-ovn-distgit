%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-ovn
Version:                16.3.0
Release:                1%{?dist}
Summary:                Puppet module to setup ovn-northd and ovn-controller
License:                ASL 2.0

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
* Wed May 06 2020 RDO <dev@lists.rdoproject.org> 16.3.0-1
- Update to 16.3.0



