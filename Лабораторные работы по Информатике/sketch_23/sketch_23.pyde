def setup():
    size(700, 700)
    smooth()
    background(255)
    noStroke()
    ellipseMode(CENTER)
    noLoop()
    
def draw():  
    border = 10 
    nw = width-2*border 
    nh = height-2*border 
    nWstep = nw / 5  
    nHstep = nh / 5
    for i in range (0, 5, 1): 
        for j in range (0, 5, 1): 
            x = border + j*nWstep + nWstep/2 
            y = border + i*nHstep + nHstep/2 
            size = 144 - (j+i)*17 
            mColor = size*1.5 
            fill(mColor, mColor, 150) 
            ellipse(x, y, size, size) 
            fill(250)
            ellipse(x, y, 4, 4) 
