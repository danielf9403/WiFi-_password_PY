from lib2to3.pytree import _Results
import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles' ]).decode('ut-f8',errors='backsplasreplace').split('\n')

profiles = [i.split(":")[1][1:-1]
            for i in data 
            if"All User Profiles" in i]

for i in profiles:
    try:
        result = subprocess.check_output(['netsh','wlan','show','profile', i, 'key=clear' ]).decode('ut-f8',errors='backsplasreplace').split('\n')
    result = [b.split(":")[1][1:-1] for b in 
                _Results if "Key Content" in b]
    try:
        print("{:<30}|{:<}".format(i, result[0]))
        expect IndexError:
            print("{:<30}| {:<}".format(i, ""))