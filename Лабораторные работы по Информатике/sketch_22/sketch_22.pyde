def setup():
    size(700, 700)
    smooth()
    background(255)
    noStroke()
    noLoop()
    
def draw():
    for h in range(1, 6, 1):    
         for i in range(1, 10, 1):
             fill(i*20)
             rect(i*40+50, 60+80*h, 35, 35)        
         for k in range(1, 10, 1):
             fill(200-k*20)
             rect(k*40+50, 100+80*h, 35, 35)
        
    
