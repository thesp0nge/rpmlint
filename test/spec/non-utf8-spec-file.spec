Name:           non-utf8-spec-file
Version:        0
Release:        0
Summary:        non-utf8-spec-file warning
License:        GPL-2.0-only
Group:          Undefined
URL:            http://rpmlint.zarb.org/#%{name}
Source0:        Source0.tar.gz

%description
The character encoding of the spec file is not UTF-8.

%prep
  %autosetup

%build

%install

%files
%{_libdir}/foo

%changelog
