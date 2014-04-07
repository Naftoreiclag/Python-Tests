
import sys

modfilenames = ["TestMod"]

for modfile in modfilenames:
    exec("import " + modfile)

for modfile in modfilenames:
    members = sys.modules[modfile]
    
    for memberName in members.__dict__:
        
        if memberName[:2] != "__":
            
            print modfile, memberName, members.__dict__[memberName]
