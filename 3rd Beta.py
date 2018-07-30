
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
family = []
combolist = []
adj_weight = []


root = Tk()
v = IntVar()

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

# current_window = None

with open('nist_baseline.csv') as csvfile:
    readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
    arr = list(readCSV)


with open('adjusted.csv') as wumbo:
    secondCSV = csv.reader(wumbo, skipinitialspace=True, delimiter=',')
    adjusted_import = list(secondCSV)

 ###- Responce Test -###
# with open('Responces.csv') as csvtest:
#     rcsv = csv.reader(csvtest, skipinitialspace=True, delimiter=',')
#     responces = list(rcsv)


workbook = xlsxwriter.Workbook('Steve.xlsx')
worksheet = workbook.add_worksheet()
worksheet1 = workbook.add_worksheet('Chart')
bold = workbook.add_format({'bold': 1})
print(arr)

# v gets inserted into num. This will add to the response list
def user_response(num):# Same as User just with _
    global responses
    responses.append(num)


# insert
def num_of_choices(list):
    length = len(list)
    length -= 2
    return length

def basic_info():

    name = "System Name"
    description = "Description"
    data_class = "Data Classification"
    date = "Date of score"
    assessor = "Assessor"
    worksheet.write('F8', "System Name:")
    worksheet.write('F9', "Description:")
    worksheet.write('F10', "Data Classification:")
    worksheet.write('F11', "Date of score:")
    worksheet.write('F12', "Assessor:")
    list1 =[name, description, data_class, date, assessor]
    options = {
        'width': 256,
        'height': 100,
        # 'x_offset': 10,
        # 'y_offset': 10,

        'font': {'color': 'black',
                 'size': 14},
        # 'align': {'vertical': 'middle',
        #          'horizontal': 'left'},
        'colors': {'#DDEBCF'}
    }

    # ('A:A', 15)
    worksheet.write('G8', name, bold)
    worksheet.write('G9', description, bold)
    worksheet.write('G10', data_class, bold)
    worksheet.write('G11', date, bold)
    worksheet.write('G12', assessor, bold)
    worksheet.write('E1', 'User Weights', bold)
    worksheet.set_column('B:B', 10)
    worksheet.set_column('D:D', 15)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('F:F', 18)


num_questions = len(arr)


def weight_list(list): #void
    global weight

    for x in range(0, len(list)):

        n = list[x][4]
        weight.append(n)


def adj_weight_list(list): #void
    global adj_weight

    for x in range(1, len(list)):

        n = list[x][4]
        n = int(n)
        adj_weight.append(n)

weight_list(arr)


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
        question = Label(root, text=arr[n][1], font=32)
        question.grid(row=0, column=0, sticky=W, pady=25)
        n += 1



label_creation()
n = 0

def radio_creation():
    # global j
    # vcount = 0
    # rcount = 1
    # if n <= len(weight):
    #     for x in range(1, num_of_choices(arr[j])):
    #         Radiobutton(root, text=arr[j][x], font=16, variable=v, value=vcount).grid(row=rcount, column=0, sticky=W)
    #         vcount += 10
    #         rcount += 1
    #     j -= 1
    Radiobutton(root, text="Yes", font=16, variable=v, value=0).grid(row=2, column=0, sticky=W)
    Radiobutton(root, text="No", font=16, variable=v, value=10).grid(row=3, column=0, sticky=W)

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

score = round(score_math(weight, responses), 2) # Calulates base line score

adj_weight_list(adjusted_import)

adj_score = round(score_math(adj_weight, responses), 2)   # calulates user adjusted score




def output():
    global row
    global col
    global workbook
    global worksheet
    global bold
    global adj_score
    print("check me Output")
    text = 'This is a Risk Scoring tool. Below you will find your basic information and score.'

    options = {
        'width': 256,
        'height': 100,
        # 'x_offset': 10,
        # 'y_offset': 10,

        'font': {'color': 'black',
                 'size': 14},
        # 'align': {'vertical': 'middle',
        #          'horizontal': 'left'},
        'colors': {'#DDEBCF'},
        'line': {'color': '#ff9900', 'width': 1.5, 'dash_type': 'square_dot'}
    }

    basic_info()

    worksheet.insert_textbox('G2', text, options)
    #formating
    # row += 4

    worksheet.write(row, col, "Baseline", bold)
    worksheet.write(row, col + 1, "Answers", bold)
    worksheet.write(row, col + 2, "Weight Assigned", bold)
    worksheet.set_column('A:A', 15)
    row += 2

    worksheet.write('G14', "Baseline Score for the system", bold)
    worksheet.write('G15', "Adjusted Score for the system", bold)
    worksheet.write_blank('H14', None)
    worksheet.write_blank('H15', None)
    worksheet.write('J14', adj_score)
    worksheet.write('J15', score)
    worksheet.write('K14', "/")
    worksheet.write('K15', "/")
    worksheet.write('L14', int("10"))
    worksheet.write('L15', int("10"))



    row += 5
    for x in range(0, len(weight)):

        rome = responses[x]
        rome = int(rome)
        worksheet.write(row, col    , arr[x][0])
        worksheet.write(row, col + 1, rome)
        worksheet.write(row, col + 2, int(weight[x]))
        row += 1

def sort(flist, rlist):
    for x in sorted(flist):
        print('x')


def combo(flist, rlist):
    global combolist
    for x in range(len(rlist)):
        combolist = list[x].append(flist[x])


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
                      'border': {'color': 'black'}})
    steve.add_series({'values': '=Sheet1!$j$15:$j$15', 'fill': {'color': 'red'},
                      'border': {'color': 'black'}})

    # insert the chart into the worksheet
    worksheet.insert_chart('G20', steve)
    workbook.close()

print('Check me')

output()
chart()
workbook.close()