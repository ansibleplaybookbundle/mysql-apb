%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name:		mysql-apb-role
Version:	1.0.5
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for MariaDB APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/RHSCL-MySQL-APB
Source0:	https://github.com/ansibleplaybookbundle/RHSCL-MySQL-APB/archive/%{name}-%{version}.tar.gz
BuildArch:  	noarch


%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/
mv playbooks %{buildroot}/opt/apb/actions
mv roles %{buildroot}/opt/ansible/roles

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Thu Oct 19 2017 David Zager <david.j.zager@gmail.com> 1.0.5-1
- Bug 1503523 - Add asb module to deprovision yaml (david.j.zager@gmail.com)

* Tue Oct 10 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- Update dockerfiles (david.j.zager@gmail.com)
- Bug 1500364 - Update apb.yml with all dependent images
  (david.j.zager@gmail.com)

* Mon Oct 09 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- Updated mysql image to use rhscl instead of centos (dymurray@redhat.com)
- Bug 1498571 - Remove image from APB (david.j.zager@gmail.com)

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- new package built with tito

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com>
- new package built with tito

* Thu Sep 28 2017 David Zager <dzager@redhat.com> 1.0.0-1
- new package built with tito

