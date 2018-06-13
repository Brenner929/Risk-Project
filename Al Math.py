#
#
# ###>- GATHERS THE BASIC STRING INFO FOR THE SYSTEM -<###        INPUT NONE / OUTPUT ARR
# def BasicInfo():
#
#     # =============
#     # VARIABLES
#     # =============
#     "SET GLOBAL"
#     "SET STRINGS"
#     "SET INT'S"
#     "SET MARTIX/LIST"
#
#     # =============
#     # PROCESS
#     # =============
#
#     System_name = input('Enter System Name: ')
#
#     System_status = int(input('Please Chose the coresponding number for your system status: \n1.Pre-Milestone \n2.LIRP '
#                               '\n'
#                               'Choice: '))
#     if System_status == 1:
#         System_status = str('Pre-Milestone')
#     if System_status == 2:
#         System_status = str('LIRP')
#
#     Authorizing_official = input('Please enter Authorizing Official: ')
#
#     Service_branch = int(input('Please Select Branch: \n1.Army \n2.Navy \n3.Air Force \nChoice: '))
#     if Service_branch == 1:
#         Service_branch = str('Army')
#     if Service_branch == 2:
#         Service_branch = str('Navy')
#     if Service_branch == 3:
#         Service_branch = str('Air Force')
#
#     Rationale_for_waiver = input('Im lazy')
#
#     Data_classification = int(input('Please Select Data Classification: '
#                                     '\n1.U \n2.S \n3.TS \nChoice: '))
#     if Data_classification == 1:
#         Data_classification = str('Unclassified')
#     if Data_classification == 2:
#         Data_classification = str('Secret')
#     if Data_classification == 3:
#         Data_classification = str('Top Secret')
#
#     arr = [System_name, System_status, Authorizing_official, Service_branch, Rationale_for_waiver, Data_classification]
#
#
# BasicInfo()


def save():
    # =============
    # VARIABLES
    # =============
    "SET GLOBAL"        # Asking the user basic questions for referencing the system
    global arr
    global systemlist = ['as', 'bs', 'cs', 'ds']
    "SET STRINGS"                           # being tested at the time.
    "SET INT'S"
    choisetemp = 0
    numtemp = 1
    "SET MARTIX/LIST"

    # =============
    # PROCESS
    # =============

    # List Systems
    temp = len(systemlist)
    print("Please select system.: ")
    for x in range (0, temp):
        print(numtemp, systemlist[x])
        numtemp += 1

    choisetemp = int(input("Select Here: "))
    # check data entry here
    # need if statements for 1

    choisetemp *= 8
    choisetemp -= 8
    finaltemp = choisetemp + 8
    for x in range (choisetemp, finaltemp):
        print(arr[x])

save()
