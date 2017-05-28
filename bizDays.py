#!/usr/bin/env python3

from bizdays import Calendar

#print("***************************************************************")
#print("*****    תוכנית לחישוב יום סיום משימה אמיתי ללא סופשים    *****")
#print("*****                                                     *****")
#print("*****   רק להזין את תאריך התחלת המשימה ואת משכה,          *****")
#print("***** והתוכנה תחשב את מועד הסיום (תוך התחשבות בסופי שבוע) *****")
#print("*****                                                     *****")
#print("*****                יוצר התוכנית: אמיר דגן               *****")
#print("***************************************************************")
print("****************************************************************")
print("*****  This program calculates real ending date of a task  *****")
print("*****  while considaring weekends                          *****")
print("*****                                                      *****")
print("*****   Just enter the date of start                       *****")
print("*****   and how many days it will continue                 *****")
print("*****                                                      *****")
print("*****   and you will get the date when the task will end   *****")
print("*****                                                      *****")
print("*****                                                      *****")
print("*****           Created by:  Amir Dagan                    *****")
print("****************************************************************")
print()
print()

holiday_list=''
cal = Calendar(holiday_list, ['Friday', 'Saturday'])
again="y"
while(again.lower()=="y"):
    dd=input("Starting Date (dd-mm-yyyy)")
    ndd=dd[6:]+dd[2:6]+dd[:2]
    bd=int(input("Days to count:"))
    bd-=1
    new_dd=cal.offset(ndd, bd)
    nice_dd=new_dd.strftime("%d-%m-%Y")
    print()
    print("---------------->",nice_dd)
    print()
    print()
    again=input("Do you want another calc? (Y/N)")
else:
    print("\n\n\n Thanks, see you next time")