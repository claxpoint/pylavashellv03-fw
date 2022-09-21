import tkinter as tk

root = tk.Tk()

text1.pack(side=tk.LEFT)

text2 = tk.Text(root, height=50, width=200)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',
                    foreground='#0a8ac9',
                    font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,'\nShup Lineview2020: PyLavaShell Freamwork v0.3\n', 'big')
quote = """
shup: shup-tk:
Hello local :)
This is the PyLavaShell Freamwork v0.3 runned on Shup Lineview2020 Engine
local says: type-s
-Whats New!?-
1-fix the bugs
2-free coding
3-simple for conding
local says: type-s
-What is shup?-
Shup is a writing engine and the analysis of human words is called a short code that is considered simple writing. It is also a programming language. Shup has many frameworks that have many functions! The manufacturer of Shup is Claxpoint. In this version that you are using, it is called Shup Lineview 2020 and your framework is called PyLavaShell, which is from the LavaShell family. Shup Lineview is not the only analysis engine family that is only an IDE or Code Editor! Rather, other engines that are programming languages and code analysis engines are included in the Shup engine family.
local says: type-s
-I Need a Help!-
git: https://github.com/claxpoint
email: claxpoint@gmail.com
local says: type-s
-What About Engine Information?-
git: https://github.com/claxpoint/pylavashellv03-fw
engine-used: shup-lineview-2020
freamwork-used: pylavashell-v0.3
by: claxpoint
from: shup-hardwares & shup-softwares & shup-networks (all type-s made by: claxpoint)
engine-v: 2020
fw-v: v0.3(on 2020)
last-upd: 2020 V0.3
cloneby-programinglangs: T@ - ShupXQL - @JQn (all made by type-s none:: claxpoint)
viewer-engine: shup-tk
viewerengine-v: v0.1
;shupend

"""
text2.insert(tk.END, quote, 'color')
text2.insert(tk.END, 'shup: local Shup Lineview2020 status: runned need: close window(local errmsg from shup: SHUP ENGINE HAS BE RUNNED FROM SYS YOU CAN CLOSE THE WINDOW RIGHT NOW)\n', 'follow')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess

window = Tk()
window.title('Shup Lineview2020: PyLavaShell Freamwork v0.3')

gpath = ''

def runMyCode():
    global gpath
    if gpath == '':
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="SLERR-23722: local errmsg: need check save type file")
        msg.pack()
        return
    command = f'python {gpath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputResult, error = process.communicate()
    output.insert('1.0',outputResult)
    output.insert('1.0',error)
     

def openMyFile():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        textEditor.delete('1.0', END)
        textEditor.insert('1.0', code)
        global gpath
        gpath = path

def saveMyFileAs():
    global gpath
    if gpath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = gpath    
    with open(path, 'w') as file:
        code = textEditor.get('1.0', END)
        file.write(code)

textEditor = Text()
textEditor.config(bg='#424140', fg='#db30b1', insertbackground='white')
textEditor.pack()

output = Text(height=7)
output.config(bg='#000000', fg='#1177ad')
output.pack()

 
menuBar = Menu(window)

fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='opn', command = openMyFile)
fileBar.add_command(label='sv', command = saveMyFileAs)
fileBar.add_command(label='svas', command = saveMyFileAs)
fileBar.add_command(label='end', command = exit)
menuBar.add_cascade(label='type', menu = fileBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='analysis-proj', command = runMyCode)
menuBar.add_cascade(label='analysis', menu = runBar)

window.config(menu=menuBar)
window.mainloop()