# TODO
# - fix broken tests
# - use system js libraries

# Conditional build:
%bcond_with	tests	# do not perform "make test"

Summary:	Circus: A Process & Socket Manager¶
Name:		circus
Version:	0.6.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/c/circus/%{name}-%{version}.tar.gz
# Source0-md5:	c8480c35f306aabbc7fcfd83be5b3925
Patch0:		unittest2.patch
URL:		http://circus.readthedocs.org/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with tests}
BuildRequires:	python-iowait >= 0.1
BuildRequires:	python-psutil >= 0.6.1
BuildRequires:	python-webtest
BuildRequires:	python-zmq >= 2.2.0
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Circus is a program that will let you run and watch multiple processes
and sockets.

Circus is a program that runs and watches processes and sockets.

Circus can be used as a library or through the command line.

%prep
%setup -q
%patch0 -p1

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/tests

# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%attr(755,root,root) %{_bindir}/circus-plugin
%attr(755,root,root) %{_bindir}/circus-top
%attr(755,root,root) %{_bindir}/circusctl
%attr(755,root,root) %{_bindir}/circusd
%attr(755,root,root) %{_bindir}/circusd-stats
%attr(755,root,root) %{_bindir}/circushttpd

%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%dir %{py_sitescriptdir}/%{name}/commands
%{py_sitescriptdir}/%{name}/commands/*.py[co]
%dir %{py_sitescriptdir}/%{name}/plugins
%{py_sitescriptdir}/%{name}/plugins/*.py[co]
%dir %{py_sitescriptdir}/%{name}/stats
%{py_sitescriptdir}/%{name}/stats/*.py[co]
%dir %{py_sitescriptdir}/%{name}/stream
%{py_sitescriptdir}/%{name}/stream/*.py[co]
%dir %{py_sitescriptdir}/%{name}/web
%{py_sitescriptdir}/%{name}/web/*.html
%{py_sitescriptdir}/%{name}/web/*.png
%{py_sitescriptdir}/%{name}/web/*.py[co]
%{py_sitescriptdir}/%{name}/web/favicon.ico
%{py_sitescriptdir}/%{name}/web/circus.css
%{py_sitescriptdir}/%{name}/web/circus.js
%{py_sitescriptdir}/%{name}/web/d3.v2.js
%{py_sitescriptdir}/%{name}/web/jquery.min.js
%{py_sitescriptdir}/%{name}/web/jquery.sparkline.min.js
%{py_sitescriptdir}/%{name}/web/rickshaw.min.css
%{py_sitescriptdir}/%{name}/web/rickshaw.min.js
%{py_sitescriptdir}/%{name}/web/socket.io.js
%{py_sitescriptdir}/%{name}/web/web-requirements.txt
%{py_sitescriptdir}/%{name}-%{version}-py*.egg-info

%dir %{py_sitescriptdir}/fl
%{py_sitescriptdir}/fl/*.py[co]
