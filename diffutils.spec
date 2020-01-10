# (tpg) optimize it a bit
%ifnarch riscv64
%global optflags %{optflags} -O3 --rtlib=compiler-rt
%endif

Summary:	A GNU collection of diff utilities
Name:		diffutils
Version:	3.7
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnu.org/software/diffutils/
Source0:	ftp://ftp.gnu.org/pub/gnu/diffutils/%{name}-%{version}.tar.xz	
Source2:	diffutils-help2man
Patch0:		diffutils-3.6-check-for-__builtin_mul_overflow_p.patch
Patch1:		diffutils-cmp-s-empty.patch
Patch2:		diffutils-mkdir_p.patch
Patch4:		diffutils-i18n.patch
Patch6:		diffutils-3.3-change-default-editor-from-ed-to-vi.patch
BuildRequires:	gettext-devel
BuildRequires:	texinfo
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
%autopatch -p1

install -m755 %{SOURCE2} help2man

autoreconf -ivf

%build
# for finding help2man
export PATH=$PATH:`pwd`
%configure \
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
