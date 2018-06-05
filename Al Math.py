

System_name = input('Enter System Name: ')

System_status = int(input('Please Chose the coresponding number for your system status.'
                      '1. Pre-Milestone , '
                      '2. LIRP: '))
if System_status == 1:
    System_status = str('Pre-Milestone')
if System_status == 2:
    System_status = str('LIRP')

Authorizing_official = input('Please enter Authorizing Official: ')

Service_branch = int(input('Please Select Branch: '
                       '1. Army , '
                       '2. Navy , '
                       '3. Air Force: '))
if Service_branch == 1:
    Service_branch = str('Army')
if Service_branch == 2:
    Service_branch = str('Navy')
if Service_branch == 3:
    Service_branch = str('Air Force')

Rationale_for_waiver = input('Im lazy')

Data_classification = int(input('Please Select Data Classification: '
                            '1. U , '
                            '2. S , '
                            '3. TS: '))
if Data_classification == 1:
    Data_classification = str('Unclassified')
if Data_classification == 2:
    Data_classification = str('Secret')
if Data_classification == 3:
    Data_classification = str('Top Secret')

arr = [System_name, System_status, Authorizing_official, Service_branch, Rationale_for_waiver, Data_classification]
print(arr)