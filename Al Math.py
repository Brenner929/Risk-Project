#__import__(Main)

# Connectivity = int(input('Please Select connectivity to the internet: '
#                      '1. Open Network - Commercial ISP, '
#                      '2. Open Network - .edu , '
#                      '3. Open Network - NIPR , '
#                      '4. Closed Restricted Network - SIPRNET , '
#                      '5. Closed Restricted Network - JWICS , '
#                      '6. Closed Restricted Network - SAP/SAR , '
#                      '7. Closed Restricted Network - Other , '
#                      '8. Standalone Network , '
#                      '9. Standalone System - With Media , '
#                      '10. Standalone System - No Media: '))
# Connectivity = 10 - Connectivity

Admin_privileges = int(input('What kind of users are logged on as?: '
                         '1. User , '
                         '2. Admin - Partial privileges , '
                         '3. Admin - Elevated privileges , '
                         '4. Does not Apply: '))

# Fixes the numbering issue so 1 = 0, 2 = 1 , 3 = 2, and 4 = 0;
# Admin_privileges -= 1
# if(Admin_privileges == 3):
#     Admin_privileges = 0
# print(Admin_privileges)


# def Maths(num):
#     num -= 1
#     if (num == 3):
#         num = 0
#     return num
#
# TFA = int(input('Does the system have PIK or TFA?: '
#             '1. Yes , '
#             '2. No , '
#             '3. Does not Apply: '))
# TFA = Maths(num=TFA)
# print(TFA)

Testing = int(input('Has any Testing been compleated?: '
                '1. Yes - Vulnerability , 2. Yes - Penetration , 3. Yes - Adversary , 4. No: '))
if(Testing == 4):
    Testing = 0
else:
    Testing = Testing * -5

print(Testing)

Funding = int(input('Is Funding Available: '
                '1. Yes , 2. No , 3. Does Not Apply: '))
# Runt += Funding
Funding -= 1
if (Funding == 1) or (Funding == 0):
    When_funding = input('When will funding be available?: (Please enter in MM/DD/YYYY format)')

print(Funding)





