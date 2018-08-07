

"""
Creation Date: 6/4/2018
Original Author: Christian Brenner, Matt Salvo, BMCS
Version Author:
Version:        0.3.1
Version Date:   7/31/2018
"""

"""
Description: This program is to take input from the user after asking questions and transform this data into a risk 
score. This risk score is scored against a baseline risk score that is pre set by admin. Both, Questions and Answers, 
are apart of a csv, in which the data in imputed. Making the program module with different systems or risk assessments. 
"""

"""
Wiki for XlsxWriter: https://xlsxwriter.readthedocs.io/
"""


####################
# RETRIVE EXTERNAL #
####################

import os
os.system('cls')
print(">Installing/Verifying Libraries")
os.system('pip install xlsxwriter csv')
print(">Installing/Verifying completed")
os.system('cls')


######################
# EXTERNAL LIBRARIES #
######################
from tkinter import *
from tkinter import messagebox
import csv
import xlsxwriter


####################
# GLOBAL VARIABLES #
####################

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
family = []
combolist = []
adj_weight = []
root = Tk()
v = IntVar()


##################
# CSV FILE INPUT #
##################

# for the baseline score
with open('nist_baseline.csv') as csvfile:
    readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
    arr = list(readCSV)

# for the user adjusted scores
with open('adjusted.csv') as wumbo:
    secondCSV = csv.reader(wumbo, skipinitialspace=True, delimiter=',')
    adjusted_import = list(secondCSV)




# Place holder for file drop down menu in the task bar
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


########################
# Excel Sheet Creation #
########################

workbook = xlsxwriter.Workbook('Results.xlsx')
worksheet = workbook.add_worksheet()
worksheet1 = workbook.add_worksheet('Chart')
bold = workbook.add_format({'bold': 1})
print(arr)

#############
# FUNCTIONS #
#############

# Responses from the GUI is saved and run in this function. This is a function that appends to the responses list.
def user_response(num):
    global responses
    responses.append(num)

# Function contains Basic_Information about the the system getting a risk score. This includes
# data that is transferred to the excel sheet with this information.
def basic_info():

    #Basic info varables with there locations are here

    name = "EMNS"
    description = "System to alert people"
    data_class = "Secret"
    date = "7/31/2018"
    assessor = "John Doe"
    worksheet.write('F8', "System Name:")
    worksheet.write('F9', "Description:")
    worksheet.write('F10', "Data Classification:")
    worksheet.write('F11', "Date of score:")
    worksheet.write('F12', "Assessor:")
    list1 =[name, description, data_class, date, assessor]
    options = {
        'width': 256,
        'height': 100,
        'font': {'color': 'black',
                 'size': 14},
        'colors': {'#DDEBCF'}
    }

    # Formatting settings for basic info including column width sizes.
    worksheet.write('G8', name, bold)
    worksheet.write('G9', description, bold)
    worksheet.write('G10', data_class, bold)
    worksheet.write('G11', date, bold)
    worksheet.write('G12', assessor, bold)
    worksheet.write('D1', 'Adjusted Weights', bold)
    worksheet.set_column('B:B', 10)
    worksheet.set_column('D:D', 15)
    worksheet.set_column('E:E', 4)
    worksheet.set_column('F:F', 18)


num_questions = len(arr)

# For loop function transferring the baseline list of weights from the CSV to a Weight only list
def weight_list(list): #void
    global weight

    for x in range(0, len(list)):

        n = list[x][4]
        weight.append(n)

# For loop function transferring the Adjusted user list of weights from the CSV to a Weight only list
def adj_weight_list(list): #void
    global adj_weight

    for x in range(0, len(list)):

        n = list[x][4]
        n = int(n)
        adj_weight.append(n)


weight_list(arr)
adj_weight_list(adjusted_import)

# The equation for calculating the risk score. Wlist is the input for Weight and Rlist is for the responses.
# Wlist should be the only list to change for both of the scores
def score_math(wlist, rlist):
    wt = 0
    rt = 0
    length = len(wlist)
    for x in range(0, length):
        wt += float(wlist[x])

    print(wt)

    for x in range(0, length):
        rt += int(wlist[x]) * int(rlist[x])
        final = rt / wt

    return final


def label_creation():
    global n
    n=0
    global question
    if n < len(weight):
        question = Label(root, text=arr[n][1], font=32, wraplength=600)
        question.grid(row=0, column=0, sticky=W, pady=25)
        n += 1


label_creation()
n = 0


def radio_creation():

    Radiobutton(root, text="Yes", font=16, variable=v, value=0).place(relx=.1, rely=.5, anchor="w")
    Radiobutton(root, text="No", font=16, variable=v, value=10).place(relx=.1, rely=.6, anchor="w")

radio_creation()


def next():
    global n
    global j
    global window_counter
    global question

    temp = v.get()
    user_response(temp)


    n += 1
    j += 1

    if n == len(arr):
        output_window = Toplevel(root)
        output_window.config(menu=menu_bar)
        output_window.geometry("600x300+0+0")
        output_window.title("RAST")

        risk_score = Label(output_window, text="The risk score is:", font=32)
        risk_score.grid(row=0, column=0, sticky=W, pady=20)
        risk_score = Label(output_window, text=round(score_math(weight, responses), 2), font=32)
        risk_score.grid(row=0, column=0, sticky=E, pady=20)
        risk_score = Label(output_window, text="/ 10", font=32)
        risk_score.grid(row=0, column=1, sticky=W, pady=20)

        risk_score = Label(output_window, text="The adjusted risk score is:", font=32)
        risk_score.grid(row=1, column=0, sticky=W, pady=20)
        risk_score = Label(output_window, text=round(score_math(adj_weight, responses), 2), font=32)
        risk_score.grid(row=1, column=0, sticky=E, pady=20)
        risk_score = Label(output_window, text="/ 10", font=32)
        risk_score.grid(row=1, column=1, sticky=W, pady=20)

        output_message = Label(output_window, text="Your responses and the risk score have been saved\nto an Excel file"
                                                   "named Results.xlsx", font=32)
        output_message.grid(row=2, column=0, sticky=W)

        btnQuit = Button(output_window, text="Quit", command=root.destroy, height=1, width=10)
        btnQuit.grid(row=3, column=0, pady=40)


    question.config(text=arr[n][1])
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
    question.config(text=arr[n][1])
    question.grid(row=0, column=0, sticky=W, pady=25)


btnNext = Button(root, text="Next", command=next, height=1, width=10)
btnNext.place(relx=.6, rely=.8, anchor="sw")

btnPrevious = Button(root, text="Previous", command=previous, height=1, width=10)
btnPrevious.place(relx=.4, rely=.8, anchor="se")


# window = new_window()


root.mainloop()

text_response = []

# makes a list that changes the numeral answers provided in responses to a text based answer for the excel workbook
def t_response(rlist):
    global text_response
    for x in range(0, len(rlist)):
        if rlist[x] == 0:
            text_response.append("Yes")
        if rlist[x] == 10:
            text_response.append("No")


t_response(responses)


row = 0
col = 0

print(responses)

score = round(score_math(weight, responses), 2) # Calulates base line score


adj_score = round(score_math(adj_weight, responses), 2)   # calulates user adjusted score

# Function is the main source for outputting the data gathered to the excel sheet. Also includes formatting.
def output():
    global row
    global col
    global workbook
    global worksheet
    global bold
    global adj_score
    global adj_weight
    print("check me Output")
    text = 'This is a Risk Scoring tool. Below you will find your basic information and score.'

    # option created for the text box for absences and formatting
    options = {
        'width': 256,
        'height': 100,

        'font': {'color ': 'black',
                 'size': 14},

        'colors': {'#DDEBCF'},
        'line': {'color': '#ff9900', 'width': 1.5, 'dash_type': 'square_dot'}
    }

    # Placing the Basic_info before the data gathered for simplicity.
    basic_info()

    worksheet.insert_textbox('G2', text, options)
    worksheet.write(row, col, "Controls", bold)
    worksheet.write(row, col + 1, "Answers", bold)
    worksheet.write(row, col + 2, "Baseline Weight", bold)
    worksheet.set_column('A:A', 15)
    worksheet.set_column('C:C', 15)
    row += 2
    worksheet.write('G14', "Baseline Score for the system", bold)
    worksheet.write('G15', "Adjusted Score for the system", bold)
    worksheet.write_blank('H14', None)
    worksheet.write_blank('H15', None)
    worksheet.write('J15', adj_score)
    worksheet.write('J14', score)
    worksheet.write('K14', "/")
    worksheet.write('K15', "/")
    worksheet.write('L14', int("10"))
    worksheet.write('L15', int("10"))

    row += 5
    # for loop placing the Weights, answers, and controls into the excel sheet
    for x in range(0, len(weight)):

        rome = text_response[x]
        worksheet.write(row, col    , arr[x][0])
        worksheet.write(row, col + 1, rome)
        worksheet.write(row, col + 2, int(weight[x]))
        worksheet.write(row, col + 3, adj_weight[x])
        row += 1


def sort(flist, rlist):
    for x in sorted(flist):
        print('x')


def combo(flist, rlist):
    global combolist
    for x in range(len(rlist)):
        combolist = list[x].append(flist[x])

# settings for the chart, including the data cells of the series, also appearance.
def chart():
    global workbook
    global worksheet1
    global bold

    # data to be plotted
    # Create a new chart object
    steve = workbook.add_chart({'type': 'column'})
    steve.set_title ({'name': 'Results of Risk Score'})

    steve.set_x_axis ({'name': 'Risk Score'})
    steve.set_y_axis ({'name': 'Family'})

    # add a series to the chart
    steve.add_series({'values': '=Sheet1!$j$14:$j$14', 'fill': {'color': 'green'},
                      'border': {'color': 'black'},
                      'name': 'Baseline'})
    steve.add_series({'values': '=Sheet1!$j$15:$j$15', 'fill': {'color': 'blue'},
                      'border': {'color': 'black'},
                      'name': 'Adj User'})

    # insert the chart into the worksheet
    worksheet.insert_chart('G20', steve)
    workbook.close()

# main

output()
chart()
workbook.close()