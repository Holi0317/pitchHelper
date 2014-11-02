#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
except:
    from Tkinter import *
    import ttk
    import tkMessageBox as messagebox

import math

FOutput = []

def addVar():
	pitchHelp = [{'C': 16, 'B': 31, 'C#/Db': 17, 'A': 28, 'F': 22, 'E': 21, 'D#/Eb': 19, 'A#/Bb': 29, 'D': 18, 'G': 24, 'G#/Ab': 25, 'F#/Gb': 23}, {'C': 33, 'B': 62, 'C#/Db': 35, 'A': 55, 'F': 44, 'E': 41, 'D#/Eb': 39, 'A#/Bb': 58, 'D': 37, 'G': 49, 'G#/Ab': 52, 'F#/Gb': 46}, {'C': 65, 'B': 124, 'C#/Db': 69, 'A': 110, 'F': 87, 'E': 82, 'D#/Eb': 78, 'A#/Bb': 117, 'D': 73, 'G': 98, 'G#/Ab': 104, 'F#/Gb': 93}, {'C': 131, 'B': 247, 'C#/Db': 139, 'A': 220, 'F': 175, 'E': 145, 'D#/Eb': 156, 'A#/Bb': 233, 'D': 147, 'G': 196, 'G#/Ab': 208, 'F#/Gb': 185}, {'C': 262, 'B': 494, 'C#/Db': 278, 'A': 440, 'F': 349, 'E': 330, 'D#/Eb': 311, 'A#/Bb': 466, 'D': 294, 'G': 392, 'G#/Ab': 415, 'F#/Gb': 370}, {'C': 523, 'B': 988, 'C#/Db': 554, 'A': 880, 'F': 699, 'E': 659, 'D#/Eb': 622, 'A#/Bb': 932, 'D': 587, 'G': 784, 'G#/Ab': 831, 'F#/Gb': 740}, {'C': 1047, 'B': 1976, 'C#/Db': 1109, 'A': 1760, 'F': 1397, 'E': 1319, 'D#/Eb': 1245, 'A#/Bb': 1865, 'D': 1175, 'G': 1568, 'G#/Ab': 1661, 'F#/Gb': 1475}, {'C': 2093, 'B': 3951, 'C#/Db': 2218, 'A': 3520, 'F': 2794, 'E': 2637, 'D#/Eb': 2489, 'A#/Bb': 3729, 'D': 2349, 'G': 3136, 'G#/Ab': 3322, 'F#/Gb': 2960}, {'C': 4186, 'B': 7902, 'C#/Db': 4435, 'A': 7040, 'F': 5588, 'E': 5274, 'D#/Eb': 4978, 'A#/Bb': 7459, 'D': 4699, 'G': 6272, 'G#/Ab': 6645, 'F#/Gb': 5920}]
	
	global FOutput
	
	try:
		lbpm = int(bpm.get())
		lpit1 = int(pit1.get())
		lpit2 = str(pit2.get())
		ldur = str(dur.get())
	except:
         messagebox.showerror(title='Error', message='One of the input is not in correct form')
         return
	
	try:
		pitch = pitchHelp[lpit1][lpit2]
	except:
		messagebox.showerror(title='Error', message='Pitch is not correct')
		return
	
	duration = bpmHelp(lbpm, ldur)
	
	FOutput.append('sound [{0} {1}] '.format(pitch, duration))
	return

def bpmHelp(bpm, tdur):
	durConvert = {'4': 1, '3': 0.75,'2': 0.5,'1': 0.25, '1/2': 0.125,'1/4': 0.0625}
	modtifier = float(durConvert[tdur])
	
	delayTime = 60 / bpm * 1000
	duration = math.floor(delayTime*modtifier)
	
	return(duration)

def final():
	global FOutput
	output = ''.join(FOutput)
	print (output)
	FOutput=[]
	
	result = Tk()
	result.title('Result')
	temp = StringVar()
	ent = Entry(result, textvariable=temp)
	ent.pack()
	ent.insert(0, output)
	result.clipboard_clear()
	result.clipboard_append(output)
	return

def main():
	root = Tk()
	root.title('Pitch Heler')
	root.geometry('400x350+200+50')

	global bpm
	global timeSig
	global pit1
	global pit2
	global dur
	
	bpm = StringVar()
	timeSig = StringVar()
	pit1 = StringVar()
	pit2 = StringVar()
	dur = StringVar()
	
	bpmLabel = Label(root, text='BPM: ')
	bpmEnt = Entry(root, textvariable = bpm, width=4)
	
	pitchLabel= Label(root, text='Pitch: ')
	
	p1_0=Radiobutton(root, text='0', value=0, variable=pit1)
	p1_1=Radiobutton(root, text='1', value=1, variable=pit1)
	p1_2=Radiobutton(root, text='2', value=2, variable=pit1)
	p1_3=Radiobutton(root, text='3', value=3, variable=pit1)
	p1_4=Radiobutton(root, text='4', value=4, variable=pit1)
	p1_5=Radiobutton(root, text='5', value=5, variable=pit1)
	p1_6=Radiobutton(root, text='6', value=6, variable=pit1)
	p1_7=Radiobutton(root, text='7', value=7, variable=pit1)
	p1_8=Radiobutton(root, text='8', value=8, variable=pit1)
	
	p2_0=Radiobutton(root, text='C', value='C', variable=pit2)
	p2_1=Radiobutton(root, text='C#/Db', value='C#/Db', variable=pit2)
	p2_2=Radiobutton(root, text='D', value='D', variable=pit2)
	p2_3=Radiobutton(root, text='D#/Eb', value='D#/Eb', variable=pit2)
	p2_11=Radiobutton(root, text='E', value='E', variable=pit2)
	p2_4=Radiobutton(root, text='F', value='F', variable=pit2)
	p2_5=Radiobutton(root, text='F#/Gb', value='F#/Gb', variable=pit2)
	p2_6=Radiobutton(root, text='G', value='G', variable=pit2)
	p2_7=Radiobutton(root, text='G#/Ab', value='G#/Ab', variable=pit2)
	p2_8=Radiobutton(root, text='A', value='A', variable=pit2)
	p2_9=Radiobutton(root, text='A#/Bb', value='A#/Bb', variable=pit2)
	p2_10=Radiobutton(root, text='B', value='B', variable=pit2)

	
	durLabel=Label(root, text='Duration: ')
	d1=Radiobutton(root, text='4', value='4', variable=dur)
	d2=Radiobutton(root, text='3', value='3', variable=dur)
	d3=Radiobutton(root, text='2', value='2', variable=dur)
	d4=Radiobutton(root, text='1', value='1', variable=dur)
	d5=Radiobutton(root, text='1/2', value='1/2', variable=dur)
	d6=Radiobutton(root, text='1/4', value='1/4', variable=dur)
	durLabel2=Label(root,text='拍')
	
	restButton = Button(root, text='Rest', command=rest)
	addButton = Button(root, text='Add', command=addVar)
	finalButton = Button(root, text='Final', command=final)
	
	#construction of GUI
	bpmLabel.grid(row=0, column=0, sticky=W)
	bpmEnt.grid(row=0, column=1, sticky=W)
	bpmEnt.insert(0, '120')
	
	pitchLabel.grid(row=1, column=0, sticky=W)
	p1_0.grid(row=1, column=1, sticky=W)
	p1_1.grid(row=2, column=1, sticky=W)
	p1_2.grid(row=3, column=1, sticky=W)
	p1_3.grid(row=4, column=1, sticky=W)
	p1_4.grid(row=5, column=1, sticky=W)
	p1_5.grid(row=6, column=1, sticky=W)
	p1_6.grid(row=7, column=1, sticky=W)
	p1_7.grid(row=8, column=1, sticky=W)
	p1_8.grid(row=9, column=1, sticky=W)
	
	p2_0.grid(row=1, column=2, sticky=W)
	p2_1.grid(row=2, column=2, sticky=W)
	p2_2.grid(row=3, column=2, sticky=W)
	p2_3.grid(row=4, column=2, sticky=W)
	p2_11.grid(row=5, column=2, sticky=W)
	p2_4.grid(row=6, column=2, sticky=W)
	p2_5.grid(row=7, column=2, sticky=W)
	p2_6.grid(row=8, column=2, sticky=W)
	p2_7.grid(row=9, column=2, sticky=W)
	p2_8.grid(row=10, column=2, sticky=W)
	p2_9.grid(row=11, column=2, sticky=W)
	p2_10.grid(row=12, column=2, sticky=W)
	
	durLabel.grid(row=1, column=3, sticky=W)
	
	d1.grid(row=1, column=4, sticky=W)
	d2.grid(row=2, column=4, sticky=W)
	d3.grid(row=3, column=4, sticky=W)
	d4.grid(row=4, column=4, sticky=W)
	d5.grid(row=5, column=4, sticky=W)
	d6.grid(row=6, column=4, sticky=W)
	
	durLabel2.grid(row=1, column=5, sticky=W)
	
	restButton.grid(row=1, column=6, sticky=E)
	addButton.grid(row=2, column=6, sticky=E)
	finalButton.grid(row=3, column=6, sticky=E)
	
	root.mainloop()
	
def rest():
	global FOutput
	durConvert = {'4': 1, '3': 0.75,'2': 0.5,'1': 0.25, '1/2': 0.125,'1/4': 0.0625}
	
	try:
		restdur = dur.get()
	except:
		messagebox.showerror(title='error', message='button is empty')
		return
	
	try:
		lbpm = int(bpm.get())
	except:
		messagebox.showerror(title='error', message='BPM is empty')
		return
	
	delayTime = 60 / lbpm * 1000
	restModtifier = durConvert[restdur]
	duration = math.floor(delayTime*restModtifier)
	
	FOutput.append('wait {0} '.format(duration))
	

if __name__ == '__main__':
	main()
	
