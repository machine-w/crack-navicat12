#coding:utf-8
import pyregedit

root = pyregedit.HKEY_CURRENT_USER
deleteList = []
path1 = r"Software\PremiumSoft\Data"
r = pyregedit.RegEdit(root, path1)
#r.delete_current_key()
path2 = r"Software\Classes\CLSID"
reg = pyregedit.RegEdit(root, path2)
with open('patch.bat', 'w') as the_file:
    for node in reg.get_sub_keys():
        reg2 = pyregedit.RegEdit(root,path2+ '\\'+ node.strip())
        if 'Info' in list(reg2.get_sub_keys()):
            #os.system('reg delete %s /f' % ('HKEY_CURRENT_USER\\'+path2+ '\\'+ node.rstrip()))
            the_file.write('reg delete HKEY_CURRENT_USER\\'+path2+ '\\'+ node + ' /f\n')
    the_file.write(r'reg delete HKEY_CURRENT_USER\Software\PremiumSoft\Data /f ')