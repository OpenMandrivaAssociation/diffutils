Summary:	A GNU collection of diff utilities
Name:		diffutils
Version:	3.3
Release:	5
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnu.org/software/diffutils/
Source0:	ftp://ftp.gnu.org/pub/gnu/diffutils/%{name}-%{version}.tar.xz	
Source2:	%{name}-help2man.bz2

BuildRequires:	gettext-devel
BuildRequires:	libsigsegv-devel

%description
Diffutils includes four utilities:  diff, cmp, diff3 and sdiff.

  * Diff compares two files and shows the differences, line by line.
  * The cmp command shows the offset and line numbers where two files differ,
    or cmp can show the characters that differ between the two files.
  * The diff3 command shows the differences between three files. Diff3 can be
    used when two people have made independent changes to a common original;
    diff3 can produce a merged file that contains both persons' changes and
    warnings about conflicts.
  * The sdiff command can be used to list diff of two files side by side or
    merge two files interactively.

Install diffutils if you need to compare text files.

%prep
%setup -q
%apply_patches

bzcat %{SOURCE2} > help2man
chmod +x help2man

# default editor for sdiff interactive mode, vi is likely better than ed
sed -i -e 's/^(#define\s+DEFAULT_EDITOR_PROGRAM\s+)"ed"/$1"vi"/' configure*

aclocal -I m4 --dont-fix
automake -a
autoconf

%build
# for finding help2man
export PATH=$PATH:`pwd`
%configure2_5x \
	--without-included-regex \
	--with-packager="%{distribution}" \
	--with-packager-bug-reports="%{bugurl}"

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README
%{_bindir}/*
%{_mandir}/man*/*
%{_infodir}/%{name}.info*

