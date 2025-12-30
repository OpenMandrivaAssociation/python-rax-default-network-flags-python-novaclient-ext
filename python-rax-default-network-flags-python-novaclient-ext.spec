Name:		python-rax-default-network-flags-python-novaclient-ext
Version:	0.4.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/r/rax-default-network-flags-python-novaclient-ext/rax_default_network_flags_python_novaclient_ext-%{version}.tar.gz
Summary:	Novaclient Extension for Instance Default Network Flags
URL:		https://pypi.org/project/rax-default-network-flags-python-novaclient-ext/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Novaclient Extension for Instance Default Network Flags

%files
%{py_sitedir}/rax_default_network_flags_python_novaclient_ext
%{py_sitedir}/rax_default_network_flags_python_novaclient_ext-*.*-info
