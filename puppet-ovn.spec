Name:                   puppet-barbican
Version:                XXX
Release:                XXX
Summary:                Puppet module for OpenStack Barbican
License:                Apache-2.0

URL:                    https://launchpad.net/puppet-ovn

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-stdlib
Requires:               puppet-keystone
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet >= 2.7.0

%description
Installs and configures puppet-ovn module.

%prep
%setup -q -n %{name}-%{version}

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

