while True:
    print("\nCHOOSE YOUR CHOICE - MAIN MENU")
    print("1. Course module")
    print("2. Subscriber module")
    print("3. Exit")

    ch=int(input("Choose an option:"))
    if ch==1:
        while True:
            print("\nCHOOSE YOUR CHOICE")
            print("1. All course details")
            print("2. Search for a particular course using course number")
            print("3. Search for a particular course using course name")
            print("4. Search for a particular course using college name")
            print("5. Search for a particular course using college location")
            print("6. Back to main menu")
            ch1=int(input("Choose an option from the above"))

            if ch1==1:
                print("Course information")
                print()
                #To display data in a tabular form
                print("{0:5}{1:15}{2:20}{3:25}{4:30}{5:35}".format("Course ID/Course Name", "", "Duration/College Name", "", "Location", "Contact"))
                print("-"*200)
                d={101: ['/B.Tech(Chemical)', 4, '/ShivNadir University', 'Noida, UP', 'snu.edu.in'], 102: ['/B.Tech(Civil)', 4, '/SRM Easwari Eng College', 'Ramapuram, Chennai', 'srmeaswari.ac.in'],  103: ['/B.Tech(CS & Eng)', 4, '/MIT, Manipal', 'Manipal, Karnataka', 'manipal.edu'], 104: ['/B.Tech(Electrical & Electronics)', 4, '/IIT-R', 'Roorkee, UK, India', 'iitr.ac.in'], 105: ['/B.Tech (Electronics & Comm)', 4, '/BITS, Pilani', 'Pilani, Rajasthan', 'bits-pilani.ac.in'], 106: ['/B.Tech(Mechanical)', 4, '/IIT-Bombay', 'Mumbai, Maharashtra', 'iitb.ac.in'], 107: ['/BA(Research) English', 3, "/St.Stephen's College", 'New Delhi', 'ststephens.edu'], 108: ['/BA(Research) History', 3, "/NIMS University", 'Jaipur, Rajasthan', 'nimsuniversity.org'], 109: ['/BA(Research) Intl Relations', 3, "/Adamas University", 'Barasat, Kolkata', 'adamasuniversity.ac.in'], 110: ['/BA(Research) Sociology', 3, "/Loyola College", 'Chennai, TN', 'loyolacollege.edu'], 111: ['/BA(Research) Economics', 3, "/Christ University", 'Bangalore', 'christuniversity.in'], 112: ['/BA(Research) Economics & Finance', 3, "/SSC, Kolkata", 'Kolkata, West Bengal', 'sivanathsastricollege.org'], 113: ['/BSc(Research) Biotechnology', 3, "/PUCHD, Punjab", 'Punjab, India', 'puchd.ac.in'], 114: ['/BSc(Research) Chemistry', 3, "/Nizam College", 'Hyderabad, India', 'nizamcollege.ac.in'], 115: ['/BSc(Research) Maths', 3, '/CMI, Chennai', 'Siruseri, Chennai', 'cmi.ac.in'], 116: ['/BSc(Research) Physics', 3, '/IIT Kanpur', 'Kanpur, UP', 'iitk.ac.in'], 117: ['/B.Management Studies', 3, 'University of Delhi', 'Delhi, India', 'du.ac.in'], 118: ['/MBBS', 5.5, '/AIIMS, Delhi', 'Ansari Nagar E, New Delhi', 'aiims.edu'], 119: ['/BDS', 5, '/SGT University', 'Gurgaon, Haryana', 'sgtuniversity.ac.in'], 120: ['/BAMS', 5.5,'/Banaras Hindu University', 'Varanasi, UP', 'bhu.ac.in'], 121: ['/BHMS', 5.5, '/National Inst of Homeopathy', 'Kolkata, WB', 'nih.nic.in'], 122: ['/BYNS', 4.5, '/GYNMCH', 'Arumbakkam, TN', 'gynmc.com'], 123: ['/LLB', 3, '/NLSIU', 'Bangalore, Karnataka', 'nls.ac.in'], 124: ['/BBA', 3, '/NMIMS', 'Vile Parle, Mumbai', 'nmims.edu'], 125: ['/BCom', 3, '/GGS Indraprastha University', 'Dwaraka, Delhi', 'ipu.ac.in'], 126: ['/MFM(Finance)', 2, '/JBIMS', 'Churchgate, Mumbai', 'jbims.edu'], 127: ['/BCA(Computer Appl)', 3, 'BIT, Mesra', 'Ranchi, Jharkhand', 'bitmesra.ac.in'], 128: ['/BFM(Fashion)', 3, '/NIFT, Chennai', 'Taramani, TN', 'nift.ac.in'], 129: ['/BA Psychology', 3, '/Surana College', 'Basavanagudi, Karnataka', 'suranacollege.edu.in'], 130: ['/BHM', 3, '/Oriental College of Hotel Mgmt', 'Wayanad, Kerala', 'orientalschool.com']}
                dkeys=list(d.keys())
                dkeyslen=len(dkeys)
                dvalues=list(d.values())
                for i in range(1):
                    for j in range(0,dkeyslen):
                        cid=dkeys[j]
                        cname=dvalues[j][0]
                        cdur=dvalues[j][1]
                        ccol=dvalues[j][2]
                        cloc=dvalues[j][3]
                        cctc=dvalues[j][4]
                        #Displaying data in a tabular form
                        print("{0:5}{1:15}{2:20}{3:35}{4:40}{5:50}".format(cid,cname,cdur,ccol,cloc, cctc))
                        print("-"*200)
                        
            elif ch1==2:
                d={101: ['/B.Tech(Chemical)', 4, '/ShivNadir University', 'Noida, UP', 'snu.edu.in'], 102: ['/B.Tech(Civil)', 4, '/SRM Easwari Eng College', 'Ramapuram, Chennai', 'srmeaswari.ac.in'],  103: ['/B.Tech(CS & Eng)', 4, '/MIT, Manipal', 'Manipal, Karnataka', 'manipal.edu'], 104: ['/B.Tech(Electrical & Electronics)', 4, '/IIT-R', 'Roorkee, UK, India', 'iitr.ac.in'], 105: ['/B.Tech (Electronics & Comm)', 4, '/BITS, Pilani', 'Pilani, Rajasthan', 'bits-pilani.ac.in'], 106: ['/B.Tech(Mechanical)', 4, '/IIT-Bombay', 'Mumbai, Maharashtra', 'iitb.ac.in'], 107: ['/BA(Research) English', 3, "/St.Stephen's College", 'New Delhi', 'ststephens.edu'], 108: ['/BA(Research) History', 3, "/NIMS University", 'Jaipur, Rajasthan', 'nimsuniversity.org'], 109: ['/BA(Research) Intl Relations', 3, "/Adamas University", 'Barasat, Kolkata', 'adamasuniversity.ac.in'], 110: ['/BA(Research) Sociology', 3, "/Loyola College", 'Chennai, TN', 'loyolacollege.edu'], 111: ['/BA(Research) Economics', 3, "/Christ University", 'Bangalore', 'christuniversity.in'], 112: ['/BA(Research) Economics & Finance', 3, "/SSC, Kolkata", 'Kolkata, West Bengal', 'sivanathsastricollege.org'], 113: ['/BSc(Research) Biotechnology', 3, "/PUCHD, Punjab", 'Punjab, India', 'puchd.ac.in'], 114: ['/BSc(Research) Chemistry', 3, "/Nizam College", 'Hyderabad, India', 'nizamcollege.ac.in'], 115: ['/BSc(Research) Maths', 3, '/CMI, Chennai', 'Siruseri, Chennai', 'cmi.ac.in'], 116: ['/BSc(Research) Physics', 3, '/IIT Kanpur', 'Kanpur, UP', 'iitk.ac.in'], 117: ['/B.Management Studies', 3, 'University of Delhi', 'Delhi, India', 'du.ac.in'], 118: ['/MBBS', 5.5, '/AIIMS, Delhi', 'Ansari Nagar E, New Delhi', 'aiims.edu'], 119: ['/BDS', 5, '/SGT University', 'Gurgaon, Haryana', 'sgtuniversity.ac.in'], 120: ['/BAMS', 5.5,'/Banaras Hindu University', 'Varanasi, UP', 'bhu.ac.in'], 121: ['/BHMS', 5.5, '/National Inst of Homeopathy', 'Kolkata, WB', 'nih.nic.in'], 122: ['/BYNS', 4.5, '/GYNMCH', 'Arumbakkam, TN', 'gynmc.com'], 123: ['/LLB', 3, '/NLSIU', 'Bangalore, Karnataka', 'nls.ac.in'], 124: ['/BBA', 3, '/NMIMS', 'Vile Parle, Mumbai', 'nmims.edu'], 125: ['/BCom', 3, '/GGS Indraprastha University', 'Dwaraka, Delhi', 'ipu.ac.in'], 126: ['/MFM(Finance)', 2, '/JBIMS', 'Churchgate, Mumbai', 'jbims.edu'], 127: ['/BCA(Computer Appl)', 3, 'BIT, Mesra', 'Ranchi, Jharkhand', 'bitmesra.ac.in'], 128: ['/BFM(Fashion)', 3, '/NIFT, Chennai', 'Taramani, TN', 'nift.ac.in'], 129: ['/BA Psychology', 3, '/Surana College', 'Basavanagudi, Karnataka', 'suranacollege.edu.in'], 130: ['/BHM', 3, '/Oriental College of Hotel Mgmt', 'Wayanad, Kerala', 'orientalschool.com']}
                dkeys=list(d.keys())#List of dictionary keys
                dvalues=list(d.values())#List of dictionary values
                scid=int(input("Enter course ID:"))
                if scid in dkeys:
                    print(d[scid])
                else:
                    print("Course ID invalid")

            elif ch1==3:
                d={'/B.Tech(Chemical)': [101, 4, '/ShivNadir University', 'Noida, UP', 'snu.edu.in'], '/B.Tech(Civil)': [102, 4, '/SRM Easwari Eng College', 'Ramapuram, Chennai', 'srmeaswari.ac.in'],  '/B.Tech(CS & Eng)': [103, 4, '/MIT, Manipal', 'Manipal, Karnataka', 'manipal.edu'], '/B.Tech(Electrical & Electronics)': [104, 4, '/IIT-R', 'Roorkee, UK, India', 'iitr.ac.in'], '/B.Tech (Electronics & Comm)': [105, 4, '/BITS, Pilani', 'Pilani, Rajasthan', 'bits-pilani.ac.in'], '/B.Tech(Mechanical)': [106, 4, '/IIT-Bombay', 'Mumbai, Maharashtra', 'iitb.ac.in'], '/BA(Research) English': [107, 3, "/St.Stephen's College", 'New Delhi', 'ststephens.edu'], '/BA(Research) History': [108, 3, "/NIMS University", 'Jaipur, Rajasthan', 'nimsuniversity.org'], '/BA(Research) Intl Relations': [109, 3, "/Adamas University", 'Barasat, Kolkata', 'adamasuniversity.ac.in'], '/BA(Research) Sociology': [110, 3, "/Loyola College", 'Chennai, TN', 'loyolacollege.edu'], '/BA(Research) Economics': [111, 3, "/Christ University", 'Bangalore', 'christuniversity.in'], '/BA(Research) Economics & Finance': [112, 3, "/SSC, Kolkata", 'Kolkata, West Bengal', 'sivanathsastricollege.org'], '/BSc(Research) Biotechnology': [113, 3, "/PUCHD, Punjab", 'Punjab, India', 'puchd.ac.in'], '/BSc(Research) Chemistry': [114, 3, "/Nizam College", 'Hyderabad, India', 'nizamcollege.ac.in'], '/BSc(Research) Maths': [115, 3, '/CMI, Chennai', 'Siruseri, Chennai', 'cmi.ac.in'], '/BSc(Research) Physics': [116, 3, '/IIT Kanpur', 'Kanpur, UP', 'iitk.ac.in'], '/B.Management Studies': [117, 3, 'University of Delhi', 'Delhi, India', 'du.ac.in'], '/MBBS': [118, 5.5, '/AIIMS, Delhi', 'Ansari Nagar E, New Delhi', 'aiims.edu'], '/BDS': [119, 5, '/SGT University', 'Gurgaon, Haryana', 'sgtuniversity.ac.in'], '/BAMS': [120, 5.5,'/Banaras Hindu University', 'Varanasi, UP', 'bhu.ac.in'], '/BHMS': [121, 5.5, '/National Inst of Homeopathy', 'Kolkata, WB', 'nih.nic.in'], '/BYNS': [122, 4.5, '/GYNMCH', 'Arumbakkam, TN', 'gynmc.com'], '/LLB': [123, 3, '/NLSIU', 'Bangalore, Karnataka', 'nls.ac.in'], '/BBA': [124, 3, '/NMIMS', 'Vile Parle, Mumbai', 'nmims.edu'], '/BCom': [125, 3, '/GGS Indraprastha University', 'Dwaraka, Delhi', 'ipu.ac.in'], '/MFM(Finance)': [126, 2, '/JBIMS', 'Churchgate, Mumbai', 'jbims.edu'], '/BCA(Computer Appl)': [127, 3, 'BIT, Mesra', 'Ranchi, Jharkhand', 'bitmesra.ac.in'], '/BFM(Fashion)': [128, 3, '/NIFT, Chennai', 'Taramani, TN', 'nift.ac.in'], '/BA Psychology': [129, 3, '/Surana College', 'Basavanagudi, Karnataka', 'suranacollege.edu.in'], '/BHM': [130, 3, '/Oriental College of Hotel Mgmt', 'Wayanad, Kerala', 'orientalschool.com']}
                dkeys=list(d.keys())#List of dictionary keys
                dvalues=list(d.values())#List of dictionary values
                scname=input("Enter course name (Enter / before the name):")
                if scname in dkeys:
                    print(d[scname])
                else:
                    print("Course name invalid")

            elif ch1==4:
                d={'/ShivNadir University': [101, '/B.Tech(Chemical)', 4, 'Noida, UP', 'snu.edu.in'], '/SRM Easwari Eng College': [102, '/B.Tech(Civil)', 4, 'Ramapuram, Chennai', 'srmeaswari.ac.in'],  '/MIT, Manipal': [103, '/B.Tech(CS & Eng)', 4, 'Manipal, Karnataka', 'manipal.edu'], '/IIT-R': [104, '/B.Tech(Electrical & Electronics)', 4, 'Roorkee, UK, India', 'iitr.ac.in'],  '/BITS, Pilani': [105, '/B.Tech (Electronics & Comm)', 4, 'Pilani, Rajasthan', 'bits-pilani.ac.in'], '/IIT-Bombay': [106, '/B.Tech(Mechanical)', 4, 'Mumbai, Maharashtra', 'iitb.ac.in'], "/St.Stephen's College": [107, '/BA(Research) English', 3, 'New Delhi', 'ststephens.edu'], "/NIMS University": [108, '/BA(Research) History', 3, 'Jaipur, Rajasthan', 'nimsuniversity.org'], "/Adamas University": [109, '/BA(Research) Intl Relations', 3, 'Barasat, Kolkata', 'adamasuniversity.ac.in'], "/Loyola College": [110, '/BA(Research) Sociology', 3, 'Chennai, TN', 'loyolacollege.edu'], "/Christ University": [111, '/BA(Research) Economics', 3, 'Bangalore', 'christuniversity.in'], "/SSC, Kolkata": [112, '/BA(Research) Economics & Finance', 3, 'Kolkata, West Bengal', 'sivanathsastricollege.org'], "/PUCHD, Punjab": [113, '/BSc(Research) Biotechnology', 3,'Punjab, India' , 'puchd.ac.in'], "/Nizam College": [114, '/BSc(Research) Chemistry', 3, 'Hyderabad, India', 'nizamcollege.ac.in'], '/CMI, Chennai': [115, '/BSc(Research) Maths', 3, 'Siruseri, Chennai', 'cmi.ac.in'], '/IIT Kanpur': [116, '/BSc(Research) Physics', 3, 'Kanpur, UP', 'iitk.ac.in'], 'University of Delhi': [117, '/B.Management Studies', 3, 'Delhi, India', 'du.ac.in'], '/AIIMS, Delhi': [118, '/MBBS', 5.5, 'Ansari Nagar E, New Delhi', 'aiims.edu'], '/SGT University': [119, '/BDS', 5, 'Gurgaon, Haryana', 'sgtuniversity.ac.in'], '/Banaras Hindu University': [120, '/BAMS', 5.5,'Varanasi, UP', 'bhu.ac.in'], '/National Inst of Homeopathy': [121, '/BHMS', 5.5, 'Kolkata, WB', 'nih.nic.in'],  '/GYNMCH': [122, '/BYNS', 4.5, 'Arumbakkam, TN', 'gynmc.com'], '/NLSIU': [123, '/LLB', 3, 'Bangalore, Karnataka', 'nls.ac.in'], '/NMIMS': [124, '/BBA', 3, 'Vile Parle, Mumbai', 'nmims.edu'],  '/GGS Indraprastha University': [125, '/BCom', 3, 'Dwaraka, Delhi', 'ipu.ac.in'], '/JBIMS': [126, '/MFM(Finance)', 2, 'Churchgate, Mumbai', 'jbims.edu'], 'BIT, Mesra': [127, '/BCA(Computer Appl)', 3, 'Ranchi, Jharkhand', 'bitmesra.ac.in'], '/NIFT, Chennai': [128, '/BFM(Fashion)', 3, 'Taramani, TN', 'nift.ac.in'],  '/Surana College': [129, '/BA Psychology', 3, 'Basavanagudi, Karnataka', 'suranacollege.edu.in'], '/Oriental College of Hotel Mgmt': [130, '/BHM', 3, 'Wayanad, Kerala', 'orientalschool.com']}
                dkeys=list(d.keys())#List of dictionary keys
                dvalues=list(d.values())#List of dictionary values
                sccol=input("Enter college name(Enter / before the name):")
                if sccol in dkeys:
                    print(d[sccol])
                else:
                    print("College Name invalid")

            elif ch1==5:
                d={'Noida, UP': [101, '/B.Tech(Chemical)', 4, '/ShivNadir University', 'snu.edu.in'], 'Ramapuram, Chennai': [102, '/B.Tech(Civil)', 4, '/SRM Easwari Eng College', 'srmeaswari.ac.in'],  'Manipal, Karnataka': [103, '/B.Tech(CS & Eng)', 4, '/MIT, Manipal', 'manipal.edu'], 'Roorkee, UK, India': [104, '/B.Tech(Electrical & Electronics)', 4, '/IIT-R', 'iitr.ac.in'], 'Pilani, Rajasthan': [105, '/B.Tech (Electronics & Comm)', 4, '/BITS, Pilani', 'bits-pilani.ac.in'], 'Mumbai, Maharashtra': [106, '/B.Tech(Mechanical)', 4, '/IIT-Bombay', 'iitb.ac.in'], 'New Delhi': [107, '/BA(Research) English', 3, "/St.Stephen's College", 'ststephens.edu'], 'Jaipur, Rajasthan': [108, '/BA(Research) History', 3, "/NIMS University", 'nimsuniversity.org'], 'Barasat, Kolkata': [109, '/BA(Research) Intl Relations', 3, "/Adamas University", 'adamasuniversity.ac.in'], 'Chennai, TN': [110, '/BA(Research) Sociology', 3, "/Loyola College", 'loyolacollege.edu'], 'Bangalore': [111, '/BA(Research) Economics', 3, "/Christ University", 'christuniversity.in'], 'Kolkata, West Bengal': [112, '/BA(Research) Economics & Finance', 3, "/SSC, Kolkata", 'sivanathsastricollege.org'], 'Punjab, India': [113, '/BSc(Research) Biotechnology', 3, "/PUCHD, Punjab", 'puchd.ac.in'], 'Hyderabad, India': [114, '/BSc(Research) Chemistry', 3, "/Nizam College", 'nizamcollege.ac.in'], 'Siruseri, Chennai': [115, '/BSc(Research) Maths', 3, '/CMI, Chennai', 'cmi.ac.in'], 'Kanpur, UP': [116, '/BSc(Research) Physics', 3, '/IIT Kanpur', 'iitk.ac.in'], 'Delhi, India': [117, '/B.Management Studies', 3, 'University of Delhi', 'du.ac.in'], 'Ansari Nagar E, New Delhi': [118, '/MBBS', 5.5, '/AIIMS, Delhi', 'aiims.edu'], 'Gurgaon, Haryana': [119, '/BDS', 5, '/SGT University', 'sgtuniversity.ac.in'], 'Varanasi, UP': [120, '/BAMS', 5.5,'/Banaras Hindu University', 'bhu.ac.in'], 'Kolkata, WB': [121, '/BHMS', 5.5, '/National Inst of Homeopathy', 'nih.nic.in'], 'Arumbakkam, TN': [122, '/BYNS', 4.5, '/GYNMCH', 'gynmc.com'], 'Bangalore, Karnataka': [123, '/LLB', 3, '/NLSIU', 'nls.ac.in'], 'Vile Parle, Mumbai': [124, '/BBA', 3, '/NMIMS', 'nmims.edu'],  'Dwaraka, Delhi': [125, '/BCom', 3, '/GGS Indraprastha University', 'ipu.ac.in'], 'Churchgate, Mumbai': [126, '/MFM(Finance)', 2, '/JBIMS', 'jbims.edu'], 'Ranchi, Jharkhand': [127, '/BCA(Computer Appl)', 3, 'BIT, Mesra', 'bitmesra.ac.in'], 'Taramani, TN': [128, '/BFM(Fashion)', 3, '/NIFT, Chennai', 'nift.ac.in'], 'Basavanagudi, Karnataka': [129, '/BA Psychology', 3, '/Surana College', 'suranacollege.edu.in'], 'Wayanad, Kerala': [130, '/BHM', 3, '/Oriental College of Hotel Mgmt', 'orientalschool.com']}
                dkeys=list(d.keys())#List of dictionary keys
                dvalues=list(d.values())#List of dictionary values
                scloc=input("Enter EXACT Location:")
                for i in dkeys:
                    if scloc in i:
                        print(d[i])
                    else:
                        pass

            elif ch1==6:
                break
                

                
    elif ch==2:
        while True:
            print("\nCHOOSE YOUR CHOICE - 2")
            print("1. All subscriber details (Only admins can operate)")
            print("2. Want to become a subscriber")
            print("3. Search for your details using subscriber number")
            print("4. Search for your details using subscriber name")
            print("5. Check Subscriber Status")
            print("6. Check Newsletter Status")
            print("7. Back to Main Menu")
            ch2=int(input("Choose an option from the above:"))

            if ch2==1:
                admin=input("Enter user name:")#Username
                adminpw=int(input("Enter password:"))#Password
                if admin=='ADMIN':
                    if adminpw==123456:
                        print("Welcome Admin!!!")
                        sub={1001: ['ARUN', 'Registered', 'Success'], 1002: ['BHARATH', 'Registered', 'Success'], 1003: ['DINESH', 'Registered', 'Under Process'], 1004: ['GOWTHAM', 'Registered', 'Success'], 1005: ['HARISH', 'Registered', 'Under Process'], 1006: ['KARAN', 'Registered', 'Under Process'], 1007: ['MANOJ', 'Registered', 'Success'], 1008: ['PRAVIN', 'Registered', 'Under Process'], 1009: ['RAM', 'Registered', 'Success'], 1010: ['THARUN', 'Registered', 'Under Process']}
                        print(sub)
                    else:
                        print("Incorrect password")
                else:
                    print("Incorrect Username/Password")

            elif ch2==2:
                print("\n--------INSTRUCTIONS:---------------- \n1. Use BLOCK LETTERS\n2. Please don't add +91 in mobile number\n3. Enter 'Y' if you want to subscribe to news letter \n    Enter 'N' for NO newsletter subscription\n------------------------------------")
                import random
                number=random.randint(1011,1030)
                subname=input("\nEnter subscriber's name:")#Get subscriber's name
                subemail=input("Enter subscriber's email-id:")#Get subscriber's email
                while '@' not in subemail:
                    print("Enter proper email id")
                    subemail=input("Enter subscriber's email-id:")#Get subscriber's email
                else:
                    pass
                submob=int(input("Enter subscriber's mobile number(10 digits)"))#Get subscriber's mobile number
                subnews=input("Do you want to subscribe to our annual newsletter:")#Confirm for newsletter
                if subnews == 'Y':
                    print("\n THANK YOU FOR SUBSCRIBING TO OUR NEWS LETTER")
                    print("Subscriber number:", number)
                    print("You cannot search for your subscriber number immeadiately")
                    print("Your newsletter is under process")
                elif subnews == 'N':
                    print("\n THANK YOU FOR YOUR VALUABLE REPLY")
                else:
                    print("ERROR, TRY AGAIN LATER")

            elif ch2==3:
                print("\nSEARCH USING SUBSCRIBER NUMBER\n")
                ssno=int(input("Enter subscriber number:"))#Search using number
                dsubno={1001: ['ARUN', 'Registered', 'Success'], 1002: ['BHARATH', 'Registered', 'Success'], 1003: ['DINESH', 'Registered', 'Under Process'], 1004: ['GOWTHAM', 'Registered', 'Success'], 1005: ['HARISH', 'Registered', 'Under Process'], 1006: ['KARAN', 'Registered', 'Under Process'], 1007: ['MANOJ', 'Registered', 'Success'], 1008: ['PRAVIN', 'Registered', 'Under Process'], 1009: ['RAM', 'Registered', 'Success'], 1010: ['THARUN', 'Registered', 'Under Process']}#Dictionary of numbers
                subnos=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]#Keys in dsubno
                if ssno in subnos:
                    print(dsubno[ssno])
                else:
                    print("Wrong Subscriber number, try after sometime")

            elif ch2==4:
                print("\nSEARCH USING SUBSCRIBER NAME\n")
                ssname=input("Enter subscriber name: (Don't use quotes)")#Search using name
                dsubname={'ARUN': [1001, 'Registered', 'Success'], 'BHARATH': [1002, 'Registered', 'Success'], 'DINESH': [1003, 'Registered', 'Under Process'], 'GOWTHAM': [1004, 'Registered', 'Success'], 'HARISH': [1005, 'Registered', 'Under Process'], 'KARAN': [1006, 'Registered', 'Under Process'], 'MANOJ': [1007, 'Registered', 'Success'], 'PRAVIN': [1008, 'Registered', 'Under Process'], 'RAM': [1009, 'Registered', 'Success'], 'THARUN': [1010, 'Registered', 'Under Process']}#Dictionary of names
                subnames=['ARUN','BHARATH','DINESH','GOWTHAM','HARISH','KARAN','MANOJ','PRAVIN','RAM','THARUN']#Keys in dsubname
                if ssname in subnames:
                    print(dsubname[ssname])
                else:
                    print("Wrong Subscriber name, try after sometime")

            elif ch2==5:
                print("\nKNOW ABOUT SUBSCRIBER STATUS\n")
                ssno=int(input("Enter subscriber number:"))#Search using number
                dsubno={1001: ['ARUN', 'Registered', 'Success'], 1002: ['BHARATH', 'Registered', 'Success'], 1003: ['DINESH', 'Registered', 'Under Process'], 1004: ['GOWTHAM', 'Registered', 'Success'], 1005: ['HARISH', 'Registered', 'Under Process'], 1006: ['KARAN', 'Registered', 'Under Process'], 1007: ['MANOJ', 'Registered', 'Success'], 1008: ['PRAVIN', 'Registered', 'Under Process'], 1009: ['RAM', 'Registered', 'Success'], 1010: ['THARUN', 'Registered', 'Under Process']}#Dictionary of numbers
                subnos=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]#Keys in dsubno
                if ssno in subnos:
                    x=dsubno[ssno]#Get dictionary values as a list
                    print(x[1])
                else:
                    print("Wrong Subscriber number, try after sometime")

            elif ch2==6:
                print("\nKNOW ABOUT NEWSLETTER STATUS\n")
                ssno=int(input("Enter subscriber number:"))#Search using number
                dsubno={1001: ['ARUN', 'Registered', 'Success'], 1002: ['BHARATH', 'Registered', 'Success'], 1003: ['DINESH', 'Registered', 'Under Process'], 1004: ['GOWTHAM', 'Registered', 'Success'], 1005: ['HARISH', 'Registered', 'Under Process'], 1006: ['KARAN', 'Registered', 'Under Process'], 1007: ['MANOJ', 'Registered', 'Success'], 1008: ['PRAVIN', 'Registered', 'Under Process'], 1009: ['RAM', 'Registered', 'Success'], 1010: ['THARUN', 'Registered', 'Under Process']}#Dictionary of numbers
                subnos=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]#Keys in dsubno
                if ssno in subnos:
                    y=dsubno[ssno]#Get dictionary values as a list
                    print(y[2])
                else:
                    print("Wrong Subscriber number, try after sometime")

            elif ch2==7:
                break

            else:
                print("TRY AGAIN ! WRONG CHOICE !")
                break

                                
    elif ch==3:
        print("THANK YOU FOR YOUR VALUABLE TIME")
        print()
        break

    else:
        print("WRONG CHOICE")
