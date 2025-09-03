from time import sleep
from  colorama import  Fore, Style

max_heart_rate = 101
min_heart_rate = 60
max_glucose = 91
min_glucose = 75
name = input("Please enter your name: ")
print(Fore.YELLOW + f"Hello {name}, in order to complete your registration, you need to give some medical details " + Style.RESET_ALL)
sleep(2)
patient_heart_rate = int(input(Fore.BLUE + Style.BRIGHT  + "Please insert your heart rate: "))
patient_glucose = int(input("Please check your glucose level: " + Style.RESET_ALL))
print("=" * 30)
if patient_heart_rate in range(min_heart_rate, max_heart_rate) and patient_glucose in range(min_glucose, max_glucose):
    status = "You are in good shape"
    print(Fore.GREEN + Style.BRIGHT + status +Style.RESET_ALL)
    sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "Please proceed to HR Office" +Style.RESET_ALL)
else:
    status = "Go see your Doctor ASAP"
    print(Fore.RED + Style.BRIGHT + status + Style.RESET_ALL)
    sleep(1)
    print(Fore.RED + Style.BRIGHT + "Return with a medical approval that everything is fine" + Style.RESET_ALL)

print("=" * 30)
name2 = input("Please enter your name: ")
if name2 == name:
    if "You are in good shape" == status:
        print("Welcome to the company, lets start your ONBOARD process")
    else:
        print("Please present the medical approval you received from your doctor")
else:
    print("Please return to first station")

