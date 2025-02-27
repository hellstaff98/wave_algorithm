from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

# doing all things automatically
def auto():
    global hm, end, the_path, k, v, bb, h, length
    hm += 1
    sp = int(scale.get())
    if m[end[0]][end[1]] == 0 :
        step(hm)
        if h != 0:
            win.after(sp, auto)
    else:
        v, bb = end
        k = m[v][bb]
        length = k - 1
        # the_path = [(v, bb)]
        fp_a()
        but1.config(command=fp)
    win.focus()

# repeating finding_path() automatically
def fp_a():
    global length
    sp = int(scale.get())
    path_identification()
    if k > 1:
        win.after(sp, fp_a)
    else:
        showinfo('Info', "I've found the way out! \nLength is {}".format(length))
        but1.config(state=DISABLED)
        but2.config(state=DISABLED)


# repeating finding_path()
def fp():
    if k == 1:
        but1.config(state=DISABLED)
    else:
        path_identification()
    win.focus()

def path_identification():
    global the_path, k, v, bb
    if v > 0 and m[v - 1][bb] == k - 1:
        v, bb = v - 1, bb
        #the_path.append((v, bb))

        k += - 1
    elif bb > 0 and m[v][bb - 1] == k - 1:
        v, bb = v, bb - 1
        #the_path.append((v, bb))

        k += - 1
    elif v < len(m) - 1 and m[v + 1][bb] == k - 1:
        v, bb = v + 1, bb
        #the_path.append((v, bb))

        k += - 1
    elif bb < len(m[v]) - 1 and m[v][bb + 1] == k - 1:
        v, bb = v, bb + 1
        #the_path.append((v, bb))

        k += - 1
    box.itemconfig(res[0] * v + bb + 1, fill='#1E90FF')

# doing one step until 'end' isn't zero
def one():
    global hm, end, k, v, bb, length
    #hm += 1

    if m[end[0]][end[1]] == 0:
        step(hm)
        # win.after(10, auto)
        hm += 1
    else:
        v, bb = end
        k = m[v][bb]
        length = k - 1

        fp()
        but1.config(command=fp)
    win.focus()


def step(k):
    global m, h
    h = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if m[i - 1][j] == 0 and (field[i - 1][j] == '0' or field[i - 1][j] == 'f'):
                    m[i - 1][j] = k + 1
                    h += 1
                    if field[i-1][j] == 'f':
                        box.itemconfig(res[0]*(i-1)+(j+1), fill='#1E90FF')
                    else:
                        box.itemconfig(res[0]*(i-1)+(j+1), fill='red')
                    box.create_text(j * each + 10 + each * 0.5, (i-1) * each + 10 + each*0.5, text=k)
                if m[i][j - 1] == 0 and (field[i][j - 1] == '0' or field[i][j - 1] == 'f'):
                    m[i][j - 1] = k + 1
                    h += 1
                    if field[i][j - 1] == 'f':
                        box.itemconfig(res[0] * i + j, fill='#1E90FF')
                    else:
                        box.itemconfig(res[0] * i + j, fill='red')
                    box.create_text((j-1) * each + 10 + each * 0.5, i * each + 10 + each * 0.5, text=k)
                if m[i + 1][j] == 0 and (field[i + 1][j] == '0' or field[i + 1][j] == 'f'):
                    m[i + 1][j] = k + 1
                    h += 1
                    if field[i + 1][j] == 'f':
                        box.itemconfig(res[0] * (i + 1) + (j + 1), fill='#1E90FF')
                    else:
                        box.itemconfig(res[0] * (i+1) + j+1, fill='red')
                    box.create_text(j * each + 10 + each * 0.5, (i + 1) * each + 10 + each * 0.5, text=k)
                if m[i][j + 1] == 0 and (field[i][j + 1] == '0' or field[i][j + 1] == 'f'):
                    m[i][j + 1] = k + 1
                    h += 1
                    if field[i][j + 1] == 'f':
                        box.itemconfig(res[0] * i + (j + 2), fill='#1E90FF')
                    else:
                        box.itemconfig(res[0] * i + (j+2), fill='red')
                    box.create_text((j+1) * each + 10 + each*0.5, i * each + 10 + each*0.5, text=k)
    if h == 0:
        showerror('Error', "I can't find the way out :(")
        but1.config(state=DISABLED)
        but2.config(state=DISABLED)

def drawing():
    global start, end
    for y in range(res[1]):
        for x in range(res[0]):
            if field[y][x] == '1':
                grid.append(box.create_rectangle(x * each, y * each, x * each + each, y * each + each, fill='#69291c',
                                                 outline='grey'))
            elif field[y][x] == '0':
                grid.append(box.create_rectangle(x * each, y * each, x * each + each, y * each + each, fill='#82c4fe',
                                                 outline='grey'))
            elif field[y][x] == 'f':
                grid.append(box.create_rectangle(x * each, y * each, x * each + each, y * each + each, fill='#3cb612',
                                                 outline='grey'))
                end = y, x
            elif field[y][x] == 's':
                grid.append(box.create_rectangle(x * each, y * each, x * each + each, y * each + each, fill='#167be0',
                                                 outline='grey'))
                start = y, x
    for item in grid:
        box.move(item, 10, 10)


def reading():
    f = open('input.txt')
    f.readline()
    while True:
        a = f.readline()
        if a == '':
            break
        a = list(a)
        if a[len(a) - 1] == '\n':
            a.pop()
        while len(a) < res[0]:
            a.append('0')
        field.append(a)
    while len(field) - 1 < res[1]:
        field.append(list('0' * res[0]))
    f.close()
    return field

# just empty list
def empty():
    for i in range(len(field)):
        m.append([])
        for j in range(len(field[i])):
            m[-1].append(0)
    i, j = start
    m[i][j] = 1


hm = 0
grid = []
field = []
m = []
each = 25
res = 30, 32
win = Tk()
win.resizable(False, False)
win.geometry('+0+0')
box = Canvas(win, width=each * res[0] + 16, height=each * res[1] + 16, bg='white')
fr3 = Frame(win)
fr1 = Frame(fr3)
fr2 = Frame(fr3)
but1 = Button(fr1, text='Next step', command=one)
but2 = Button(fr1, text='Automatically', command=auto)
scale = Scale(fr2, orient='horizontal', from_=400, to_=50)
scale.set(200)
box.pack()
fr1.pack(side=LEFT, padx=30)
fr2.pack(side=LEFT, padx=30)
fr3.pack()
but1.pack(side=LEFT, padx=10, pady=10)
but2.pack(side=LEFT, padx=10, pady=10)
Label(fr2, text='Speed').pack(anchor=E, side=LEFT, padx=20, pady=20)
scale.pack(side=LEFT, padx=10, pady=10, anchor=W)
reading()
drawing()
empty()
mainloop()
