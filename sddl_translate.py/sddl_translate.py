#!C:\Python24\python.exe

"""Print out an SDDL string in human-readable format."""

__author__ = 'timjohnson@google.com (Tim Johnson)'
__version__ = '0.1'
__updated__ = '2008-07-14'

import sys
import SDDL

sddl_type = None
target = None

if len(sys.argv) < 2:
  print '\nError:  You must supply at least one SDDL string as an argument!\n'
  print 'USAGE: SDDLTranslate.py <SDDL_Strings> [type]\n'
  print 'Note: the only supported type at this time is "service"\n'
  sys.exit(1)

if sys.argv[-1] == 'service':
  target = 'service'

for string in sys.argv[1:]:
  if string.lower() == 'service':
    continue

  print '\nSDDL String: ' + string + '\n'
  sec = SDDL.SDDL(string, target)
  print 'Type: ' + sec.sddl_type

  if sec.owner_sid:
    print '\tOwner Name: ' + sec.owner_account
    print '\tOwner SID: ' + sec.owner_sid + '\n'

  if sec.group_sid:
    print '\tGroup Name: ' + sec.group_account
    print '\tGroup SID: ' + sec.group_sid + '\n'

  print '\tAccess Control Entries:\n'
  sec.acl.sort(cmp=SDDL.SortAceByTrustee)
  for ace in sec.acl:
    print '\t\tTrustee: ' + ace.trustee
    print '\t\tACE Type: ' + ace.ace_type
    print '\t\tPerms:'

    for perm in ace.perms:
      print '\t\t\t' + perm

    if ace.flags:
      print '\t\tFlags:'

      for flag in ace.flags:
        print '\t\t\t' + flag

    if ace.object_type:
      print '\t\tObject Type: ' + ace.object_type

    if ace.inherited_type:
      print '\t\tInherited Type: ' + ace.inherited_type

    print ''

  print ''

