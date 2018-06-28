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
text_responce = []

def t_responce(rlist):
    global text_responce
    for x in range(0, len(rlist)):
        if rlist[x] == 10:
            text_responce.append("Yes")
        if rlist[x] == 0:
            text_responce.append("No")

t_responce(responces)

row = 0
col = 0

def output():
    global row
    global col
    workbook = xlsxwriter.Workbook('Results.xlsx')
    worksheet = workbook.add_worksheet()

    text = 'This is a Risk Scoring tool. Below you will find your basic information and score.'

    options = {
        'width': 256,
        'height': 100,
        'x_offset': 10,
        'y_offset': 10,

        'font': {'color': 'black',
                 'size': 14},
        'align': {'vertical': 'middle',
                 'horizontal': 'left'},
        'gradient': {'colors':['#DDEBCF', '#9CB86E', '#156B13']}
    }

    worksheet.insert_textbox('G2', text, options)
    #formating
    row += 2
    bold = workbook.add_format({'bold': 1})
    worksheet.write(row, col, "Questions", bold)
    worksheet.write(row, col + 1, "Answers", bold)
    worksheet.write(row, col + 2, "Weight Assigned", bold)
    worksheet.set_column('A:A', 15)
    row += 2

    worksheet.write(row, col, "Risk Score for the system", bold)
    worksheet.write_blank(row, col + 1, None)
    worksheet.write(row, col + 2, score)
    worksheet.write(row, col + 3, "/")
    worksheet.write(row, col + 4, "10")



    row += 5
    for x in range(0, len(weight)):
        worksheet.write(row, col    , arr[x][0])
        worksheet.write(row, col + 1, text_responce[x])
        worksheet.write(row, col + 2, int(weight[x]))
        row += 1



output()