def setup():
    background(255) 
    size(500, 500) 
    smooth()  
l1x1 = 0 
l1y1 = 0 
l1x2 = 500 
l1y2 = 500 
flug = 2
i=0
g=0
def draw():
    global l1x1, l1y1,l1x2,l1y2, flug, i, k, g 
    colorMode(HSB, width, height, 100)
    background(15) 
    strokeWeight(50) 
    line(l1x1, l1y1, l1x2, l1y2) 
    for i in range (0, 20, 2):
        k = i * 25 
        stroke(HSB, l1x2, l1y1, 20+i*10); 
        line(l1x1 + k, l1y1, l1x2, l1y2 - k) 
        line(l1x1, l1y1 + k, l1x2 - k, l1y2)
         
    l1x1 = l1x1 + flug 
    l1y1 = l1y1 + flug 
    l1x2 = l1x2 - flug
    l1y2 = l1y2 - flug 
    
    if l1y2 in range (0, 500):
        flug = flug
    else:
        flug = flug*(-1) 
        
  
