#processFinder is a programme that can find a programme is in process or not.
#
import psutil
#
print('+++   PorcessFinder   +++')
print('')
processName = input('Enter programme to find ==> ')
print('')
print('In process....')
print('')
#
def checkCMDProcessRunning(processName):
    for pro in psutil.process_iter():
        try:
            if processName.lower() in pro.name().lower():
                return True
        except(pstil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return False;
#
if checkCMDProcessRunning(processName):
    print(processName,' is running!!!')
    print('')
else:
    print(processName,' is not running!!!')
    print('')
