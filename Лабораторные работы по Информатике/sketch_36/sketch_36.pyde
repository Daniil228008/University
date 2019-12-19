def setup():
    size(500, 500) 
    smooth()
    background(250) 
    strokeWeight(1)
i = 0
k = 1  
def upDate():
    global i, k, myRandom, myY1, myY2
    i = i + k; 13 
    if(i == 255): k=-1
    if(i == 0): k=1 
def draw (): 
    stroke(i, 20); 
    myRandom = random(-20,20); 
    myY1 = mouseY - myRandom; 
    myY2 = mouseY + myRandom; 
    line(0, myY1, 500, myY2); 
    upDate() 
