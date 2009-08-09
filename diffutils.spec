Summary:	A GNU collection of diff utilities
Name:		diffutils
Version:	2.8.7
Release:	%mkrel 10
License:	GPLv2+
Group:		Development/Other
URL:		http://www.gnu.org/software/diffutils/
Source0:	ftp://alpha.gnu.org/gnu/diffutils/diffutils-%{version}.tar.gz
Source1:	%{SOURCE0}.sig
Source2:	%{name}-help2man.bz2
Patch2:		%{name}-2.8.7-i18n.patch
Patch3:		diffutils-2.8.7-format_not_a_string_literal_and_no_format_arguments.diff
Requires(pre):	info-install
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch2 -p1 -b .i18n
%patch3 -p0 -b .format_not_a_string_literal_and_no_format_arguments

bzcat %{SOURCE2} > help2man
chmod +x help2man

%build
# for finding help2man
export PATH=$PATH:`pwd`

%configure2_5x

# default editor for sdiff interactive mode, vi is likely better than ed
perl -pi -e 's/^(#define\s+DEFAULT_EDITOR_PROGRAM\s+)"ed"/$1"vi"/' config.h

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post 
%_install_info diff.info

%preun
%_remove_install_info diff.info

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_infodir}/diff.info*

