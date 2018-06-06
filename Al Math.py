

###>- GATHERS THE BASIC STRING INFO FOR THE SYSTEM -<###        INPUT NONE / OUTPUT ARR
def BasicInfo():

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


BasicInfo()


