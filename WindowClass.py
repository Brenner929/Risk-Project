from tkinter import *
import csv

weight = []
numquestions = 0
num = 0
y = 0
question = 0
choise = 0
numchoice = 0
arr = []
responses = []
trash = []
n = 0
j = 0

root = Tk()
root.withdraw()

# Responses: These are the responses to the question. Stored as a location in memory
v = IntVar()

current_window = None

with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
    arr = list(readCSV)


# v gets inserted into num. This will add to the response list
def userresponce(num):
    global responses
    responses.append(num)


# insert
def num_of_choices(list):
    length = len(list)
    length -= 1
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


def hello():
    print("hello!")

menubar = Menu(root)
menubar.add_command(label="Hello", command=hello)
menubar.add_command(label="Quit", command=root.quit)


def previous():
    print("Previous!")


def replace_window(root):
    # Destroy current window, create new window
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = Toplevel(root)

    # if the user kills the window via the window manager,
    # exit the application.
    current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)

    return current_window


counter = 0


def new_window():
    global counter
    counter += 1

    window = replace_window(root)
    window.config(menu=menubar)
    window.geometry("500x300+0+0")
    window.title("IRAT")

    # Label: This is where the questions will go

    def label_creation():
        #count = Label(window, text=counter)
        #count.grid(row=1, column=1, pady=25)
        global n
        question = Label(window, text=arr[n][0], font=32)
        question.grid(row=0, column=0, sticky=W, pady=25)
        n += 1

    label_creation()

    def radio_creation():
        global j
        vcount = 0
        rcount = 1
        #choice = ["One", "Two", "Three"]
        for x in range(1, num_of_choices(arr[j])):
            Radiobutton(window, text=arr[j][x], font=16, variable=v, value=vcount).grid(row=rcount, column=0, sticky=W)
            vcount += 1
            rcount += 1
        j += 1


    radio_creation()

    btnNext = Button(window, text="Next", command=new_window, height=1, width=10)
    btnNext.grid(row=9, column=2, pady=40)

    btnPrevious = Button(window, text="Previous", command=previous, height=1, width=10)
    btnPrevious.grid(row=9, column=0, pady=40)

    global responses
    global v
    temp = v.get()
    userresponce(temp)
    print(responses)


window = new_window()


root.mainloop()
