#coding:utf-8
from tkinter import *
from tkinterdnd2 import *
import os

def dndstrtoary(drop_str):
    i = 0
    files = []
    while i < len(drop_str):
        if drop_str[i] == '{':
            fd = drop_str.find('}', i)
            filname = drop_str[i+1:fd]
            i = fd + 1
                
            files.append(filname)
            if len(drop_str) <= i:
                break

            if drop_str[i] == ' ':
                i += 1
        else:
            fd = drop_str.find(' ', i)
            if fd < 0:
                filname = drop_str[i:]
                i = len(drop_str)
            else:
                filname = drop_str[i:fd]
                i = fd + 1
            files.append(filname)
    return files


def add_listbox(event):
    #listbox.insert("end", event.data)
    files = dndstrtoary(event.data)
    for i in files:
        listbox.insert("end", i)
        newname = ''
        for j in range(len(i)):
            if i[len(i)-j-1] == '/':
                newname += i[:len(i)-j-1] + "/"
                #print(newname)
                tmp = str(i[len(i)-j:])
                tmp = tmp.split('_')
                #print(tmp)
                newname += tmp[1]+" 第"+tmp[2].zfill(2)+"話 "+tmp[3]
                #print(newname)
                newname += '.'+tmp[5].split('.')[1]
                #print(newname)
                break
        os.rename(i, newname)
    listbox.insert("end", "処理が終わりました")
    #s = event.data

root = TkinterDnD.Tk()
root.geometry("400x300")
root.title("AnimeLockerRenamer")
root.config(bg = "#cccccc")

frame = Frame(root)

listbox = Listbox(frame, width = 50, height = 15, selectmode = SINGLE)
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', add_listbox)

scroll = Scrollbar(frame, orient = VERTICAL)
listbox.configure(yscrollcommand = scroll.set)
scroll.config(command = listbox.yview)

frame.pack()
listbox.pack(fill = X, side = LEFT)
scroll.pack(side = RIGHT, fill = Y)

root.mainloop()
