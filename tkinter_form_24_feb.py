from tkinter import *


qs = []
with open("form_questions") as reader:
	for line in reader.readlines():
		qs.append(line.strip())


class Status():
	status = None

def yes_page1():
    Status.status = "safe"
    # print("yes", Status.status)
    page1.destroy()
    submitpage2()

def no_page1():
    Status.status = "not safe"
    # print("no", Status.status)
    page1.destroy()
    submitpage2()

def yes_page2():
    Status.status = "not safe"
    # print("yes", Status.status)
    page2.destroy()
    submitpage3()

def no_page2():
    # status = "safe"
    # print("no", Status.status)
    page2.destroy()
    submitpage3()

def yes_page3():
    Status.status = "not safe"
    # print("yes", Status.status)
    page3.destroy()
    submitpage4()

def no_page3():
    # status = "safe"
    # print("no", Status.status)
    page3.destroy()
    submitpage4()

def yes_page4():
    Status.status = "not safe"
    # print("yes", Status.status)
    page4.destroy()

def no_page4():
    # status = "safe"
    # print("no", Status.status)
    page4.destroy()


def submitpage1():
    # output =
    global page1 
    page1 = Tk()
    page1.geometry("1280x720")
    page1.configure(background='white')
    page1.title("Question 1")
    Label(page1, text= qs[0], width = 40, font=("Courier", 50 )).grid(row=0,column=0)
    yes = Button(page1, text = "Yes", command = yes_page1,height = 10, width = 40, bg = "black", fg = "white").place(x=340, y=500)
    no = Button(page1, text = "No", command = no_page1,height = 10,  width = 40, bg = "black", fg = "white").place(x=700, y=500)
    # yes.grid(row = 12, column = 11)
    # no.grid(row = 15, column = 11)

def submitpage2():
    global page2
    page2 = Tk()
    page2.geometry("1280x720") 
    page2.configure(background='white')
    page2.title("Question 2")
    Label(page2, text= qs[1],width = 40, font=("Courier", 50 )).grid(row=0,column=0)
    yes = Button(page2, text = "Yes", command = yes_page2,height = 10, width = 40, bg = "black", fg = "white").place(x=340, y=500)
    no = Button(page2, text = "No", command = no_page2, height = 10, width = 40, bg = "black", fg = "white").place(x=700, y=500)
    # yes.grid(row = 70, column = 0)
    # no.grid(row = 70, column = 0)


def submitpage3():
    global page3
    page3 = Tk()
    page3.geometry("1280x720")
    page3.configure(background='white') 
    page3.title("Question 3")
    Label(page3, text= qs[2], width = 40, font=("Courier", 50 )).grid(row=0,column=0)
    yes = Button(page3, text = "Yes", command = yes_page3, height=10, width = 40, bg = "black", fg = "white").place(x=340, y=500)
    no = Button(page3, text = "No", command = no_page3,height=10, width = 40, bg = "black", fg = "white").place(x=700, y=500)
    # yes.grid(row = 12, column = 11)
    # no.grid(row = 15, column = 11)


def submitpage4():
    global page4
    page4 = Tk()
    page4.geometry("1280x720")
    page4.configure(background='white')
    page4.title("Question 4")
    Label(page4, text= qs[3], width = 40, font=("Courier", 50 )).grid(row=0,column=0)
    yes = Button(page4, text = "Yes", command = yes_page4, height=10, width = 40, bg = "black", fg = "white").place(x=340, y=500)
    no = Button(page4, text = "No", command = no_page4, height = 10, width = 40, bg = "black", fg = "white").place(x=700, y=500)
    # yes.grid(row = 12, column = 11)
    # no.grid(row = 15, column = 11)



if __name__ == "__main__":
	submitpage1()
	mainloop()
