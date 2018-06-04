# This will be the quetions that will be asked

System_name = input('Enter System Name: ')
#test block
System_status = input('Please Chose the coresponding number for your system status.'
                      '1. Pre-Milestone , '
                      '2. LIRP: ')
Authorizing_official = input('Please enter Authorizing Official: ')
Service_branch = input('Please Select Branch: '
                       '1. Army , '
                       '2. Navy , '
                       '3. Air Force: ')
Rationale_for_waiver = input('Im lazy')
Data_classification = input('Please Select Data Classification: '
                            '1. U , '
                            '2. S , '
                            '3. TS: ')
Connectivity = input('Please Select connectivity to the internet: '
                     '1. Open Network - Commercial ISP , '
                     '2. Open Network - .edu , '
                     '3. Open Network - NIPR , '
                     '4. Closed Restricted Network - SIPRNET , '
                     '5. Closed Restricted Network - JWICS , '
                     '6. Closed Restricted Network - SAP/SAR , '
                     '7. Closed Restricted Network - Other , '
                     '8. Standalone Network , '
                     '9. Standalone System - With Media , '
                     '10. Standalone System - No Media: ')
System_fielded = input('Please select how many systems are fielded: '
                       '1. 1-10 , '
                       '2. 11-50 , '
                       '3. 51-100 , '
                       '4. 101-500 , '
                       '5. 501+: ')
Email = input('Are users able to email?: '
              '1. Yes , '
              '2. No: ')
Web = input('Are users able to use a web browser?: '
            '1. Yes , '
            '2. No: ')
Admin_privileges = input('What kind of users are logged on as?: '
                         '1. User , '
                         '2. Admin - Partial privileges , '
                         '3. Admin - Elevated privileges , '
                         '4. Does not Apply: ')
TFA = input('Does the system have PIK or TFA?: '
            '1. Yes , '
            '2. No , '
            '3. Does not Apply: ')
App_whitelist = input('Use a App whitelisting capability?: '
                      '1. Yes , '
                      '2. No , '
                      '3. Does not Apply: ')
Host_protection = input('Uses Host Based Protection?: '
                        '1. Yes , '
                        '2. No , '
                        '3. Does Not Apply: ')
Hard_ports = input('Are the unused ports (Ethernet/USB) disabled on the system?: '
                   '1. Yes , '
                   '2. No , '
                   '3. Does Not Apply: ')
STIGs = input('Have any STIGs been run on the system?: '
              '1. Yes , '
              '2. No , '
              '3. Does Not Apply: ')
Encryption = input('Is ecnryption at rest?: '
                   '1. Yes , '
                   '2. No , '
                   '3. Does Not Apply: ')
Owner = input('System Owner Approval Justification Discussion: ')
System_ato_date = input('Please enter System ATO Date in MM/DD/YYYY Format: ')
Anticipated_ato_date = input("Please Enter Anticipated ATO Date in MM/DD/YYYY Format: ")
MIC = input('Please Enter Mission Impact if Compromised: '
            '1. Very High , 2. High , 3. Moderate , 4. Low , 5. Very Low: ')
ISC = input('Please Enter Impact to the System if Compromised: '
            '1. Very High , 2. High , 3. Moderate , 4. Low , 5. Very Low: ')
print('Additional Testing: Please leave this section blank')
Testing = input('Has any Testing been compleated?: '
                '1. Yes - Vulnerability , 2. Yes - Penetration , 3. Yes - Adversary , 4. No: ')
SMI = input('Were security measures implemented?: '
            '1. Yes , 2. No , 3. Does Not Apply: ')
ExSMI = input('If yes to the prevous question please enter a discription: ')
Funding = input('Is Funding Available: '
                '1. Yes , 2. No , 3. Does Not Apply: ')
When_funding = input('When will funding be available?: (Please enter in MM/DD/YYYY format): '#