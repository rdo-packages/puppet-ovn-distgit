%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-ovn
Version:                10.5.0
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
* Fri Jan 19 2018 RDO <dev@lists.rdoproject.org> 10.5.0-1
- Update to 10.5.0

* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 10.4.1-1
- Update to 10.4.1

* Mon Mar 13 2017 Alfredo Moralejo <amoralej@redhat.com> 10.4.0-1
- Update to 10.4.0

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 10.3.0-1
- Update to 10.3.0


