from tkinter import *
import os
import sys
import subprocess
import threading

encoding = 'latin1'
shell = subprocess.Popen('/bin/bash', \
    env={"PATH": "/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin"}, \
                         stdin=subprocess.PIPE,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

current_output = ''
  
root = Tk()
root.title('impetus')
root.minsize(400,500)
root.wm_attributes("-transparent", True)
    
output_display = Text(root);
output_display.pack(side="top", fill=BOTH, expand=True)
output_display.configure(state=DISABLED, insertbackground='#00b000', \
                         highlightcolor='#00b000', fg='#00b000')
bottom_frame = Frame(root, width=400, height=40)
bottom_frame.pack(fill=X, side="bottom", expand=False)
command_entry = Text(bottom_frame, width=60, height=7);
command_entry.pack(fill=X, side="top", expand=False)
command_entry.configure(insertbackground='#00b000', \
                        highlightcolor='#00b000', fg='#00b000')
password_frame = Frame(bottom_frame, width=400, height=40)
password_frame.pack(fill=X, expand=True)
passwor_label = Label(password_frame, text='Hidden:', fg='#00b000')
passwor_label.pack(side='left')
password_entry = Entry(password_frame, show="*", width=60)
password_entry.pack(side='right', fill=X, expand=True)
password_entry.configure(insertbackground='#00bf00', \
                        highlightcolor='#00b000', fg='#00b000')
password_button = Button(password_frame, text='Enter')

def handle_command(event):
    output_display.configure(state=NORMAL)
    command = command_entry.get('1.0',END)
    output_display.insert(END, command)
    command_entry.delete('0.0', END)
    shell.stdin.write(bytes(command + "\n", 'utf-8'))
    shell.stdin.flush()
    shell.stdin.write(bytes('pwd\n', 'utf-8'))
    shell.stdin.flush()
    output_display.configure(state=DISABLED)
    return "break"

def get_output():
    global current_output
    output_display.configure(state=NORMAL)
    for line in iter(shell.stdout.readline, ''):
        str_line = str(line.decode('UTF-8')).rstrip()
        if str_line == '':
            break
        else:
            current_output = str_line + '\n'
            root.event_generate("<<event1>>")
        sys.stdout.flush
    output_display.configure(state=DISABLED)

def write_output(event):
    global current_output
    output_display.configure(state=NORMAL)
    output_display.insert(END, current_output)
    output_display.configure(state=DISABLED)
    

command_entry.bind("<Return>",handle_command)
command_entry.focus_set()

output_thread = threading.Thread(target=get_output)
output_thread.daemon = True
output_thread.start()
root.bind("<<event1>>", write_output)

shell.stdin.write(bytes('pwd\n', 'utf-8'))
shell.stdin.flush()

root.mainloop()

