import tkinter


def convert_mile_to_km():
    mile = float(mile_input.get())
    km = mile * 1.609
    km_output.config(text=f'{km}')


root = tkinter.Tk()
root.title('Mile to Km Converter')

mile_input = tkinter.Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = tkinter.Label(text='Miles')
mile_label.grid(column=2, row=0)

is_equal_to = tkinter.Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

km_output = tkinter.Label(border=0, width=4)
km_output.grid(column=1, row=1)

km_label = tkinter.Label(text='Km')
km_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text='Calculate', command=convert_mile_to_km)
calculate_button.grid(column=1, row=2)

root.mainloop()
