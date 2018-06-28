import csv

weight = []
numquestions = 0
num = 0
y = 0
question = 0
choise = 0
numchoice = 0
arr = []
responces = [10, 0, 10]
trash = []
with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
    arr = list(readCSV)

print(arr)

# v gets inserted into num. This will add to the response list
def userresponce(num):
    global responces
    responces.append(num)

# insert
def num_of_choices(list):
    length = len(list)
    length -= 2
    return length


numquestions = len(arr)


def weight_list(list): #void
    global weight

    for x in range(0, len(list)):

        n = list[x][3]
        weight.append(n)

weight_list(arr)


# def score_math(wlist, rlist):
#     wt = 0
#     rt = 0
#     length = len(wlist)
#     for x in range(0, length):
#         wt += int(wlist[x])
#
#     print(wt)
#
#     for x in range(0, length):
#         rt += int(wlist[x]) * int(rlist[x])
#         final = rt / wt
#
#     print(final, "/", 10)
# score_math(weight, responces)


def score_math(wlist, rlist):
    wt = 0
    rt = 0
    length = len(wlist)
    for x in range(0, length):
        wt += int(wlist[x])

    print(wt)

    for x in range(0, length):
        rt += int(wlist[x]) * int(rlist[x])
        final = rt / wt

    return final
final = score_math(weight, responces)


row = 0
col = 0
text_responce = []

def t_responce(rlist):
    global text_responce
    for x in range(0, len(rlist)):
        if rlist[x] == 10:
            text_responce.append("Yes")
            print("yeeeet")
        if rlist[x] == 0:
            text_responce.append("No")
            print("nope")


t_responce(responces)


def output():
    global row
    global col
    workbook = xlsxwriter.Workbook('Results.xlsx')
    worksheet = workbook.add_worksheet()
    for x in range(0, len(weight)):
        worksheet.write(row, col    , arr[x][0])
        worksheet.write(row, col + 1, text_responce[x])
        worksheet.write(row, col + 2, weight[x])
        row += 1
    worksheet.write(row + 11, col + 2, final)
    worksheet.write(row + 11, col + 3, "/")
    worksheet.write(row + 11, col + 4, "10")

output()