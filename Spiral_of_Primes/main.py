#https://www.youtube.com/watch?v=a35KWEjRvc0&t=370s
import tkinter

tink = tkinter.Tk()


width = 1000
height = 1000
spiral_size = 201 #should be odd


def create_canvas():
    # width, height int
    global my_canvas
    my_canvas = tkinter.Canvas(tink, width=str(width), height =str(height), bg ="black")

def w_txt(x1,y1,text):
    my_canvas.create_text(x1,y1, font=("Purisa", int(stepSize/10)), fill="red", text=str(text))
def w_box(x1,y1,colr):
    s = stepSize/4
    my_canvas.create_rectangle(x1-s,y1-s,x1+s,y1+s,fill=colr, outline="black")

def w_line(x1,y1,x2,y2):
    my_canvas.create_line(x1,y1,x2,y2,fill="white",width=str(50/spiral_size))

def is_prime(value):
    if (value==1):
        return False

    for i in range(2,int(value/2)+1):
        if (value%i == 0):
            return False
    return True
     

def drawing():
    global x 
    global y
    global old_x
    global old_y 
    global state
    global numStep
    global step
    global turnCounter
 
    #w_txt(x,y,step)
    if (is_prime(step)):
        bx_clr = "white"
        w_box(x,y,bx_clr)
    else:
        bx_clr = "grey"

     #w_line(old_x, old_y, x, y)
    #w_box(x,y,bx_clr)
    

    old_x = x 
    old_y = y

    if (state == 0):
        x+=stepSize
    elif (state == 1):
        y-=stepSize
    elif (state == 2):
        x-=stepSize
    elif (state == 3):
        y+=stepSize

    if (step % numStep == 0):
        state = (state +1)%4
        turnCounter +=1
        if (turnCounter % 2 ==0):
            numStep+=1
    step+=1

x = width/2
y = height/2
stepSize = width/spiral_size
step = 1 
numStep = 1
state = 0
turnCounter = 0

old_x = x
old_y = y


create_canvas()
for i in range(0, spiral_size*spiral_size):
    drawing()



my_canvas.pack()
tink.mainloop()


# my_canvas = tkinter.Canvas(tink, width="500", height ="500", bg = "blue")

# Create Line
#my_canvas.create_line(x1,y1,x2,y2,fill="color")
#Create Square
#w.create_rectangle(x1,y1,x2,y2, fill="color", outline = 'color')
#Create Text
#my_canvas.create_text(250,250,text="issa me mario", fill="red")


# my_canvas.create_line(0,0,100,200,fill="white")
# my_canvas.create_rectangle(250-20,250-20,250+20,250+20,fill="white", outline="white")
# my_canvas.create_text(250,250,text="issa me mario", fill="red")

