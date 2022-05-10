#Foong Wai Keat

#TP060033

#LIN YONG JING

#TP061039


#extra section

#emergency create admin account through customer registration option if no accounts exits in username.txt

def emergency1(): #define emergency1 function
    tfile = open('Username.txt', 'r') #open username text file
    if tfile.read() == '': #if the contents of the file readed is nothing then add deatils of admin account to list
        tfile.close()
        print('\n')
        xfile = open('Username.txt', 'a')
        admin = ['1', 'admin', 'admin', 'admin', '0', 'admin', '0000000000', '0000000000000000', 'admin', 'Admin']

        for infos in admin: #add infos of admin account from list into username file
            xfile.write(infos)
            xfile.write("\t")
        xfile.write("\n")
        xfile.close()
        print('An admin account have been created with the details below:.') #print default username and password for admin account
        print('Admin account:\nUsername:\tadmin\nPassword:\tadmin')
        print('Please try to login with the created admin account.')
        print('')
    else: #if username have account then execute customercreatemember function
        return customercreatemember()

#emergency create admin account through login option if no accounts exits in username.txt

def emergency0(): #define emergency0 function
    tfile = open('Username.txt', 'r') #open username text file
    if tfile.read() == '': #if the contents of the file readed is nothing then add deatils of admin account to list
        tfile.close()
        print('\n')
        xfile = open('Username.txt', 'a') #add infos of admin account from list into username file
        admin = ['1', 'admin', 'admin', 'admin', '0', 'admin', '0000000000', '0000000000000000', 'admin', 'Admin']

        for infos in admin: #add infos of admin account from list into username file
            xfile.write(infos)
            xfile.write("\t")
        xfile.write("\n")
        xfile.close()
        print('An admin account have been created with the details below:.') #print default username and password for admin account
        print('Admin account:\nUsername:\tadmin\nPassword:\tadmin')
        print('Please try to login with the created admin account.')
        print('')

#ensure car plate don't repeat

def test002(): #define test002 function

    file = open('Cars.txt', 'r')  #open cars text file

    try: #validation for invalid input and errors
        carplate = str(input("Please enter Car Plate:\t ")) #accept user input of car plate

        for details in file:
            details = details.split("\t")
            if (carplate == details[1]): #compare the user input with all car plates in cars text file
                print('Sorry Car Plate exists in record.\nPlease use another Car Plate.')
                return test002() #rerun test002 function to ask user to enter another car plate
            else:
                continue

        return carplate #return the value of carplate
    except:
        print('Invalid input.\nPlease try again.')


#member return to member menu

def memberreturn(): #define memberretuen function

    try: #validatetion for any error

        returnkey = input("Enter \'m\' return to Menu or enter \'p\' to proceed: ") #accept user input, either m or p
        returnkey = returnkey.lower() #turn user input of 'M' or 'P' in capital into lowercase

    except:
        print('Invalid input.\nPlease try again.')
        return memberreturn() #call emberreturn function if any error occurs due to invalid input or so on

    for i in returnkey: #for loop the user input and apply flag by returning the value of 0 or 1 based on the input
        if returnkey == "m":
            return 0
            break
        elif returnkey == 'p':
            return 1
            continue
        else: #if not m or p
            print('Sorry, option not available.\n Please try again')
            return 0
            break

#rent section

#enter date

def stime(): #define stime function
    try: #validate any error

        import datetime #import datetime to allow datetime to be used in function

        # inform customers about the rules of setting up the booking date

        print('\n')
        print('Please enter the year, month, day, time and minutes which starts car rental service.')
        print('Booking service in only available within a week starting from the current time.')
        print('The maximum duration to rent a car is 1 week (168 hours)')

        # create variable of now in string = current time (have year, month, day, hours, minutes, seconds and microseconds

        now=str(datetime.datetime.now())

        # print current time in year, month, day, hours, minutes, seconds, miroseconds removed by slicing string [:19]

        print('Time now is:\t',now[:19])

        # ask user enter year, month, day, hours in 24 hour format, minutes

        y = int(input('Enter the year:\t'))
        mo = int(input('Enter the month:\t'))
        d = int(input('Enter the day:\t'))
        h = int(input('Enter the hour in 24 hour format:\t'))
        mi = int(input('Enter the minutes:\t'))

        # create variable of starttime = user input year, month, day, hours in 24 hour format, minutes

        starttime = datetime.datetime(y, mo, d, h, mi)

        # create variable of b to minus time in seconds for validation

        b = 1
        c = starttime - datetime.timedelta(seconds=b)

        # create variable of hours to limit time entered does not execed 1 week time limit

        hours = 168
        renthours = datetime.timedelta(hours=hours)

        endrent = starttime + renthours

        #print(starttime)
        #print(c)
        #print(endrent)

        # validate time input is not in the past and does not execed 1 week time limit

        if c < starttime < endrent:
            if starttime>datetime.datetime.now(): #validate time input  does not execed current time
                endrent = str(endrent)
                startrent = starttime
                c = str(c)
                return starttime #return value of starttime
            else:
                print('Invalid time input.\nPlease try again.')
                return stime() #rerun stime() by calling it again if have error

    except:
        print('Invalid input.\nPlease try again.')
        return stime()


#auto generate record id

def recordno(): #define recordno function
    nofile = open("Records.txt", "r") #open record text file in read mode
    record = [] #create record list
    for record in nofile: #remove blank space, split details in record file, add into record list
        record = record.rstrip()
        record = record.split('\t')
        record.append(record) #add records into list
        #print(len(carno)) #checker

    x = len(record) #create variable x = number of items in record list
    recordno =1
    #print(cars[x-1][0]+1)

    if not x: #if list (file) is empty, set recordno=1
        recordno=1
    else: #if list (file) is not empty, declare recordno = largest nuber of current list +1
        recordno=int(record[x-1][0])+1
    #print(newestcarno)
    return recordno #return value of recordno

#rent car
def rent(): #declare rent function
    try: #validate error
        import time
        import datetime #allow datetime could be used in function
        from datetime import date
        print('-'*50, 'Rent Car','-'*50) #print function title

        #confirm user
        mfile = open('Username.txt', 'r') #open username text file in read mode
        username = input('Please enter Username:\t ') #accept user input (username and password)
        password = input('Please enter Password:\t ')
        flag =0 #set original value of flag = 0

        for infos in mfile: #remove blank space and seperate infos with tab
            infos = infos.rstrip()
            infos = infos.split('\t')
            if username == infos[1]: #compare the user input to confirm user, after confirmed, value of flag = 1
                if password == infos[5]:
                    print("User Confirmed")
                    flag = 1
                    break
                else:
                    break
            else:
                continue

        if flag==1: #when flag is 1 (user confirmed)

            tfile = open("Cars.txt", "r") #open car file in read mode
            edit = [] #blank list
            print("-" * 45, "Car Rent", "-" * 45)
            no = 1

            for details in tfile:
                details = details.rstrip()  # remove empty space
                details = details.split("\t") #split deatils with tab,(\t)

                print(details[0], ".", details[2], details[3], details[4], details[5], details[6], details[7],
                          details[9],
                          details[10])  # print details in cars file
                edit.append(details) #add all details from cars file to 'edit' list

            if memberreturn()==1: #when member confirm to proceed to rent car
                no_ofcar = int(input("Choose No. of car to rent:\t")) #accept input (which car to rent from user)
                no_ofcar = no_ofcar - 1 #as the 1st box in python starts from zero but normally people enter 1 for the first box, so user input-1

                price = float(edit[no_ofcar][10]) #make the contents of 10th box of users's choice of car to be 'price'
                cid=edit[no_ofcar][0] #make the contents of 0th box of users's choice of car to be 'car id'
                cplate= edit[no_ofcar][1] #make the contents of 1st box of users's choice of car to be 'car plate'
                status=edit[no_ofcar][9]

                if status!='Available': #stop user from renting car if car is not available
                    print('Sorry, the car is currently not available.\n Please choose another car which is available.')
                    return rent()

                hours = int(input("Please enter the amount of hours to rent the car:\t "))

                if hours>168 or hours<0: #ensure user does not enter hours which exceed 1 week
                    print('The maximum duration to rent a car is 168 hours (1 week).\nPlease try again.')
                else:
                    a = stime() #declare a=value returned by stime function
                    afile=open('Cars.txt','a') #open cars test file in add infos mode
                    finalconfirm=str(input('Please confirm with you booking by entering \'Confirm\' or \'Not Confirm\':\t')) #double confirm withe user to rent the car
                    finalconfirm=finalconfirm.lower() #turn user input into lowercase the uppercase for first letter and declare it into 'confirmation'
                    finalconfirm=finalconfirm.title()
                    confirmation=finalconfirm
                    if confirmation=='Confirm': #if user confirm, change the status of car into not available
                        state = str('Not Available')
                        edit[no_ofcar][9] = state
                        filemcgv = open("Cars.txt", "w")
                        for car in edit:
                            for info in car:
                                filemcgv.write(info)
                                filemcgv.write('\t')
                            filemcgv.write('\n')
                        filemcgv.close()
                        print(edit[no_ofcar])

                    elif confirmation=='Not confirm': #bring user to rent title again by calling rent function
                        return rent()
                    else:
                        print('Sorry, please enter only \'Confirm\' or \'Not Confirm\'.') #limit user input into confirm or not confirm
                        return rent()

                    p=datetime.timedelta(hours=hours) #declare p=user entered hours


                    endrent = a + p #declare time for rent to end (endrent) as time userstarts renting+rent hours

                    usageperiod = hours #declre hours into car usage time (usageperiod)

                    usageperiod=str(usageperiod) #change usageperiod, end rent into string type to remove microsecond

                    endrent = str(endrent)

                    totalamount = price * int(usageperiod) #declare total amount as price * usage period in integer form

                    # declare variable and remove microsecond for endrent and str(a)

                    e = endrent[:19]
                    a=str(a)
                    a=a[:19]

                    print('Time which car rent starts:\t ', a) #print renting details
                    print('Time which car rent ends:\t ', e)
                    print('Total time:\t', p)
                    print('Total amount:\t ', totalamount)
                    print('\n')
                    print('Thank you for using our service.\nPlease stay safe and enjoy you ride.')

                    #record = [userIDMain,userFirstNameMain,userLastNameMain,cid,cplate,startrent,e,price,renthours,totalamount]

                    sfile = open('Records.txt', 'a') #open records file in append mode and add rent details into it
                    recordid=recordno()
                    record = [recordid, infos[0], infos[2], infos[3],cid,cplate,a,e,price,usageperiod,totalamount]
                    for infos in record:
                        infos=str(infos)
                        sfile.write(infos)
                        sfile.write('\t')
                    sfile.write('\n')
                    sfile.close() #close record file
        else:
            print('Wrong Username or Password.\nPlease try again.')
    except:
        print('Invalid input is found.\nPlease try again.')





#record section

#view records

def viewrecords(): #define view records function
    vfile=open('Records.txt','r') #open records text file in read only mode
    print("-" * 45, "Cars Record History", "-" * 45) #print function title
    list = [] #create empty list
    no = 1
    for records in vfile: #remove blank space, seperate with tab and app infos in file into list and print it
        records = records.rstrip()
        records = records.split('\t')
        list.append(records)
        ulist = (records[0], records[1],records[2], records[3], records[4], records[5], records[6], records[7], records[8], records[9],records[10])

        print('Record ID:\t', records[0])
        print('Member ID:', records[1])
        print('Member First Name:', records[2])
        print('Member Last name:', records[3])
        print('Car ID:', records[4])
        print('Car Plate No.:', records[5])
        print('Start Time:', records[6])
        print('End Time:', records[7])
        print('Car Rent (RM):', records[8])
        print('Total Hours:', records[9])
        print('Total Car Rent (RM):', records[10])
        print('\r')

        #print(ulist)
    no = no + 1
    vfile.close() #close file


#view personal records

def viewpersonalhistory(): #define viewpersonalhistory function
    try: #validation for errors
        print('-'*50, 'Rent Car History','-'*50) #print function title

        ememberno = str(midforother()) #use the returned value from midfother function (member id function) to get member id
        rfile = open("Records.txt", "r") #open files in read only mode
        flag=0
        for infos in rfile: #remove blank space, seperate with tab and app infos in file into list and close file
            infos = infos.rstrip()
            infos = infos.split("\t")
            if ememberno == infos[1]:
                print('\n')
                print('Record ID:\t', infos[0])
                print('Member ID:', infos[1])
                print('Member First Name:', infos[2])
                print('Member Last name:', infos[3])
                print('Car ID:', infos[4])
                print('Car Plate No.:', infos[5])
                print('Start Time:', infos[6])
                print('End Time:', infos[7])
                print('Car Rent (RM):', infos[8])
                print('Total Hours:', infos[9])
                print('Total Car Rent (RM):', infos[10])
                print('\n')
                flag=flag+1
        if flag==0:
            print('Sorry no records are found, this may due to no record exists for your account.')

        rfile.close() #close file

        #print(list[ememberno][0], list[ememberno][1], list[ememberno][2], list[ememberno][3], list[ememberno][4],list[ememberno][5], list[ememberno][6], list[ememberno][7], list[ememberno][8],list[ememberno][9],list[ememberno][10])

    except:
        print('Sorry no records are found, this may due to no record exists for your account.')


#search record

def searchrecord(): #define searchrecord function

    try:
        searchrecords=str(input("Please enter Record ID:\t ")) #accept user input
        filemcgv=open("Records.txt","r") #open records text file in read mode
        rno=1
        for details in filemcgv:
            details =details.split("\t")
            if (searchrecords in details[0]): #if member id is same with user input the print details of record
                print('\n')
                print("Record ID:\t ", details[0])
                print("Member ID:\t ", details[1])
                print("Member First Name:\t ", details[2])
                print("Member Last Name:\t ", details[3])
                print("Car ID:\t ", details[4])
                print("Car Plate No.:\t ", details[5])
                print("Start Time:\t ", details[6])
                print("End Time:\t ", details[7])
                print("Car Rent per hour (RM):\t ", details[8])
                print("Hours Rent:\t ", details[9])
                print("Total Amount (RM):\t ", details[10])
                #print(details[0],". ", details[2],details[3],details[4],details[5],details[6],details[7], details[8], details[9])
                #print(rno,". ",details[0], details[1],details[2],details[3],details[4],details[5],details[6],details[7], details[8], details[9],end="")
                rno = rno + 1

            else:
                continue
        if (rno == 1): #if no records in records file the infrm no records in file
            print("Sorry record does not exist.")
            print("Please ensure the right Record ID.")
        filemcgv.close()


    except:
        print('Invalid input.\n Please try again.')



#car section

#delete car

def deletecar(): #define deletecar function
    filemcgv = open("Cars.txt", "r") #open car text file in read mode
    edit = []
    no = 1

    print("-" * 45, "Delete Cars", "-" * 45) #print function title
    for details in filemcgv:
        details = details.rstrip()  # remove empty space, seperate details in file and print details in file
        details = details.split("\t")

        print("1.\tCar ID:\t ", details[0])
        print("2.\tCar Plate:\t ", details[1])
        print("3.\tCar Brand:\t ", details[2])
        print("4.\tCar Model:\t ", details[3])
        print("5.\tCar Colour:\t ", details[4])
        print("6.\tNumber of Seats:\t ", details[5])
        print("7.\tType of Car :\t ", details[6])
        print("8.\tAvailability of Car :\t ", details[9])
        print("9.\tRental per hour (RM):\t ", details[10])
        print('\n')

        # print(details[0], ".",details[1],details[2],details[3],details[4],details[5],details[6],details[7],details[8],details[9],details[10])
        # print(no,".",details[0])
        edit.append(details) #add details in file to list
        no = no + 1

    filemcgv.close() #close file

    try:
        no_ofcar = int(input("Choose ID of Car to be deleted:\t")) #accept user input
        no_ofcar = no_ofcar - 1 #user input -1 due to concept of array (start from 0)

        edit.pop(no_ofcar) #delete details based on user input
        filemcgv = open("Cars.txt", "w") #open car text fie and remove details from file
        for car in edit:
            for info in car:
                filemcgv.write(info)
                filemcgv.write('\t')
            filemcgv.write('\n')
        filemcgv.close()
        print('Car have been deleted.')

    except:
        print('Invalid input.\nPlease try again')

# admin edit car
def editcargallery(): #define editcargallery function
    filemcgv = open("Cars.txt", "r") #open cars text file and create 'edit' list and 'validate' list
    edit = []
    validate=[]
    no = 1

    print("-" * 50, "Edit Cars Gallery", "-" * 50) #print function title
    for details in filemcgv:
        details = details.rstrip() #remove empty space, seperate with tab and print details in file
        details=details.split("\t")
        print('\n')
        print('Car No:\t', no)
        print("1.\tCar ID:\t ", details[0])
        print("2.\tCar Plate:\t ", details[1])
        print("3.\tCar Brand:\t ", details[2])
        print("4.\tCar Model:\t ", details[3])
        print("5.\tCar Colour:\t ", details[4])
        print("6.\tNumber of Seats:\t ", details[5])
        print("7.\tType of Car:\t ", details[6])
        print("8.\tCar Production Year:\t ", details[7])
        print("9.\tRoad Tax Due Date:\t ", details[8])
        print("10.\tAvailability of Car:\t ", details[9])
        print("11.\tRental per hour (RM):\t ", details[10])



        #print(details[0], ".",details[1],details[2],details[3],details[4],details[5],details[6],details[7],details[8],details[9],details[10])
        #print(no,".",details[0])
        edit.append(details) #add details into 'edit' list
        no = no + 1

    filemcgv.close() #close file

    try: #validate errors
        print('\n')
        no_ofcar=int(input("Choose number of car for changes to be made: ")) #accept user input and user input-1
        no_ofcar=no_ofcar-1

        for infos in edit:
            if no_ofcar + 1 == int(infos[0]): #if user input+1 = car id the add info into 'validate' list
                validate.append(infos)

        if not validate: #if validate list is empty, call editcargallery function
            print("Car does not exist, Please try again")
            return editcargallery()

        field = int(input('Please enter field to changes to be made:\t')) #accept user input for field and -1 user input
        field = field - 1

        if field > 10 or field < 0: #limit input within range of available fields or else call editcargallery function
            print('Sorry no such field.\nPlease try again.')
            return editcargallery()

        # edit car id
        if field==0: #if user input=0
            ncarid = input("Please enter new Car ID:\t ") #accept user input and replace the previous details in the file of the selected car
            edit[no_ofcar][field] = ncarid
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==1: #if user input=1

            #edit car plate
            nplate=str(test002()) #call test002 function to ensure no similar car plate and convert into string
            nplate=nplate.upper() #uppercare all strings as car plates are in uppercase
            edit[no_ofcar][field]=nplate
            filemcgv = open("Cars.txt", "w") #open file,use returned value from test002() replace the previous details in the file of the selected car
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==2: #if user input=2

            # edit car brand
            ncarbrand = input("Please enter new Car Brand:\t ") #accept user input and replace the previous details in the file of the selected car
            ncarbrand=ncarbrand.title()
            edit[no_ofcar][field] = ncarbrand
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==3: #if user input =3

            #edit car model
            nmodel=input("Please enter new Car Model:\t ") #accept user input and replace the previous details in the file of the selected car
            nmodel=nmodel.title()
            edit[no_ofcar][field]=nmodel
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==4: #if user input=4
            #edit car colour
            ncolour=input("Please enter new Car Colour:\t ") #accept user input and replace the previous details in the file of the selected car
            ncolour=ncolour.upper()
            edit[no_ofcar][field]=ncolour
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==5: #if user input =5

            #edit No of car seat
            nseat=input("Please enter the new No of Car Seats:\t ") #accept user input and replace the previous details in the file of the selected car
            edit[no_ofcar][field]=nseat
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==6: #if user input =6

            #edit car type
            ntype=input("Please enter new Car Type:\t ") #accept user input and replace the previous details in the file of the selected car
            ntype=ntype.upper()
            edit[no_ofcar][field]=ntype
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==7: #if user input =7

            #edit car production date
            ndate = input("Please enter new Car Production Date:\t ") #accept user input and replace the previous details in the file of the selected car
            edit[no_ofcar][field] = ndate
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==8: #if user input=8

            #edit the car road tax due date
            ntax = input("Please enter new Car Road Tax Due Date:\t ") #accept user input and replace the previous details in the file of the selected car
            edit[no_ofcar][field] = ntax
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==9: #if user input =9 then allow admiin to change the returned car into available

            #edit car availbility
            nstate=str(input("Edit availability of car \'Available\' or \'Not Available\':\t ")) #accept user input and replace the previous details in the file of the selected car
            nstate=nstate.lower()
            nstate=nstate.title()
            #print(nstate)

            while (nstate=='Available') or (nstate=='Not Available'):  #limite input to be Availabl or not available only
                break
            else:
                print('Invalid input.\nPlease try again.')
                return editcargallery()

            edit[no_ofcar][field] = nstate
            filemcgv=open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


        elif field==10: #if user input =10

            #edit rental price of car per hour

            price = str(input("Edit rental price of car per hour (RM):\t ")) #accept user input and replace the previous details in the file of the selected car
            edit[no_ofcar][field] = price
            filemcgv = open("Cars.txt", "w")
            for car in edit:
                for info in car:
                    filemcgv.write(info)
                    filemcgv.write('\t')
                filemcgv.write('\n')
            filemcgv.close()
            print(edit[no_ofcar])


    except:
        print('Invalid input.\nPlease try again')


#search cars

def searchCar(): #define search car function
    try:
        searchcarid=str(input("Please enter Car ID:\t ")) #accept user input
        filemcgv=open("Cars.txt","r") #open cars text file, seperate with tab and print details in file
        carno=1
        for details in filemcgv:
            details =details.split("\t")
            if (searchcarid in details[0]):
                print('\n')
                print("Car No:\t ", details[0])
                print("Car Plate:\t ", details[1])
                print("Car Brand:\t ", details[2])
                print("Car Model:\t ", details[3])
                print("Car Colour:\t ", details[4])
                print("Number of Seats:\t ", details[5])
                print("Type of Car :\t ", details[6])
                print("Car Production Year:\t ", details[7])
                print("Road Tax Due Date:\t ", details[8])
                print("Availability of Car :\t ", details[9])
                print("Rental per hour (RM):\t ", details[10])
                #print(details[0],". ", details[2],details[3],details[4],details[5],details[6],details[7], details[8], details[9])
                #print(carno,". ",details[0], details[1],details[2],details[3],details[4],details[5],details[6],details[7], details[8], details[9],end="")
                carno = carno + 1

            else:
                continue
        if (carno == 1): #if no cars in file
            print("Sorry car does not exist.")
            print("Please ensure the right car ID is entered.")
        filemcgv.close()


    except:
        print('Invalid input.\n Please try again.')


#auto generate carno

def carno(): #define carno function
    nofile = open("Cars.txt", "r") #open car text file in read mode, remove spaces and seperate with tab
    cars = []
    for carno in nofile:
        carno = carno.rstrip()
        carno = carno.split('\t')
        cars.append(carno)#ok
        #print(len(carno)) #checker

    x = len(cars) #declare x=number of items in 'cars' list
    newestcarno =1
    #print(cars[x-1][0]+1)

    if not x: #if list is empty, declare newestcarno=1, or else declare newestcarno=largest number of car id +1
        newestcarno=1
    else:
        newestcarno=int(cars[x-1][0])+1
    #print(newestcarno)
    return newestcarno #return value of newestcarno

#admin add car
def adminaddcar(): #define adminaddcar function
    try:
        carsno=str(carno()) #declare carsno=returned value of carno function
        carid=str(test002()) #declare carid=returned value of test002 function and make into uppercase
        carid=carid.upper()
        carbrand=str(input("Enter Car Brand:\t ")) #accept user input
        carbrand=carbrand.title()
        carmodel=str(input("Enter Car Model:\t "))
        carmodel=carmodel.title()
        carcolour=str(input("Enter Car Colour:\t "))
        carcolour=carcolour.upper()
        numberofseats=str(input("Enter No. of Car Seats:\t "))
        typeofcar=str(input("Enter Car Type:\t "))
        typeofcar=typeofcar.upper()
        productiondate=str(input("Enter Car Production Date:\t "))
        roadtaxduedate=str(input("Enter Road Tax Due Date of Car:\t "))
        carstatus=str(input("Enter Car Status \'Available\' or \'Not Available\':\t "))
        carstatus=carstatus.lower()
        carstatus=carstatus.title()

        if carstatus!='Available'and carstatus!='Not Available': #limit user input into available and not available only
            print('Invalid input.\nPlease try again.')
            return adminaddcar()

        carprice=input("Enter the price to rent the car in 1 hour (RM):\t ")


        filemcgv=open('Cars.txt','a') #open cars text file in append mode (add)

        carinfo=[carsno,carid, carbrand, carmodel, carcolour, numberofseats, typeofcar, productiondate, roadtaxduedate, carstatus, carprice]

        for infos in carinfo: #add contents in list to file
            filemcgv.write(infos)
            filemcgv.write('\t')
        filemcgv.write('\n')
        filemcgv.close() #close file


    except:
        print('Invalid input.\nPlease try again.')



#view all cars (mm)

def viewcargallery(): #define view car gallery function (for main menu)
    filemcgv=open("Cars.txt","r") #open car text file in read mode
    print("-"*45, "Cars Gallery", "-"*45) #print title of function
    no=1
    for details in filemcgv: #seperate with tab and print out details
        details=details.split("\t")
        print("Car Brand:\t ", details[2])
        print("Car Model:\t ", details[3])
        print("Car Colour:\t ", details[4])
        print("Number of Seats:\t ", details[5])
        print("Type of Car :\t ", details[6])
        print("Availability of Car :\t ", details[9])
        print("Rental per hour (RM):\t ", details[10])

        no = no+1
    filemcgv.close() #close file

#view all cars (member)

def viewcargallerym(): #define view car gallery function (for member)

    filemcgv=open("Cars.txt","r") #open car text file in read mode
    print("-"*45, "Cars Gallery", "-"*45) #print title of function
    no=1
    for details in filemcgv: #seperate with tab and print out details
        details=details.split("\t")
        print('\n')
        print("Car Brand:\t ", details[2])
        print("Car Model:\t ", details[3])
        print("Car Colour:\t ", details[4])
        print("Number of Seats:\t ", details[5])
        print("Type of Car :\t ", details[6])
        print("Availability of Car :\t ", details[9])
        print("Rental per hour (RM):\t ", details[10])

        no = no+1
    filemcgv.close() #close file

#view all cars (admin)

def viewcargallerya(): #define view car gallery function (for admin)
    filemcgv=open("Cars.txt","r") #open car text file in read mode
    print("-"*45, "Cars Gallery", "-"*45) #print title of function
    no=1
    for details in filemcgv: #seperate with tab and print out details
        details=details.split("\t")
        print('\n')
        print("Car ID:\t ", details[0])
        print("Car Brand:\t ", details[2])
        print("Car Model:\t ", details[3])
        print("Car Colour:\t ", details[4])
        print("Number of Seats:\t ", details[5])
        print("Type of Car :\t ", details[6])
        print("Availability of Car :\t ", details[9])
        print("Rental per hour (RM):\t ", details[10])

        no = no+1
    filemcgv.close() #close file


#member section

#return member id
def midforother(): #define midforother function
    mfile = open('Username.txt', 'r') #open username text file in read mode
    record = []
    username = input('Please enter Username:\t ') #accept username and pass word to return vale of member id
    password = input('Please enter Password:\t ')

    for infos in mfile:
        infos = infos.rstrip()
        infos = infos.split('\t')
        if username == infos[1]:
            if password == infos[5]: #if username and password are samw the return member id for the username and password
                print("User Confirmed")
                userIDMain = infos[0]
                return userIDMain
            else:
                break
        else:
            continue

# delete member function

def deletemember(): #define deletemember function
    filemcgv = open("Username.txt", "r") #open username text file in read mode
    edit = [] #create empty list 'edit'
    no = 1

    print("-" * 45, "Delete Member", "-" * 45) #print title of function
    for infos in filemcgv:
        infos = infos.rstrip()  # remove empty space, separate with tab and print usernames in file
        infos = infos.split("\t")

        print("Member ID:\t", infos[0])
        print("Username:\t", infos[1])
        print("First name:\t", infos[2])
        print("Last name:\t", infos[3])
        print("Email:\t", infos[4])
        print('Password:\t', infos[5])
        print("Telephone No.:\t", infos[6])
        print("Bank Card No.:\t", infos[7])
        print("Bank Card Password:\t", infos[8])
        print('\n')

        edit.append(infos) #add details of each user in file into list
        no = no + 1

    filemcgv.close() #close file

    try:
        no_ofmember = int(input("Choose ID of Member to be deleted:\t")) #accept user input
        no_ofmember = no_ofmember - 1 #user input-1 due to array start from 0

        edit.pop(no_ofmember) #use input to decide which user i username file to delete
        filemcgv = open("Username.txt", "w") #open file in write mode
        for car in edit:
            for info in car:
                filemcgv.write(info)
                filemcgv.write('\t')
            filemcgv.write('\n')
        filemcgv.close() #close file
        print('Username have been deleted.') #inform delete is done

    except:
        print('Invalid input.\nPlease try again.')



# member edit personal info

def membereditinfo(): #define membereditinfo function
    try: #validate any error
        filem = open("Username.txt", "r") #open username text file in read mode
        medit = [] #create 'medit' empty list
        print("-" * 50, 'Edit Member', '-' * 50) #print title of function
        num = 1
        for infos in filem: #remove blank spaces of details in username file, seperate with tab and add into medit list
            infos = infos.rstrip()
            infos = infos.split("\t")
            medit.append(infos)
            num = num + 1

        filem.close() #close file

        # Edit member info
        ememberno=int(midforother()) #call midforother function and user the returned value (member id)
        ememberno = ememberno - 1 #due to array start from 0, so user input -1

        print('\n') #print infos of member based on member id
        print("1.\tUsername:\t", medit[ememberno][1])
        print("2.\tFirst name:\t", medit[ememberno][2])
        print("3.\tLast name:\t",  medit[ememberno][3])
        print("4.\tEmail:\t", medit[ememberno][4])
        print('5.\tPassword:\t', medit[ememberno][5])
        print("6.\tTelephone No.:\t", medit[ememberno][6])
        print("7.\tBank Card No.:\t", medit[ememberno][7])
        print("8.\tBank Card Password:\t", medit[ememberno][8])
        print('\n')

        #print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2], medit[ememberno][3],
        # medit[ememberno][4], medit[ememberno][5], medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])

        if memberreturn() == 1: #if the returned valus is 1 (flag) then continue

            field=int(input('Please enter field to changes to be made:\t')) #accept user input for field

            if field>8 or field<0: #limit the range of numbers intered into field to 1 to 8 or else rerun membereditinfo function
                print('Sorry no such field.\nPlease try again.')
                return membereditinfo()

            if field==0: #to avoid member from editing their member id, if user enter 0, it will become 1
                field=field+1

            if field==1:  #if user input is 1
                # edit username
                nusername = input("Please enter new Username:\t ") #accept user input
                medit[ememberno][field] = nusername
                filem = open('Username.txt', 'w') #open username text file in write mode to replace old data
                for member in medit:
                    for infos in member: #replace the datas in file with user input
                        filem.write(infos)
                        filem.write("\t")
                    filem.write('\n')
                filem.close() #close file
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2], #print new member details
                            medit[ememberno][3],medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])


            elif field == 2: #if user input is 2

                # edit firstname
                nfirstname = input("Please enter new First Name:\t ")
                medit[ememberno][field] = nfirstname
                filem = open('Username.txt', 'w')
                for member in medit:
                    for infos in member:
                        filem.write(infos)
                        filem.write('\t')
                    filem.write("\n")
                filem.close()
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2],
                            medit[ememberno][3], medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])

                #print(medit[ememberno])
                #print(medit)

            elif field == 3: #if user input is 3

                # edit last name
                nlastname = str(input("Please enter new Last Name:\t "))
                medit[ememberno][field] = nlastname
                filem = open('Username.txt', 'w')
                for member in medit:
                    for infos in member:
                        filem.write(infos)
                        filem.write('\t')
                    filem.write('\n')
                filem.close()
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2],
                            medit[ememberno][3], medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])

                #print(medit)

            elif field == 4: #if user input is 4

                # edit email
                nemail = input("Please enter new Email:\t ")
                medit[ememberno][field] = nemail
                filem = open('Username.txt', 'w')
                for member in medit:
                    for infos in member:
                        filem.write(infos)
                        filem.write('\t')
                    filem.write('\n')
                filem.close()
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2],
                            medit[ememberno][3], medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])

                #print(medit)

            elif field == 5: #if user input is 5
                #edit password
                npassword = input("Please enter new Password:\t ")
                medit[ememberno][field] = npassword
                filem = open('Username.txt', 'w')
                for member in medit:
                    for infos in member:
                        filem.write(infos)
                        filem.write('\t')
                    filem.write('\n')
                filem.close()
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2],
                            medit[ememberno][3], medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])

                #print(medit)

            elif field == 6: #if user input is 6

                # edit telephone
                ntelephoneno = input("Please enter new Telephone Number:\t ")

                if (len(ntelephoneno) != 10):
                    print('Please enter telephone number again in 10 digits.')
                    return membereditinfo()

                medit[ememberno][field] = ntelephoneno
                filem = open('Username.txt', 'w')
                for member in medit:
                    for infos in member:
                        filem.write(infos)
                        filem.write('\t')
                    filem.write('\n')
                filem.close()
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2],
                            medit[ememberno][3], medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])

                #print(medit)

            elif field == 7: #if user input is 7

                #edit bank card number
                ncard = input("Please enter new Bank Card No.:\t ")

                if (len(ncard) != 16):
                    print('Please enter Bank Card Number again in 16 digits')
                    return membereditinfo()

                medit[ememberno][field] = ncard
                filem = open('Username.txt', 'w')
                for member in medit:
                    for infos in member:
                        filem.write(infos)
                        filem.write('\t')
                    filem.write('\n')
                filem.close()
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2],
                            medit[ememberno][3], medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])

                #print(medit)

            elif field == 8: #if user input is 8

                #edit bank card password
                ncardp = input("Please enter new Bank Card Password:\t ")
                medit[ememberno][field] = ncardp
                filem = open('Username.txt', 'w')
                for member in medit:
                    for infos in member:
                        filem.write(infos)
                        filem.write('\t')
                    filem.write('\n')
                filem.close()
                print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2],
                            medit[ememberno][3], medit[ememberno][4], medit[ememberno][5],
                            medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])


    except:
        print('Invalid input\nPlease try again.')



#admin edit member

def admineditmember(): #define admineditmember function

    filem = open("Username.txt", "r") #open username text file in read mode
    medit = [] #create empty list of 'medit', and 'validate'
    validate=[]
    print("-"*50, 'Edit Member', '-'*50) #print title of function
    num = 1
    for infos in filem: #remove blank space and seperate with tab and print user details
        infos = infos.rstrip()
        infos = infos.split("\t")
        print('\n')
        print('Member No:\t', num)
        print("1.\tMember ID:\t", infos[0])
        print("2.\tUsername:\t", infos[1])
        print("3.\tFirst name:\t", infos[2])
        print("4.\tLast name:\t", infos[3])
        print("5.\tEmail:\t", infos[4])
        print('6.\tPassword:\t', infos[5])
        print("7.\tTelephone No.:\t", infos[6])
        print("8.\tBank Card No.:\t", infos[7])
        print("9.\tBank Card Password:\t", infos[8])
        #print(infos[0], ".", infos[1],infos[2],infos[3],infos[4],infos[5],infos[6],infos[7],infos[8])
        medit.append(infos)
        num = num + 1
    filem.close() #close file



    # print(medit[ememberno][0], medit[ememberno][1], medit[ememberno][2], medit[ememberno][3],
    # medit[ememberno][4], medit[ememberno][5], medit[ememberno][6], medit[ememberno][7], medit[ememberno][8])
    try:

        print('\n')
        ememberno = int(input("Please insert Member No to edit:\t ")) #accept use input
        ememberno = ememberno - 1 #user input -1 as array start from 0

        for infos in medit: #validate if member id exits then add into 'validate' list
            if ememberno+1==int(infos[0]):
                validate.append(infos)

        if not validate: #if member id not found then call admin edit function to rerun again
            print("Member does not exist, Please try again")
            return admineditmember()


        field = int(input('Please enter field to changes to be made:\t')) #accept user input

        field = field - 1 #user input -1 due to array start from 0

        if field > 9 or field < 0: #limit user input within range of 0 to 9
            print('Sorry no such field.\nPlease try again.')

        #edit member ID

        if field==0: #if user input =0
            nmemberid = input("Please enter new Member ID:\t ") #accept user input
            medit[ememberno][field] = nmemberid
            filem = open('Username.txt', 'w') #open username text file in write mode
            for member in medit: #replace original data with user input
                for infos in member:
                    filem.write(infos)
                    filem.write("\t")
                filem.write('\n')
            filem.close()
            print(medit[ememberno]) #print edited detail

        elif field==1:

            # edit username
            nusername = input("Please enter new Username:\t ")
            medit[ememberno][1] = nusername
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write("\t")
                filem.write('\n')
            filem.close()
            print(medit[ememberno])

        elif field==2: #if user input =2

            # edit firstname
            nfirstname = input("Please enter new First Name:\t ")
            medit[ememberno][2] = nfirstname
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write('\t')
                filem.write("\n")
            filem.close()
            print(medit[ememberno])

        elif field==3: #if user input =3

            # edit last name
            nlastname = str(input("Please enter new Last Name:\t "))
            medit[ememberno][3] = nlastname
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write('\t')
                filem.write('\n')
            filem.close()
            print(medit[ememberno])

        elif field==4: #if user input =4

            # edit email
            nemail = input("Please enter new Email:\t ")
            medit[ememberno][4] = nemail
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write('\t')
                filem.write('\n')
            filem.close()
            print(medit[ememberno])

        elif field==5:#if user input =5

            npassword = input("Please enter new Password:\t ")
            medit[ememberno][5] = npassword
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write('\t')
                filem.write('\n')
            filem.close()
            print(medit[ememberno])

        elif field==6: #if user input =6

            # edit telephone
            ntelephoneno = input("Please enter new Telephone Number in 10 digits:\t ")

            if (len(ntelephoneno) != 10): #limit the numbers for telephone number to be 10 only
                print('Please enter telephone number again in 10 digits.')
                return admineditmember()

            medit[ememberno][6] = ntelephoneno
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write('\t')
                filem.write('\n')
            filem.close()
            print(medit[ememberno])

        elif field==7: #if user input =7

            #edit back card number
            ncard = input("Please enter new Bank Card No. in 16 digits:\t ")

            if (len(ncard) != 16): #limit the numbers for bank card number to be 16 only
                print('Please enter Bank Card Number again in 16 digits')
                return admineditmember()

            medit[ememberno][7] = ncard
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write('\t')
                filem.write('\n')
            filem.close()
            print(medit[ememberno])

        elif field==8: #if user input =8

            #edit bank car pass word
            ncardp = input("Please enter new Bank Card Password:\t ")
            medit[ememberno][8] = ncardp
            filem = open('Username.txt', 'w')
            for member in medit:
                for infos in member:
                    filem.write(infos)
                    filem.write('\t')
                filem.write('\n')
            filem.close()
            print(medit[ememberno])
    except:
        print('Invalid input.\nPlease try again.')



#validate username input

def test001(): #define test001 function
    file=open('Username.txt','r') #open username text file in read mode

    try:
        username = str(input("Please enter Member Username:\t ")) #accept user input

        for details in file:
            details = details.split("\t")
            if (username == details[1]): #check if user input exists in username of username file
                print('Sorry username have been used\nPlease use another username.')
                return test001()
            else:
                continue

        return username #return username variable
    except:
        print('Invalid input.\nPlease try again.')


#admin create member

def admincreatemember(): #define admincreatemember function

    try:
        flag=1 #set flag as 1
        mID = str(memberid()) #call memberid function to auto generate new member id
        username = str(test001()) #call test001 function to ensure no repeated username
        firstname = str(input("Please enter First Name:\t ")) #accept user input
        lastname = str(input("Please enter Last Name:\t "))
        email = input("Please enter Email Address:\t ")
        password = str(input("Please enter Password:\t "))
        telephoneno = str(input("Please enter Telephone Number in 10 digits:\t "))

        if (len(telephoneno) != 10): #limit telephon number to be 10 number only
            print('Please enter telephone number again in 10 digits.')
            return admincreatemember()

        cardno = str(input("Please enter Bank Card Number in 16 digits:\t "))

        if (len(cardno) != 16): #limit bank card number to be 16 number only
            print('Please enter Bank Card Number again in 16 digits')

            return admincreatemember()

        usertype=str(input('Please enter usertype (Member/Admin):\t ')) #accept user input, transform to lowercase and 1st letter into uppercase
        usertype=usertype.lower()
        usertype=usertype.title()


        if usertype!='Member'and usertype!='Admin': #limit user input only member and admin only
            print('Invalid input.\nPlease try again.')
            flag=0
            return admincreatemember()

        cpassword=str(input("Please enter Password for your bank card:\t "))
        if flag==1:
            filem = open("Username.txt", "a") #open username text file in append mode (add)

            memberinfo = [mID, username, firstname, lastname, email, password, telephoneno, cardno,cpassword,usertype] #add variables into list

            for infos in memberinfo: #add infos in list into file and close file
                filem.write(infos)
                filem.write("\t")
            filem.write("\n")
            filem.close()

    except:
        print('Invalid input.\nPlease try again.')

#customer become member

def customercreatemember(): #define member create member function
    try:
        mID = str(memberid()) #call memberid function to auto generate next member id
        username = str(test001()) #call test001 function to ensure no repeated username
        firstname = str(input("Please enter First Name:\t ")) #accept user input and declare user input as variable
        lastname = str(input("Please enter Last Name:\t "))
        telephoneno = str(input("Please enter Telephone Number in 10 digits:\t "))

        if (len(telephoneno) != 10): #limit telephone number to be 10 number only
            print('Please enter telephone number in 10 digits.')
            return customercreatemember()

        email = input("Please enter Email Address:\t ")
        password = str(input("Please enter Password:\t "))
        cardno = str(input("Please enter Bank Card Number in 16 digits:\t "))
        if (len(cardno) != 16): #limit bank card number to be 16 number only
            print('Please enter Bank Card number again in 16 digits')
            return customercreatemember()

        usertype=str('Member') #fix usertype for accounts created by non admin
        cpassword=str(input("Please enter Password for your bank card:\t "))

        filem = open("Username.txt", "a") #open username text file in append mode (add)

        memberinfo = [mID, username, firstname, lastname, email, password, telephoneno, cardno,cpassword, usertype] #insert variable into list

        for infos in memberinfo: #add informations in list into username file
            filem.write(infos)
            filem.write("\t")
        filem.write("\n")
        filem.close() #close file
        print('')

    except:
        print('Invalid input.\nPlease try again.')


#auto generate member id

def memberid(): #define memberid function
    text_file = open("Username.txt", "r") #open username text file in read mode
    user = [] #create 'user' list
    for userid in text_file: #remove space and seperate infos of file with tab
        userid = userid.rstrip()
        userid = userid.split('\t')
        user.append(userid)
        ##print(len(userid))

    x = len(user) #declare x as number of items in 'user' list

    if not x: #if list (file) is empty, declare newestid=1 or else largest number of user id +1
        newestID =1
    else:
        newestID = int(user[x - 1][0]) + 1
    return newestID #return value of newestid

#view all member info
def vmemberinfo(): #define vmemberinfo function
    filem = open("Username.txt", "r") #open username text file in read mode
    print("-" * 45, "Member Details", "-" * 45)
    memberid = 1
    for infos in filem: #print details of each member in file
        infos = infos.split("\t")
        print("Member ID:\t", infos[0])
        print("Username:\t", infos[1])
        print("First name:\t", infos[2])
        print("Last name:\t", infos[3])
        print("Email:\t", infos[4])
        print('Password:\t', infos[5])
        print("Telephone No.:\t", infos[6])
        print("Bank Card No.:\t", infos[7])
        print("Bank Card Password:\t", infos[8])


        memberid = memberid + 1
        print('\r')
    filem.close() #close file
    adminmenu()

#login

def log(): #define log function
    username=input('Please enter Username:\t ') #accept username and password input

    password=input('Please enter Password:\t ')

    usertype=userverification(username,password) #declare usertype = variable returned from user verification

    if usertype=='Admin': #if usertype = admin then call adminmenufunction, member then open membermenu function, or else back to main menu
        adminmenu()#adminmenu()

    elif usertype=='Member':
        membermenu()#membermenu()
    else:
        print("Sorry, invalid Username or Password.\n Please try again.")
        mmenu()

#user verification
def userverification(username,password): #declare userverification(username,password) function
    accfile=open('Username.txt','r') #open usernametext file in read mode
    user=[]
    for infos in accfile: #remove blank space, seperate infos in file with tab
        infos=infos.rstrip()
        infos=infos.split('\t')
        if username==infos[1]:
            if password==infos[5]: #if both user input exists in username text file, print all user details
                print("Login success")
                print('Welcome',infos[2], infos[3])
                print('\n')
                print('Personal details:\t')
                print("Member ID:\t", infos[0])
                print("Username:\t", infos[1])
                print("First name:\t", infos[2])
                print("Last name:\t", infos[3])
                print("Email:\t", infos[4])
                print('Password:\t', infos[5])
                print("Telephone No.:\t", infos[6])
                print("Bank Card No.:\t", infos[7])
                print("Bank Card Password.:\t", infos[8])
                userIDMain = infos[0]
                userFirstNameMain = infos[2]
                userLastNameMain = infos[3]
                return infos[9] #return infos[9] (admin or member) to decide to call admin menu or membermenu function
            else:
                break
        else:
            continue
    accfile.close() #close file


#menu section

#member menu

def membermenu(): #define membermenu function
    memberchoice=True #allows the while loop to run endlessly (and print out option avaiable and accept user input
    while memberchoice:
        print('-'*50, "Welcome",'-'*50) #print title and choices available
        print("Options available:")
        print('1.\tEdit Account Info')
        print('2.\tView Car Gallery')
        print('3.\tBook Car')
        print('4.\tView Personal Booking Records')
        print('5.\tEXIT')

        try: #validate errors

            memberchoice = int(input("Please select an option listed below:\t ")) #accept user input

        except: #back to member menu if error input
            print('Invalid input.\nPlease try again.')
            membermenu()
            break

            # call different functions based on user input

        if memberchoice == 1: #if user input is 1 then call respective function
            print("\'1.\tEdit Account Info\' function is selected")  # call another function
            membereditinfo()

        elif memberchoice == 2: #if user input is 2 then call respective function
            print("\'2.\tView Car Gallery function\' is selected")  # call another function
            viewcargallerym()

        elif memberchoice == 3: #if user input is 3 then call respective function
            print('\'3.\tBook Car\' function is selected')
            rent()

        elif memberchoice==4: #if user input is 4 then call respective function
            print("\'4.\tView Personal Booking Records\' is selected")
            viewpersonalhistory()

        elif memberchoice==5: #if user input is 5 then call respective function
            print("Thank you, please come again")
            exit()

        else: #if other number other than 1 to 5 the back to member menu again
            print("Sorry, option is not valid, please choose an option among 1 to 5. \n Thank you.")
            membermenu()
            break


#admin menu

def adminmenu(): #def adminmenu function
    adminchoice=True #allows the while loop to run endlessly (and print out option avaiable and accept user input
    while adminchoice:

        print('-'*50,'Admin Main Menu', '-'*50) #print title and choices available
        print("Welcome, Administrator")
        print("Options available:")
        print('1.\tView Member Account Info')
        print('2.\tEdit Account Info')
        print('3.\tCreate Member')
        print('4.\tDelete Member')
        print('5.\tView Car Gallery')
        print('6.\tSearch Car')
        print('7.\tAdd Cars')
        print('8.\tEdit Cars')
        print('9.\tDelete Cars')
        print('10.\tView Booking Records')
        print('11.\tSearch Records')
        print('12.\tEXIT')

        try: #validate any errors

            adminchoice = int(input("Please select an option listed below:\t ")) #accept user input

        except: #rerun adminmenu if invalid input
            print('Invalid input.\nPlease try again.')
            adminmenu()

        adminchoice = int(adminchoice) #change data type of adminchoice into integer

        if adminchoice==1: #if user input is 1 then call respective function
            print('\'1.\tView Member Account Info\' function is selected')
            vmemberinfo()
        elif adminchoice==2: #if user input is 2 then call respective function
            print('\'2.\tEdit Account Info\' function is selected')
            admineditmember()
        elif adminchoice==3: #if user input is 3 then call respective function
            print('\'3.\tCreate Member\' function is selected')
            admincreatemember()
        elif adminchoice==4: #if user input is 4 then call respective function
            print('\'4.\tDelete Member\' function is selected')
            deletemember()
        elif adminchoice==5: #if user input is 5 then call respective function
            print('\'5.\tView Car Gallery\' function is selected')
            viewcargallerya()
        elif adminchoice==6: #if user input is 6 then call respective function
            print('\'6.\tSearch Car\' function is selected')
            searchCar()
        elif adminchoice==7: #if user input is 7 then call respective function
            print('\'7.\tAdd Cars\' function is selected')
            adminaddcar()
        elif adminchoice == 8: #if user input is 8 then call respective function
            print('\'8.\tEdit Cars\' function is selected')
            editcargallery()

        elif adminchoice==9: #if user input is 9 then call respective function
            print('\'9.\tDelete Car\' function is selected')
            deletecar()

        elif adminchoice == 10: #if user input is 10 then call respective function
            print('\'10.\tView Booking Records\' function is selected') #complete?
            viewrecords()

        elif adminchoice==11: #if user input is 11 then call respective function
            print('\'11.\tSearch Records\' function is selected') #complete?
            searchrecord()

        elif adminchoice==12: #if user input is 12 then call respective function
            print('Thank you, please come again.')
            exit()
        else: #if other number other than 1 to 12 the back to admin menu again
            print('Sorry, option is not valid, please choose an option among 1 to 9. \n Thank you.')
            adminmenu()
        #except:
            #print("Sorry, option is not valid, please choose an option among 1 to 9. \nThank you.")
            #adminmenu()

#main menu function

def mmenu(): #define mmenu function

    mmchoice = True #allow while loop to run endlessly (print options available and accept user input)
    while mmchoice:
        print("-"*40, "MAIN MENU", "-"*40) #print title and choices available
        print("Welcome to SUPER CAR RENTAL SERVICES (SCRS)")
        print("Options available:")
        print("1.\tView Cars")
        print("2.\tLogin")
        print("3.\tRegistration")
        print("4.\tEXIT")



        try: #validate any input errors

            mmchoice = int(input("Please select an option listed below:\t ")) #accept user input

        except: #back to main menu if error input
            print('Invalid input.\nPlease try again.')
            mmenu()

        mmchoice=int(mmchoice) #set user input into integer

        # call different functions based on user input

        if mmchoice == 1: #if user input is 1 then call respective function
            print("\"1. View Cars\" option is selected") #call another function
            viewcargallery()

        elif mmchoice == 2: #if user input is 2 then call respective function
            print("\"2. Login\"option is selected")#call another function
            emergency0()
            log()
        elif mmchoice == 3: #if user input is 3 then call respective function
            print("\"3. Member Registration\"option is selected")#call another function
            emergency1()
        elif mmchoice == 4: #if user input is 4 then call respective function
            print("Thank you, please come again")
            exit()
        else: #if other number other than 1 to 4 the back to main menu again
            print("Sorry, option is not valid, please choose an option among 1 to 4. \nThank you.")
            mmenu()



#call main menu function to execute program

mmenu()