# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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

Name: python-filelock
Epoch: 100
Version: 3.8.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Platform independent file lock for Python
License: Unlicense
URL: https://github.com/tox-dev/py-filelock/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package contains a single module, which implements a platform
independent file locking mechanism for Python. The lock includes a lock
counter and is thread safe. This means, when locking the same lock
object twice, it will not block.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-filelock
Summary: Platform independent file lock for Python
Requires: python3
Provides: python3-filelock = %{epoch}:%{version}-%{release}
Provides: python3dist(filelock) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-filelock = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(filelock) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-filelock = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(filelock) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-filelock
This package contains a single module, which implements a platform
independent file locking mechanism for Python. The lock includes a lock
counter and is thread safe. This means, when locking the same lock
object twice, it will not block.

%files -n python%{python3_version_nodots}-filelock
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 700)
%package -n python3-filelock
Summary: Platform independent file lock for Python
Requires: python3
Provides: python3-filelock = %{epoch}:%{version}-%{release}
Provides: python3dist(filelock) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-filelock = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(filelock) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-filelock = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(filelock) = %{epoch}:%{version}-%{release}

%description -n python3-filelock
This package contains a single module, which implements a platform
independent file locking mechanism for Python. The lock includes a lock
counter and is thread safe. This means, when locking the same lock
object twice, it will not block.

%files -n python3-filelock
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
