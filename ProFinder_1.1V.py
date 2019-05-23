#
#ProFinder is a programme that can find a programme which is in process or not.
#ProFinder will update you by sending an e-mail when the process is over.
#
import psutil
import smtplib
#
print('********************************')
print('****     ProFinder 1.1V     ****')
print('********************************')
print('')
print('Welcome to ProFinder 1.1V!!!')
print('Before start useing ProFinder 1.1V, you have to sigin in.')
print('')
emailAddress = input('E-mail address : ')
password = input('Password       : ')
print('')
#
subject = 'ProFinder 1.1V Update'
message = 'Your process is over!!!\n\nThank you for using ProFinder 1.1V'
#
print('')
processName = input('Enter programme or process to find : ')
print('')
print('In process....')
print('')
#
#sendMail() function notifies the user about the status of the programme or process with an email
#
def sendMail(emailAddress,receiverEMail,password,subject,message):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(emailAddress,password)
        message = 'Subject: {}\n\n{}'.format(subject,message)
        server.sendmail(emailAddress,receiverEMail,message)
        server.quit()
        print('')
        print("E-mail sent succsessfully!!!")
        print('')
    except:
        print("Problem detected!!!")
        print("")
        print("   + Pleace check your e-mail has enabled less secure apps. If not pleace enable.")
        print("   + Check the internet connection")
        print("   + Check whether you have given the correct e-mail address and password.")
#
#checkCMDProcessRunning() function checks the programme or process is running or not.
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
#runProcess() function runs the main programme
#
def runProcess():
    if checkCMDProcessRunning(processName):
        runProcess()
    else:
        print(processName,'is not running!!!')
        sendMail(emailAddress,emailAddress,password,subject,message)
        print('')
#
runProcess()
