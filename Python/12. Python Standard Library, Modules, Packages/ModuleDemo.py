from MyFuncyLib import modulea
import MyFuncyLib.GameFuncs.modulea

print('sumofsquares', modulea.sumofsquares(3))

print('from 2nd import, sub dir')
print('sumofsquares', MyFuncyLib.GameFuncs.modulea.sumofsquares(3))

print('from 2nd import, sub dir')
print('sumofcubes', MyFuncyLib.GameFuncs.modulea.sumofcubes(3))

x = modulea.sumofsquares(3)
print('X', x)

print('last call')
modulea.sumofsquares(3)

