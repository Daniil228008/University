def setup ():
    size (700 , 500)
    smooth ()
    
counter=0

def draw (): 
    noStroke ()
    global counter
    fill (10, 30)
    rect (-1,-1, width - 350, height +1)
    
    ny = sin( counter )*100 + 200
    nx = counter*10
    stroke (25, 250, 200, 150)
    strokeWeight (20)
    line(nx , ny , nx , ny)
    counter = counter + 0.1
    if (nx > width):
        counter = 0;

def keyPressed ():
    if key =="s": 
        saveFrame (" myProcessing .png")
