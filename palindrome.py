from tkinter import *

root = Tk()
root.geometry('400x200')
root.config(bg='#222')


class Checker():
    def __init__(self):
        Label(text='This program checks if word is a Palindrome', font='candara 14',
            fg='#fff',bg='#222').pack(pady=(15,5))
        self.entry = Entry(justify='center',font='poppins 12',width=22)
        self.entry.pack(pady=(0,5))
        Button(text='Check',bg='teal',fg='#fff',font='candara 14',
            command=self.checker).pack(pady=(10,5))
        self.output = Label(font='poppins 16')


    def checker(self):
        self.output.pack(pady=(0,5))
        word = self.entry.get()
        if word == '':
            self.output.config(text='Please input something',fg='red')
        elif word == word[::-1]:
            self.output.config(text=f'{word} is a palindrome',fg='green')
        else:
            self.output.config(text=f'{word} is not a palindrome',fg='red')


if __name__ == '__main__':
    app = Checker()
    mainloop()