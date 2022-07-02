from tkinter import Tk, NORMAL, HIDDEN, Canvas

def toggle_eyes():
    current_color = c.itemcget(left_eye,'fill')
    new_color = 'pink' if current_color == 'white' else 'white'
    current_state = c.itemcget(left_pupil,'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(left_pupil, state = new_state)
    c.itemconfigure(right_pupil , state = new_state)
    c.itemconfigure(left_eye , fill = new_color)
    c.itemconfigure(right_eye , fill = new_color)

def blink():
    toggle_eyes()
    win.after(200,toggle_eyes)
    win.after(2000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(left_pupil , 10,-5)
        c.move(right_pupil, -10,-5)
        c.crossed_eyes = True
    else:
        c.move(left_pupil , -10,5)
        c.move(right_pupil, 10,5)
        c.crossed_eyes = False

def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip , state = NORMAL)
        c.itemconfigure(tongue_main , state = NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip , state = HIDDEN)
        c.itemconfigure(tongue_main , state = HIDDEN)
        c.tongue_out = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    win.after(1000,toggle_tongue)
    win.after(1000,toggle_pupils)
    return

def show_happy(event):
    if(10<= event.x and event.x <= 500) and (10<= event.y and event.y <= 500):
        c.itemconfigure(left_cheek , state = NORMAL)
        c.itemconfigure(right_cheek , state = NORMAL)
        c.itemconfigure(mouth_happy , state = NORMAL)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad, state = HIDDEN)
        c.happy_level = 10
        return

def hide_happy(event):
    c.itemconfigure(left_cheek , state = HIDDEN)
    c.itemconfigure(right_cheek , state = HIDDEN)
    c.itemconfigure(mouth_happy , state = HIDDEN)
    c.itemconfigure(mouth_normal , state = NORMAL)
    c.itemconfigure(mouth_sad, state = HIDDEN)
    return

def sad():
    if c.happy_level == 0 :
        c.itemconfigure(mouth_happy , state = HIDDEN)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad , state = NORMAL)
    else:
        c.happy_level -= 1
    win.after(500,sad)
    
win = Tk()
c = Canvas(win,width=500,height=500)
c.configure(bg='blue')
body = c.create_oval(100,100,400,400,outline='pink',fill='pink')
left_foot = c.create_oval(100,350,200,400,outline='pink',fill='pink')
right_foot = c.create_oval(300,350,400,400,outline='pink',fill='pink')
left_ear = c.create_polygon(100,150,200,150,150,50,outline='pink',fill='pink')
right_ear = c.create_polygon(300,150,400,150,350,50,outline='pink',fill='pink')
left_eye = c.create_oval(180,160,240,240,outline='black',fill='white')
right_eye = c.create_oval(260,160,320,240,outline='black',fill='white')
left_pupil = c.create_oval(210,200,220,210,outline='black',fill='black')
right_pupil = c.create_oval(280,200,290,210,outline='black',fill='black')
mouth_normal = c.create_line(200,320,250,350,300,320,smooth=1 , width=2 , state=NORMAL)
mouth_happy = c.create_line(200,320,250,380,300,320,smooth=1 , width=2 , state=HIDDEN)
mouth_sad = c.create_line(200,320,250,300,300,320,smooth=1 , width=2 , state=HIDDEN)
left_cheek = c.create_oval(130,260,200,290,outline='red',fill='red', state = HIDDEN)
right_cheek = c.create_oval(300,260,370,290,outline='red',fill='red', state = HIDDEN)
tongue_main = c.create_rectangle(210,290,290,330,outline='red' , fill='red',state=HIDDEN)
tongue_tip = c.create_oval(210,310,290,350,outline='red' , fill='red',state=HIDDEN)
c.pack()
c.bind('<Motion>' , show_happy)
c.bind('<Leave>' , hide_happy)
c.bind('<Double-1>' , cheeky)
c.crossed_eyes = False
c.tongue_out = False
c.happy_level = 10
win.after(1000,blink)
win.after(5000,sad)
win.mainloop()