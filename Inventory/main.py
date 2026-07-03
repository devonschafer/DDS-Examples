from tkinter import *
from dds import DDS

ddsfile = 'bench_stock.dds'
ddsui = 'ui.dds'

size = '%sx%s' % (DDS.returnSpecificValue(ddsui, (2,1), 'value'), DDS.returnSpecificValue(ddsui, (2,2), 'value'))
root = Tk()
root.geometry(size)
root.title(DDS.returnSpecificValue(ddsui, (1,1), 'value'))

frame_top = Frame(root)
frame_top.pack(side=TOP)
frame_bottom = Frame(root)
frame_bottom.pack(side=BOTTOM, expand=True, fill=BOTH, anchor='s')

column1 = Entry(frame_top)
column1.insert(0, DDS.returnSpecificValue(ddsui, (3,1), 'value'))
column1.pack(side=LEFT)

column2 = Entry(frame_top)
column2.insert(0, DDS.returnSpecificValue(ddsui, (3,2), 'value'))
column2.pack(side=LEFT)

column3 = Entry(frame_top)
column3.insert(0, DDS.returnSpecificValue(ddsui, (3,3), 'value'))
column3.pack(side=LEFT)

column4 = Entry(frame_top)
column4.insert(0, DDS.returnSpecificValue(ddsui, (3,4), 'value'))
column4.pack(side=LEFT)

column5 = Entry(frame_top)
column5.insert(0, DDS.returnSpecificValue(ddsui, (3,5), 'value'))
column5.pack(side=LEFT)

column6 = Entry(frame_top)
column6.insert(0, DDS.returnSpecificValue(ddsui, (3,6), 'value'))
column6.pack(side=LEFT)

column7 = Entry(frame_top)
column7.insert(0, DDS.returnSpecificValue(ddsui, (3,7), 'value'))
column7.pack(side=LEFT)

column8 = Entry(frame_top)
column8.insert(0, DDS.returnSpecificValue(ddsui, (3,8), 'value'))
column8.pack(side=LEFT)

column9 = Entry(frame_top)
column9.insert(0, DDS.returnSpecificValue(ddsui, (3,9), 'value'))
column9.pack(side=LEFT)

column10 = Entry(frame_top)
column10.insert(0, DDS.returnSpecificValue(ddsui, (3,10), 'value'))
column10.pack(side=LEFT)

def update_output():
    output.delete("1.0", END)
    output.insert(END, DDS.readFile(ddsfile, 'all', None))

def button_command():
    DDS.appendFile(ddsfile, '%s::%s,,%s,,%s,,%s,,%s,,%s,,%s,,%s,,%s' % (column1.get(), column2.get(), column3.get(), column4.get(), column5.get(), column6.get(), column7.get(), column8.get(), column9.get(), column10.get()), 'save')
    update_output()

    
button = Button(frame_bottom, text='Enter', command=button_command)
button.pack(side=TOP, fill=X)

output = Text(frame_bottom, wrap=WORD, relief=FLAT, width=65)
output.pack(side=BOTTOM, expand=True, fill=BOTH)
sb = Scrollbar(output, orient=VERTICAL, command=output.yview)
sb.pack(side=RIGHT, fill=Y)
output.config(yscrollcommand=sb.set)

root.mainloop()
