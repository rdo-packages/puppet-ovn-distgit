%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-ovn
Version:                17.6.0
Release:                1%{?dist}
Summary:                Puppet module to setup ovn-northd and ovn-controller
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-ovn

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:              noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:               puppet-stdlib
Requires:               puppet >= 2.7.0

%description
Puppet module to install and configure ovn

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Tue May 03 2022 RDO <dev@lists.rdoproject.org> 17.6.0-1
- Update to 17.6.0

* Fri Jun 11 2021 RDO <dev@lists.rdoproject.org> 17.5.0-1
- Update to 17.5.0

* Tue Oct 20 2020 Joel Capitao <jcapitao@redhat.com> 17.4.0-2
- Enable sources tarball validation using GPG signature.

* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 17.4.0-1
- Update to 17.4.0



