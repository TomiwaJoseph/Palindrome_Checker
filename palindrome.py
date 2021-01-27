from tkinter import *

root = Tk()
root.geometry('400x200')
root.config(bg='#000')

def checker():
    word = entry.get()
    if word == word[::-1]:
        output.config(f'{word} is a palindrome')

Label(text='This program checks if input is a Palindrome', font='candara 14',
    fg='#fff').pack(pady=(10,5))
entry = Entry(justify='center',font='poppins 12',width=22)
entry.pack(pady=(0,5))
Button(text='Check',font='candara 14').pack(pady=(0,5))
output = Label(text='Input is a palindrome',font='poppins 16',fg='green')
output.pack(pady=(0,5))

mainloop()