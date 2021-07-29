import os
try:
    import openpyxl
except:
    import os
    os.system('pip install openpyxl')

try:
    import KEEpydb
except:
    print('installing KEEpydb please wait ...')
    import sys
    paths=sys.path()
    os.system('mkdir KEEpydb')
    for i in os.listdir():
        os.system(f'cp -rf {i} KEEpydb')
    os.system(f'mv -rf KEEpy {paths[len(paths)-1]}')
    print('Installation Sucessfull ...')