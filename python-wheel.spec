# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-wheel
Epoch: 100
Version: 0.44.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Built-package format for Python
License: MIT
URL: https://github.com/pypa/wheel/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel

%description
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build
python3 setup.py bdist_wheel

%install
%py3_install
%if 0%{?suse_version} > 1500
install -Dpm755 -d %{buildroot}%{python3_sitelib}/../wheels
install -Dpm644 -t %{buildroot}%{python3_sitelib}/../wheels dist/*.whl
%endif
%if 0%{?rhel} >= 7
install -Dpm755 -d %{buildroot}%{_datarootdir}/%{python3_version}-wheels
install -Dpm644 -t %{buildroot}%{_datarootdir}/%{python3_version}-wheels dist/*.whl
%endif
%if !(0%{?suse_version} > 1500) && !(0%{?rhel} >= 7)
install -Dpm755 -d %{buildroot}%{_datarootdir}/python-wheels
install -Dpm644 -t %{buildroot}%{_datarootdir}/python-wheels dist/*.whl
%endif
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python_version_nodots}-wheel
Summary: Built-package format for Python
Requires: python3
Provides: python3-wheel = %{epoch}:%{version}-%{release}
Provides: python3dist(wheel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wheel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wheel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wheel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wheel) = %{epoch}:%{version}-%{release}

%description -n python%{python_version_nodots}-wheel
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%package -n python%{python_version_nodots}-wheel-wheel
Summary: The Python wheel module packaged as a wheel

%description -n python%{python_version_nodots}-wheel-wheel
A Python wheel of wheel to use with virtualenv.

%files -n python%{python_version_nodots}-wheel
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*

%files -n python%{python_version_nodots}-wheel-wheel
%dir %{python3_sitelib}/../wheels
%{python3_sitelib}/../wheels/*.whl
%endif

%if 0%{?rhel} >= 7
%package -n python3-wheel
Summary: Built-package format for Python
Requires: python3
Provides: python3-wheel = %{epoch}:%{version}-%{release}
Provides: python3dist(wheel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wheel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wheel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wheel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wheel) = %{epoch}:%{version}-%{release}

%description -n python3-wheel
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%package -n python3-wheel-wheel
Summary: The Python wheel module packaged as a wheel

%description -n python3-wheel-wheel
A Python wheel of wheel to use with virtualenv.

%files -n python3-wheel
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*

%files -n python3-wheel-wheel
%dir %{_datarootdir}/%{python3_version}-wheels
%{_datarootdir}/%{python3_version}-wheels/*.whl
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} >= 7)
%package -n python3-wheel
Summary: Built-package format for Python
Requires: python3
Provides: python3-wheel = %{epoch}:%{version}-%{release}
Provides: python3dist(wheel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wheel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wheel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wheel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wheel) = %{epoch}:%{version}-%{release}

%description -n python3-wheel
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%package -n python-wheel-wheel
Summary: The Python wheel module packaged as a wheel

%description -n python-wheel-wheel
A Python wheel of wheel to use with virtualenv.

%files -n python3-wheel
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*

%files -n python-wheel-wheel
%dir %{_datarootdir}/python-wheels
%{_datarootdir}/python-wheels/*.whl
%endif

%changelog
