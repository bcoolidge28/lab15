#########################################
#
#    100pt - Putting it together!
#
#########################################


# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='grey')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="green")
player = drawpad.create_rectangle(240,240,260,260, fill="purple")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "#F25252")
		self.up.grid(row=0,column=0)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate2()

                self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "#4D4FF0")
		self.left.grid(row=0,column=1)
		self.left.bind("<Button-1>", self.moveLeft)
	
	        self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "#CBFFB3")
		self.right.grid(row=0,column=2)
		self.right.bind("<Button-1>", self.moveRight)
	
	        self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "#1CB0EB")
		self.down.grid(row=0,column=3)
		self.down.bind("<Button-1>", self.moveDown)
	
	def moveUp(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                if y1 > 10:
                    drawpad.move(player,0,-10)
                
                
        def moveLeft(self, event):
            global player
            global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            if x1 > 10:
                drawpad.move(player,-10,0)
        
        def moveRight(self, event):
            global player
            global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            if x2 < 480:            
                drawpad.move(player,10,0)
        
        def moveDown(self, event):
            global player
            global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            if y2 < 320:
                drawpad.move(player,0,10)



    
        # Animate function that will bounce target left and right, and trigger the collision detection  
        def animate(self):
	    global target
	    global direction
	    
	    # Insert the code here to make the target move, bouncing on the edges    
	direction = 4    
        def animate2(self):
            global direction
            global target
            x1, y1, x2, y2 = drawpad.coords(target)
            px1, py1, px2, py2 = drawpad.coords(player)
            if x2 > drawpad.winfo_width():
                direction = - 4
            elif x1 < 0:
                direction = 5
                         
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            if didWeHit == False:
                drawpad.move(target,direction,0)
            drawpad.after(1,self.animate2) 
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1, y1, x2, y2 = drawpad.coords(target)
                px1, py1, px2, py2 = drawpad.coords(player)
                if (px1 > x1 and px2 < x2) and (py1 > y1 and py2 < y2):
                    return True
                else:
                    return False
                
                
        

          
          
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)

                # Do your if statement - remember to return True if successful!                
		


myapp = MyApp(root)

root.mainloop()