import joblib
import numpy as np
import tkinter as tk
from playsound import playsound

#load the random forest classification model
filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)


def classification():

    gender = str(entry_gender.get())
    siblings = entry_siblings.get()
    Pclass = entry_class.get()
    chpar = entry_children.get()
    price = entry_ticket.get()
    age = entry_age.get()

    #convert the human readable information to the format that Random forest understands.
    #ONE HOT ENCODING
    #class [1,2,3]  gender [female male]

    if gender == 'male':
        a1 = [0, 1]
    else:
        a1 = [1, 0]
    if Pclass == 1:
        a2 = [1, 0, 0]
    elif Pclass == 2:
        a2 = [0, 1, 0]
    else:
        a2 = [0, 0, 1]

    if not int(loaded_model.predict([np.concatenate((a1,a2,[age],[siblings],[chpar],[price]))])):

        label_result = tk.Label(root, text='You would dieee!!',font=('Helvetica 10 bold'),bg='black', fg='red')
    else:
        label_result = tk.Label(root, text='You would survive, lucky bastard!!', font=('Helvetica 10 bold'), bg='black', fg='gold')

    label_result.place(x=730, y=500, relwidth=0.25, relheight=0.1)


height=1300
width=1300
root=tk.Tk()
canvas=tk.Canvas(root,height=height,width=width)
canvas.pack()



background_image=tk.PhotoImage(file='titanic.gif')
background_image=background_image.subsample(3)
background_label=tk.Label(root,image=background_image, text="WOULD YOU SURVIVE TITANIC?", font=('Helvetica 50 bold'), compound='bottom')

background_label.place(x=0,y=0, relwidth=1,relheight=1)

#audio player
playsound('heart.mp3', 0)

#create the entries for user input
entry_gender = tk.Entry(root)
canvas.create_window(650, 410, window=entry_gender)
label_gender = tk.Label(root, text='Gender')
canvas.create_window(550, 410, window=label_gender)

entry_siblings = tk.Entry(root)
canvas.create_window(650, 440, window=entry_siblings)
label_siblings = tk.Label(root, text='Class')
canvas.create_window(550, 440, window=label_siblings)

entry_class = tk.Entry(root)
canvas.create_window(650, 470, window=entry_class)
label_class = tk.Label(root, text='Siblings')
canvas.create_window(550, 470, window=label_class)

entry_children = tk.Entry(root)
canvas.create_window(650, 500, window=entry_children)
label_children = tk.Label(root, text='Children')
canvas.create_window(550, 500, window=label_children)

entry_ticket = tk.Entry(root)
canvas.create_window(650, 530, window=entry_ticket)
label_ticket = tk.Label(root, text='Ticket Price')
canvas.create_window(550, 530, window=label_ticket)

entry_age = tk.Entry(root)
canvas.create_window(650, 560, window=entry_age)
label_age= tk.Label(root, text='Age')
canvas.create_window(550, 560, window=label_age)


button1 = tk.Button (text='Would you make it?', command = classification)
canvas.create_window(650, 590, window=button1)


root.mainloop()
