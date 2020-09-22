#Tkinter Init
from tkinter import *
import os
import sys
root = Tk(className="System variable checker")
root.configure(bg="black")
root.geometry("700x100")
#Making the text and background

text = Text(root)
text.insert(INSERT, "JavaHome:  ")
text.insert(END, os.environ['JAVA_HOME'])
text.pack()
text.insert(INSERT, "                                   MavenHome:  ")
text.insert(END, os.environ['MAVEN_HOME'])
text.pack()
text.insert(INSERT, "                                                                                           Made by c0d3rb0y                                                                                                                                                                                                                                                                                                ")
text.pack()
#Text Formatting
text.tag_add("here", "1.0", "30.0")
text.tag_config("here", background="black", foreground="white")

#Main Window Control
root.mainloop()
