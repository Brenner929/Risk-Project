import os
os.system('cls')
print(">Installing/Verifying Libraries")
os.system('pip install xlsxwriter')
print(">Installing/Verifying completed")
os.system('cls')

from tkinter import *
from tkinter import messagebox
import csv
import xlsxwriter

weight = []
num_questions = 0
num = 0
y = 0
question = 0
choice = 0
num_choice = 0
arr = []
responses = []
trash = []
n = 0
j = 0
window_counter = 0

root = Tk()


def hello():
    print("hello!")


menu_bar = Menu(root)
menu_bar.add_command(label="Hello", command=hello)
menu_bar.add_command(label="Quit", command=root.quit)
root.config(menu=menu_bar)
root.geometry("600x300+0+0")
root.title("RAST")
background_image = PhotoImage(file='Logo1.gif')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#root.withdraw()

# Responses: These are the responses to the question. Stored as a location in memory
v = IntVar()

# current_window = None

with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
    arr = list(readCSV)


# v gets inserted into num. This will add to the response list
def user_response(num):
    global responses
    responses.append(num)


# insert
def num_of_choices(list):
    length = len(list)
    length -= 1
    return length


num_questions = len(arr)


def weight_list(list): #void
    global weight

    for x in range(0, len(list)):

        n = list[x][3]
        weight.append(n)


weight_list(arr)


def score_math(wlist, rlist):
    wt = 0
    rt = 0
    length = len(wlist)
    for x in range(0, length):
        wt += float(wlist[x])

    print(wt)

    for x in range(0, length):
        rt += float(wlist[x]) * float(rlist[x])
        final = rt / wt

    return final


#def replace_window(root):
    # Destroy current window, create new window
    # global current_window
    # if current_window is not None:
    #     current_window.destroy()
    # current_window = Toplevel(root)
    #
    # # if the user kills the window via the window manager,
    # # exit the application.
    # current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)
    #
    # return current_window


# def new_window():
# global window_counter
# window_counter += 1



#print(responses)


    # Label: This is where the questions will go


def label_creation():
    global n
    global question
    if n <= len(weight):
        question = Label(root, text=arr[n][0], font=32)
        question.grid(row=0, column=0, sticky=W, pady=25)
        n += 1


label_creation()


def radio_creation():
    global j
    vcount = 0
    rcount = 1
    if n <= len(weight):
        for x in range(1, num_of_choices(arr[j])):
            Radiobutton(root, text=arr[j][x], font=16, variable=v, value=vcount).grid(row=rcount, column=0, sticky=W)
            vcount += 10
            rcount += 1
        j -= 1


radio_creation()


def next():
    global n
    global j
    global window_counter
    global question

    temp = v.get()
    user_response(temp)

    if n >= len(arr):
        output_window = Toplevel(root)
        output_window.config(menu=menu_bar)
        output_window.geometry("600x300+0+0")
        output_window.title("RAST")

        risk_score = Label(output_window, text="The risk score is:", font=32)
        risk_score.grid(row=0, column=0, sticky=W, pady=40)
        risk_score = Label(output_window, text=round(score_math(weight, responses), 2), font=32)
        risk_score.grid(row=0, column=0, sticky=E, pady=40)
        risk_score = Label(output_window, text="/ 10", font=32)
        risk_score.grid(row=0, column=1, sticky=W, pady=40)

        output_message = Label(output_window, text="Your responses and the risk score have been saved\nto an Excel file"
                                                   "named Results.xlsx", font=32)
        output_message.grid(row=1, column=0, sticky=W)

        btnQuit = Button(output_window, text="Quit", command=root.destroy, height=1, width=10)
        btnQuit.grid(row=2, column=0, pady=40)

    n += 1
    j += 1
    question.config(text=arr[n][0])
    question.grid(row=0, column=0, sticky=W, pady=25)

    print(n)
    print(len(arr))
    print(responses)
    print(weight)


def previous():
    global n
    global j
    global question
    n -= 1
    j -= 1
    question.config(text=arr[n][0])
    question.grid(row=0, column=0, sticky=W, pady=25)


btnNext = Button(root, text="Next", command=next, height=1, width=10)
btnNext.grid(row=9, column=1, padx=25, pady=40)

btnPrevious = Button(root, text="Previous", command=previous, height=1, width=10)
btnPrevious.grid(row=9, column=0, padx=25, pady=40)


# window = new_window()


root.mainloop()




text_response = []


def t_response(rlist):
    global text_response
    for x in range(0, len(rlist)):
        if rlist[x] == 10:
            text_response.append("Yes")
        if rlist[x] == 0:
            text_response.append("No")


t_response(responses)


row = 0
col = 0

print(responses)

score = round(score_math(weight, responses), 2)

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
    # formatting
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
        worksheet.write(row, col + 1, text_response[x])
        worksheet.write(row, col + 2, int(weight[x]))
        row += 1


output()
# def output():
#     global row
#     global col
#     global score
#     workbook = xlsxwriter.Workbook('Results.xlsx')
#     worksheet = workbook.add_worksheet()
#     for x in range(0, len(weight)):
#         worksheet.write(row, col    , arr[x][0])
#         worksheet.write(row, col + 1, text_response[x])
#         worksheet.write(row, col + 2, weight[x])
#         row += 1
#     worksheet.write(row + 11, col + 2, score)
#     worksheet.write(row + 11, col + 3, "/")
#     worksheet.write(row + 11, col + 4, "10")
#
# output()
