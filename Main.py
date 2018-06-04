
# DOES NOT APPLY does not work untill it is switched to option 0
# This will be the quetions that will be asked
Runt = 0
Total = 0
Xvalue = 0

System_name = input('Enter System Name: ')
#test block
System_status = int(input('Please Chose the coresponding number for your system status.'
                      '1. Pre-Milestone , '
                      '2. LIRP: '))
Runt += System_status

Authorizing_official = input('Please enter Authorizing Official: ')

Service_branch = int(input('Please Select Branch: '
                       '1. Army , '
                       '2. Navy , '
                       '3. Air Force: '))

Rationale_for_waiver = input('Im lazy')

Data_classification = int(input('Please Select Data Classification: '
                            '1. U , '
                            '2. S , '
                            '3. TS: '))
Runt += Data_classification

Connectivity = int(input('Please Select connectivity to the internet: '
                     '1. Open Network - Commercial ISP , '
                     '2. Open Network - .edu , '
                     '3. Open Network - NIPR , '
                     '4. Closed Restricted Network - SIPRNET , '
                     '5. Closed Restricted Network - JWICS , '
                     '6. Closed Restricted Network - SAP/SAR , '
                     '7. Closed Restricted Network - Other , '
                     '8. Standalone Network , '
                     '9. Standalone System - With Media , '
                     '10. Standalone System - No Media: '))
Runt += Connectivity

System_fielded = int(input('Please select how many systems are fielded: '
                       '1. 1-10 , '
                       '2. 11-50 , '
                       '3. 51-100 , '
                       '4. 101-500 , '
                       '5. 501+: '))
Runt += System_fielded

Email = int(input('Are users able to email?: '
              '1. Yes , '
              '2. No: '))
Runt += Email

Web = int(input('Are users able to use a web browser?: '
            '1. Yes , '
            '2. No: '))
Runt += Web

Admin_privileges = int(input('What kind of users are logged on as?: '
                         '1. User , '
                         '2. Admin - Partial privileges , '
                         '3. Admin - Elevated privileges , '
                         '4. Does not Apply: '))
Runt += Admin_privileges

TFA = int(input('Does the system have PIK or TFA?: '
            '1. Yes , '
            '2. No , '
            '0. Does not Apply: '))
Runt += TFA

App_whitelist = int(input('Use a App whitelisting capability?: '
                      '1. Yes , '
                      '2. No , '
                      '0. Does not Apply: '))
Runt += App_whitelist

Host_protection = int(input('Uses Host Based Protection?: '
                        '1. Yes , '
                        '2. No , '
                        '0. Does Not Apply: '))
Runt += Host_protection

Hard_ports = int(input('Are the unused ports (Ethernet/USB) disabled on the system?: '
                   '1. Yes , '
                   '2. No , '
                   '0. Does Not Apply: '))
Runt += Hard_ports

STIGs = int(input('Have any STIGs been run on the system?: '
              '1. Yes , '
              '2. No , '
              '0. Does Not Apply: '))
Runt += STIGs

Encryption = int(input('Is ecnryption at rest?: '
                   '1. Yes , '
                   '2. No , '
                   '0. Does Not Apply: '))
Runt += Encryption

Owner = input('System Owner Approval Justification Discussion: ')

System_ato_date = input('Please enter System ATO Date in MM/DD/YYYY Format: ')

Anticipated_ato_date = input("Please Enter Anticipated ATO Date in MM/DD/YYYY Format: ")

MIC = int(input('Please Enter Mission Impact if Compromised: '
            '4. Very High , 3. High , 2. Moderate , 1. Low , 0. Very Low: '))
Xvalue = MIC

ISC = int(input('Please Enter Impact to the System if Compromised: '
            '4. Very High , 3. High , 2. Moderate , 1. Low , 0. Very Low: '))

if Xvalue <= ISC:
    Xvalue = ISC

print('Additional Testing: Please leave this section blank')

Testing = int(input('Has any Testing been compleated?: '
                '1. Yes - Vulnerability , 2. Yes - Penetration , 3. Yes - Adversary , 4. No: '))




Runt += Testing

SMI = int(input('Were security measures implemented?: '
            '1. Yes , 2. No , 0. Does Not Apply: '))
Runt += SMI

ExSMI = input('If yes to the prevous question please enter a discription: ')

Funding = int(input('Is Funding Available: '
                '1. Yes , 2. No , 0. Does Not Apply: '))
Runt += Funding

When_funding = input('When will funding be available?: (Please enter in MM/DD/YYYY format)')

Answer = 0
Answer = Runt * 5
print('This is the Total Score: ' + str(Answer))
print('This is the Colum Number: ' + str(Xvalue))




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
