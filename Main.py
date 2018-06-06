


# DOES NOT APPLY does not work untill it is switched to option 0
# This will be the quetions that will be asked

# function for some yes no problems
# This function takes the Yes/No options and correctly outputs the numerical that is assoated with the excel sheet
'''
Creation Date:      6/4/2018
Original Author:    Christian Brenner, Matt Salvo, BMCS
Version Author:
Version:            0.1
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


#############
# FUNCTIONS #
#############

###>- PLOTS SCORE ON [x,y] GRAPH -<###       INPUT NUM, NUM2 / OUTPUT ARR , ARR2
def scorefunction(num, num2):


    #=============
    # VARIABLES
    #=============
    "SET GLOBAL"
    "SET STRINGS"
    "SET INT'S"
    "SET MARTIX/LIST"
    xnx = 0

    arrl = [0, 4]
    arri = [0, 1]

    arrl[0] = num
    arri[0] = num2

    # =============
    # PROCESS
    # =============

    # Assigning the correct value to the Likelihood score.
    for x in range(0,2):
        if arrl[x] <= 10:                       # If 10 or less Very Low is assigned
            arrl[x] = 'Very Low'
        if arrl[x] in range(11, 41):            # If 11 - 40 Low is assigned
            arrl[x] = 'Low'
        if arrl[x] in range(40, 61):            # If 40-60 Moderate
            arrl[x] = 'Moderate'
        if arrl[x] in range(60, 91):            # 60-90 is High
            arrl[x] = 'High'
        if arrl[x] in range(91, 120):           #91 to anything else is Very High
            arrl[x] = 'Very High'

    # Assigning the correct risk to the Impact
    for x in range(0,2):
        if arri[x] == 0:                        # An Score of 0 equates to a Very Low Score
            arri[x] = 'Very Low'
        if arri[x] == 1:                        # 1 = Low
            arri[x] = 'Low'
        if arri[x] == 2:                        # 2 for Moderate
            arri[x] = 'Moderate'
        if arri[x] == 3:                        # 3 for High
            arri[x] = 'High'
        if arri[x] == 4:                        # 4 for Very High. // No Score Higher than 4 is possible.
            arrl[x] = 'Very High'

    xnx = [0,0]
    return xnx
    return


###>- GATHERS THE BASIC STRING INFO FOR THE SYSTEM -<###        INPUT NONE / OUTPUT ARR
def basicinfo():

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

    arr = [System_name, System_status, Authorizing_official, Service_branch, Rationale_for_waiver, Data_classification]


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
    if (num == 3):                      # If num is equal to 3
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

    arr = [System_name, System_status, Authorizing_official, Service_branch, Rationale_for_waiver, Data_classification]


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

    mic = int(input('Please Enter Mission Impact if Compromised: \n4.Very High \n3.High \n2.Moderate \n1.Low '
                    '\n0.Very Low \nChoice: '))
    score = mic

    isc = int(input('Please Enter Impact to the System if Compromised: \n4.Very High \n3.High \n2.Moderate \n1.Low '
                    '\n0.Very Low \nChoice: '))

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
                             '\n2.Open Network - .edu , '
                             '\n3.Open Network - NIPR , '
                             '\n4.Closed Restricted Network - SIPRNET , '
                             '\n5.Closed Restricted Network - JWICS , '
                             '\n6.Closed Restricted Network - SAP/SAR , '
                             '\n7.Closed Restricted Network - Other , '
                             '\n8.Standalone Network , '
                             '\n9.Standalone System - With Media , '
                             '\n10.Standalone System - No Media'
                             '\nChoice: '))
    # This Line Flips the number to the correct out put. AKA 1 will = 9 to collate with the Excel sheet scoring table.
    connectivity = 10 - connectivity
    runt += connectivity

    system_fielded = int(input('Please select how many systems are fielded: '
                               '\n1.1-10 , '
                               '\n2.11-50 , '
                               '\n3.51-100 , '
                               '\n4.101-500 , '
                               '\n5.501+ '
                               '\nChoice: '))
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
    if admin_privileges == 3:
        admin_privileges = 0

    runt += admin_privileges

    tfa = int(input('Does the system have PIK or TFA?: '
                    '\n1.Yes '
                    '\n2.No '
                    '\n3.Does not Apply'
                    '\nChoice: '))
    tfa = maths(tfa)
    runt += tfa

    app_whitelist = int(input('Use a App whitelisting capability?: '
                              '\n1.Yes '
                              '\n2.No '
                              '\n3.Does not Apply'
                              '\nChoices: '))
    app_whitelist = maths(app_whitelist)
    runt += app_whitelist

    host_protection = int(input('Uses Host Based Protection?: '
                                '\n1.Yes '
                                '\n2.No'
                                '\nChoices: '))

    host_protection = maths(host_protection)
    runt += host_protection

    hard_ports = int(input('Are the unused ports (Ethernet/USB) disabled on the system?: '
                           '\n1.Yes  '
                           '\n2.No'
                           '\nChoices: '))

    hard_ports = maths(hard_ports)
    runt += hard_ports

    stigs = int(input('Have any STIGs been run on the system?: '
                      '\n1.Yes  '
                      '\n2.No  '
                      '\n0. Does Not Apply:'
                      '\nChoices: '))
    runt += stigs

    encryption = int(input('Is ecnryption at rest?: '
                           '\n1. Yes , '
                           '\n2. No , '
                           '\n0. Does Not Apply'
                           '\nChoices: '))
    encryption = maths(encryption)
    runt += encryption

    'This is commented out untill firther notice'
    # owner = input('System Owner Approval Justification Discussion: ')
    #
    # system_ato_date = input('Please enter System ATO Date in MM/DD/YYYY Format: ')
    #
    # anticipated_ato_date = input("Please Enter Anticipated ATO Date in MM/DD/YYYY Format: ")
    #
    impact_score = impact()
    #
    # print('Additional Testing: Please leave this section blank')

    testing = int(input('Has any Testing been compleated?: '
                        '\n1.Yes - Vulnerability  \n2.Yes - Penetration  \n3. Yes - Adversary , \n4.No: '
                        '\nChoices: '))

    # Make a negative number out of the Choice selected
    if testing == 4:
        testing = 0
    else:
        testing = testing * -5
    runt += testing

    SMI = int(input('Were security measures implemented?: '
                    '\n1.Yes  \n2.No  \n0.Does Not Apply \nChoices: '))
    runt += SMI

    exsmi = input('If yes to the previous question please enter a description: ')

    # funding = int(input('Is Funding Available: '
    #                     '\n1.Yes  \n2.No  \n0.Does Not Apply \nChoices : '))
    # funding -= 1
    # if (funding == 1) or (funding == 0):
    #     when_funding = input('When will funding be available?: (Please enter in MM/DD/YYYY format)')
    # runt += funding // Funding should not effect the likely hood score

    answer = likelyhood(runt)
    return answer


def main():

    global impact_score
    global likelyhood_final
    global runt
    global bingo



    # basicinfo()
    # likelyhood_final = likelyhood_score()
    # a = scorefunction(likelyhood_final, impact_score)       #return


    for x in range(0,3):
        bingo[x][y].append['r'+1]


    print(impact_score)
    print(likelyhood_final)
    return 0


main()





# Function 3 Bellow


# def Al(Runt):
#
#     answer = 0
#
#     x=0
#     y=0
#     y += answer
#     while(x<y):
#     Total += 5
#     x += 1
#
#     RunT += Total
