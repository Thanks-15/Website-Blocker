from time import *  
from datetime import datetime as dt  

start_hr = 9
end_hr = 15 
  
host_path = "C:\Windows\System32\drivers\etc\hosts"  
redirect = "127.0.0.1"  
web_list = ["https://m.facebook.com","https://www.facebook.com","www.facebook.com", "facebook.com","https://www.youtube.com","www.youtube.com","youtube.com","https://www.amazon.in","www.amazon.in","amazon.in","https://www.amazon.com","www.amazon.com","amazon.com","https://mail.google.com","www.mail.google.com","mail.google.com","https://www.gmail.com","www.gmail.com","gmail.com","https://www.google.com","www.google.com","google.com"]  
  
while True:  
    if dt(dt.now().year,dt.now().month,dt.now().day,start_hr)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,end_hr):  
        print("Working hours.!! :(( !!")
        with open(host_path,"r+") as fileptr:  
            content = fileptr.read()  
            for website in web_list:  
                if website in content:  
                    pass  
                else:  
                    fileptr.write(redirect+" "+website+"\n")  
    else:  
        with open(host_path,'r+') as file:  
            content = file.readlines();  
            file.seek(0)  
            for line in content:  
                if not any(website in line for website in web_list):  
                    file.write(line)

            # this is used to remove the hostname from the host file 
            file.truncate()

        print("Fun hours.!! :)) !!")  
    sleep(2)  