import csv
import datetime
import requests
import os
import random

class recommending_ppl:
    def __init__(self):
        self.x = input("What is your first name ")
        self.y = input("What is your last name ")
        self.url = input("What is the url of your courseoff export to ical ")
    def class_finder(self): #This function downloads an ical file from the users input, reads from the file, and then deletes the file from memory
        r = requests.get(self.url,allow_redirects=True)
        f1 = open('classes.ical', 'wb').write(r.content)
        fall_classes_list = []
        spring_classes_list = []
        spring_ending = [datetime.datetime(2019,4,23,23,59,59)]
        from icalendar import Calendar
        f = open("classes.ical","rb")
        fcal = Calendar.from_ical(f.read())
        for component in fcal.walk():
            if component.name == "VEVENT":
                if component.get("RRULE")["UNTIL"] == spring_ending and component.get("SUMMARY") not in spring_classes_list:
                    spring_classes_list.append(component.get("SUMMARY"))
                elif component.get("RRULE")["UNTIL"] != spring_ending and component.get("SUMMARY") not in fall_classes_list:
                    fall_classes_list.append(component.get("SUMMARY"))
        f = open("people.csv","a")
        f.write(self.x + "||")
        f.write(self.y + "||")
        for entry in spring_classes_list:
            f.write(entry + "||")
        f.write("\n")
        f.close()
        os.remove("classes.ical")
    def clean(self): #This function modifies the csv file output so that you don't get your own name as a person to meet
        z = open("people.csv","r")
        myreader = z.readlines()
        myreader = myreader[1:]
        for entry in range(len(myreader)):
            myreader[entry] = myreader[entry].replace(",,\n","")
            myreader[entry] = myreader[entry].replace("\n","")
            myreader[entry] = (myreader[entry]).split("||")
            del myreader[entry][-1]
        extra_list = []
        for num in range(len(myreader)):
            if self.x in myreader[num] and self.y in myreader[num]:
                extra_list.append(num)
        for numero in range(len(extra_list)-1):
            myreader[extra_list[numero]] = []
        #print(extra_list)
        return myreader
    def output(self): #This function outputs people who have atleast one class in common with you
        total_friends_list = []
        shortened_friends_list = []
        myreader = recommending_ppl.clean(self)

        for item in range(len(myreader)):
            if self.x in myreader[item] and self.y in myreader[item]:
                mylist = myreader[item]
        a = myreader.index(mylist)
        del myreader[a]
        for entry in myreader:
            if set(mylist).isdisjoint(set(entry)) == False:
                total_friends_list.append(entry[0] + " " + entry[1])

        # (as the list gets bigger) shortened_friends_list = random.sample(total_friends_list,4)
        
        print (self.x + " " + self.y + " we recommend meeting: ")
        print("\n")
        for i in total_friends_list:
            print(i)
