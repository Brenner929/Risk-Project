


# Higest score is 120
# This will be the quetions that will be asked

# function for some yes no problems
# This function takes the Yes/No options and correctly outputs the numerical that is assoated with the excel sheet
'''
Creation Date:      6/4/2018
Original Author:    Christian Brenner, Matt Salvo, BMCS
Version Author:
Version:            0.1.4
Version Date:
'''


####################
# RETRIVE EXTERNAL #
####################
import os
os.system('cls')
print(">Installing/Verifying Libraries")
os.system('pip install pandas numpy xlsxwriter')
print(">Installing/Verifying completed")
os.system('cls')


######################
# EXTERNAL LIBRARIES #
######################
import re
import pandas as pd
import numpy as np
import xlsxwriter


####################
# GLOBAL VARIABLES #
####################
runt = 0
likelyhood_final = 0
impact_score = 0
bingo = []
xchart = 0
ychart = 0
infoarr = []
a = 1
zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []
eleven = []
twelve = []
thirteen = []
fourteen = []
fifteen = []
sixteen = []
seventeen = []
eighteen = []
nineteen = []
twenty = []
twenty_one = []
twenty_two = []
twenty_three = []
twenty_four = []

#############
# FUNCTIONS #
#############

###>- CHECK INPUT VALIDATION -<###          INOUT REFERENCE / OUTPUT SCORE
def check(reference, highest):
    while True:
        if (reference > highest) or (reference < 1):
            reference = int(input('Invalid input! Please enter another choice: '))
        else:
            score = reference
            break
    return score

###>- PLOTS SCORE ON [x,y] GRAPH -<###       INPUT NUM, NUM2 / OUTPUT ARR , ARR2
def scorefunction(num, num2):


    #=============
    # VARIABLES
    #=============
    "SET GLOBAL"
    global xchart
    global ychart
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"


    y = num
    x = num2

    # =============
    # PROCESS
    # =============

    # Assigning the correct value to the Likelihood score.
    if y <= 10:                       # If 10 or less Very Low is assigned
        ychart = 0
    if y in range(11, 41):            # If 11 - 40 Low is assigned
        ychart = 1
    if y in range(40, 61):            # If 40-60 Moderate
        ychart = 2
    if y in range(60, 91):            # 60-90 is High
        ychart = 3
    if y in range(91, 125):           #91 to anything else is Very High
        ychart = 4

    # Assigning the correct risk to the Impact
    if x == 0:                        # An Score of 0 equates to a Very Low Score
        xchart = 0
    if x == 1:                        # 1 = Low
        xchart = 1
    if x == 2:                        # 2 for Moderate
        xchart = 2
    if x == 3:                        # 3 for High
        xchart = 3
    if x == 4:                        # 4 for Very High. // No Score Higher than 4 is possible.
        xchart = 4


###>- DOES MATH -<###         INPUT: num / OUTPUT: num
def maths(num):
    #=============
    # VARIABLES
    #=============
    "Set Global"
    global runt
    "Set Strings"
    tomCat = ""
    "Set Int's"
    getGood = 0
    "Set Martix/list"
    adminMatrix = []
    santasList = []

    #=============
    # PROCESS
    #=============
    "Testing num for a given value"
    num -= 1                            # Subtract 1 from num
    if (num == 2):                      # If num is equal to 3
        num = 0                         # Set num to 0
    else:
        print('NOPE')
    # END IF:ELSE


    "End Function"
    return num


###>- CALCULATES LIKELY HOOD SCORE -<###         INPUT NUM / OUTPUT SCORE
def likelyhood(num):
    "SET GLOBAL"
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    # TAKES THE INPUT AND * 5 TO IT FOR A CORRECT SCORE
    score = num * 5
    return score


###>- GATHERS THE BASIC STRING INFO FOR THE SYSTEM -<###        INPUT NONE / OUTPUT ARR
def basicInfo():

    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    System_name = input('Enter System Name: ')

    System_status = int(input('Please Chose the coresponding number for your system status: \n1.Pre-Milestone \n2.LIRP '
                              '\n'
                              'Choice: '))
    if System_status == 1:
        System_status = str('Pre-Milestone')
    if System_status == 2:
        System_status = str('LIRP')

    Authorizing_official = input('Please enter Authorizing Official: ')

    Service_branch = int(input('Please Select Branch: \n1.Army \n2.Navy \n3.Air Force \nChoice: '))
    if Service_branch == 1:
        Service_branch = str('Army')
    if Service_branch == 2:
        Service_branch = str('Navy')
    if Service_branch == 3:
        Service_branch = str('Air Force')

    Rationale_for_waiver = input('Im lazy')

    Data_classification = int(input('Please Select Data Classification: '
                                    '\n1.U \n2.S \n3.TS \nChoice: '))
    if Data_classification == 1:
        Data_classification = str('Unclassified')
    if Data_classification == 2:
        Data_classification = str('Secret')
    if Data_classification == 3:
        Data_classification = str('Top Secret')

    arr = System_name, System_status, Authorizing_official, Service_branch, Rationale_for_waiver, Data_classification
    return arr


###>- GATHERS THE IMPACT SCORE -<###            INPUT NONE / OUTPUT SCORE
def impact():
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    mic = int(input('Please Enter Mission Impact if Compromised: \n5.Very High \n4.High \n3.Moderate \n2.Low '
                    '\n1.Very Low \nChoice: '))
    mic = check(mic, 5)                             # Input Validation
    mic -= 1
    score = mic

    isc = int(input('Please Enter Impact to the System if Compromised: \n5.Very High \n4.High \n3.Moderate \n2.Low '
                    '\n1.Very Low \nChoice: '))
    isc = check(isc, 5)                             # Input Validation
    isc -= 1
    if score <= isc:
        score = isc

    return score


###>- GATHERS THE BASE SCORE FOR LIKELYHOOD FOR RISK -<###          INPUT RUNT / OUTPUT LIKELY, IMPACT_SCORE
def likelyhood_score():
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    global impact_score
    global runt
    "SET STRINGS"
    "SET INT'S"
    answer = 0
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============


    connectivity = int(input('Please Select connectivity to the internet: \n1.Open Network - Commercial ISP '
                             '\n2.Open Network - .edu  '
                             '\n3.Open Network - NIPR  '
                             '\n4.Closed Restricted Network - SIPRNET  '
                             '\n5.Closed Restricted Network - JWICS  '
                             '\n6.Closed Restricted Network - SAP/SAR  '
                             '\n7.Closed Restricted Network - Other  '
                             '\n8.Standalone Network  '
                             '\n9.Standalone System - With Media  '
                             '\n10.Standalone System - No Media'
                             '\nChoice: '))

    connectivity = check(connectivity, 10)  # Input Validation
    connectivity = 10 - connectivity
    runt += connectivity

    system_fielded = int(input('Please select how many systems are fielded: '
                               '\n1.1-10  '
                               '\n2.11-50  '
                               '\n3.51-100  '
                               '\n4.101-500  '
                               '\n5.501+ '
                               '\nChoice: '))
    system_fielded = check(system_fielded, 5)                                       # Input Validation
    runt += system_fielded

    email = int(input('Are users able to email?: '
                      '\n1.Yes  '
                      '\n0.No '
                      '\nChoice: '))

    runt += email

    web = int(input('Are users able to use a web browser?: '
                    '\n1.Yes  '
                    '\n0.No '
                    '\nChoice: '))
    runt += web

    admin_privileges = int(input('What kind of users are logged on as?: '
                                 '\n1.User '
                                 '\n2.Admin - Partial privileges '
                                 '\n3.Admin - Elevated privileges '
                                 '\n4.Does not Apply'
                                 '\nChoice: '))

    # Fixes the numbering issue so 1 = 0, 2 = 1 , 3 = 2, and 4 = 0;
    admin_privileges = check(admin_privileges, 4)                                   # Input Validation
    admin_privileges -= 1
    if admin_privileges == 3:
        admin_privileges = 0

    runt += admin_privileges

    tfa = int(input('Does the system have PIK or TFA?: '
                    '\n1.Yes '
                    '\n2.No '
                    '\n3.Does not Apply'
                    '\nChoice: '))
    # corrects for the number 3 choice due to maths function.
    tfa = check(tfa, 3)                                                             # Input Validation
    tfa = maths(tfa)
    runt += tfa

    app_whitelist = int(input('Use a App whitelisting capability?: '
                              '\n1.Yes '
                              '\n2.No '
                              '\n3.Does not Apply'
                              '\nChoices: '))
    app_whitelist = check(app_whitelist, 3)                                         # Input Validation
    app_whitelist = maths(app_whitelist)
    runt += app_whitelist

    host_protection = int(input('Uses Host Based Protection?: '
                                '\n1.Yes '
                                '\n2.No'
                                '\nChoices: '))
    host_protection = check(host_protection, 2)                                     # Input Validation
    host_protection = maths(host_protection)
    runt += host_protection

    hard_ports = int(input('Are the unused ports (Ethernet/USB) disabled on the system?: '
                           '\n1.Yes  '
                           '\n2.No'
                           '\nChoices: '))
    hard_ports = check(hard_ports, 2)
    hard_ports = maths(hard_ports)
    runt += hard_ports

    stigs = int(input('Have any STIGs been run on the system?: '
                      '\n1.Yes  '
                      '\n2.No  '
                      '\nChoices: '))
    stigs = check(stigs, 2)
    stigs = maths(stigs)
    runt += stigs

    encryption = int(input('Is ecnryption at rest?: '
                           '\n1.Yes  '
                           '\n2.No  '
                           '\nChoices: '))
    encryption = check(encryption, 2)
    encryption = maths(encryption)
    runt += encryption

    'This is commented out until further notice'
    # owner = input('System Owner Approval Justification Discussion: ')
    #
    # system_ato_date = input('Please enter System ATO Date in MM/DD/YYYY Format: ')
    #
    # anticipated_ato_date = input("Please Enter Anticipated ATO Date in MM/DD/YYYY Format: ")
    #
    impact_score = impact()
    #
    # print('Additional Testing: Please leave this section blank')

    testing = int(input('Has any Testing been complected?: '
                        '\n1.Yes - Vulnerability  \n2.Yes - Penetration  \n3. Yes - Adversary  \n4.No: '
                        '\nChoices: '))

    # Make a negative number out of the Choice selected
    testing = check(testing, 4)
    if testing == 4:
        testing = 0
    else:
        testing = testing * -5
    runt += testing


    # funding = int(input('Is Funding Available: '
    #                     '\n1.Yes  \n2.No  \n0.Does Not Apply \nChoices : '))
    # funding -= 1
    # if (funding == 1) or (funding == 0):
    #     when_funding = input('When will funding be available?: (Please enter in MM/DD/YYYY format)')
    # runt += funding // Funding should not effect the likely hood score

    answer = likelyhood(runt)
    return answer

###>- PLOTS LIKELYHOOD AND IMPACT ON A 23 FLAT DATA LIST
def plot(xval, yval):
    ####################
    # GLOBAL VARIABLES #
    ####################
    global zero
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global ten
    global eleven
    global twelve
    global thirteen
    global fourteen
    global fifteen
    global sixteen
    global seventeen
    global eighteen
    global nineteen
    global twenty
    global twenty_one
    global twenty_two
    global twenty_three
    global twenty_four
    global a


    b = 'R'
    if xval == 0:
        if yval == 4:
            zero.append(b)
        if yval == 3:
            five.append(b)
        if yval == 2:
            ten.append(b)
        if yval == 1:
            fifteen.append(b)
        if yval == 0:
            twenty.append(b)
    if xval == 1:
        if yval == 4:
            one.append(b)
        if yval == 3:
            six.append(b)
        if yval == 2:
            eleven.append(b)
        if yval == 1:
            sixteen.append(b)
        if yval == 0:
            twenty_one.append(b)
    if xval == 2:
        if yval == 4:
            two.append(b)
        if yval == 3:
            seven.append(b)
        if yval == 2:
            twelve.append(b)
        if yval == 1:
            seventeen.append(b)
        if yval == 0:
            twenty_two.append(b)
    if xval == 3:
        if  yval == 4:
            three.append(b)
        if yval == 3:
            eight.append(b)
        if yval == 2:
            thirteen.append(b)
        if yval == 1:
            eighteen.append(b)
        if yval == 0:
            twenty_three.append(b)
    if xval == 4:
        if yval == 4:
            four.append(b)
        if yval == 3:
            nine.append(b)
        if yval == 2:
            fourteen.append(b)
        if yval == 1:
            nineteen.append(b)
        if yval == 0:
            twenty_four.append(b)
    print(zero, one, two, three, four)
    print(five, six, seven, eight, nine)
    print(ten, eleven, twelve, thirteen, fourteen)
    print(fifteen, sixteen, seventeen, eighteen, nineteen)
    print(twenty, twenty_one, twenty_two, twenty_three, twenty_four)



def output():

    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"
    global impact_score
    global likelyhood_final
    global infoarr
    global xchart
    global ychart
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    #arr = [System_name, System_status, Authorizing_official, Service_branch, Rationale_for_waiver, Data_classification]
    print('')
    print('Here are your results!')
    print('System Name: ' + infoarr[0])
    print('System Status: ' + infoarr[1])
    print('Authorizing Official: ' + infoarr[2])
    print('Service Branch: ' + infoarr[3])
    print('Data Classification: ' + infoarr[5])
    print('')
    print('Your system risk score is as follows.\nX-Value: ' + str(xchart))
    #print('Y-Value: ' + ychart)


def main():

    global impact_score
    global likelyhood_final
    global runt
    global bingo
    global infoarr
    global xchart
    global ychart

    # basicinfo()
    # likelyhood_final = likelyhood_score()
    # scorefunction(likelyhood_final, impact_score)       #return

    infoarr = basicInfo()
    likelyhood_final = likelyhood_score()
    scorefunction(likelyhood_final, impact_score)
    output()
    plot(xchart, ychart)
    print("Impact ", impact_score)
    print("LikelyHood ", likelyhood_final)
    return 0


main()




