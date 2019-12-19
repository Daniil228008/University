windowWidth = 900;
windowHeight = 700;
ellipseSize = 200;

def setup():
    size(windowWidth , windowHeight);
    smooth();
    background(55, 190, 91);
    fill(50, 80);
    stroke(150 , 44, 190);
    strokeWeight(5);
    noLoop(); 

def draw():
    ellipse(windowWidth/2, windowHeight/2 - ellipseSize/2, ellipseSize , ellipseSize);
    ellipse(windowWidth/2 - ellipseSize/2, windowHeight/2, ellipseSize , ellipseSize);
    ellipse(windowWidth/2 + ellipseSize/2, windowHeight/2, ellipseSize , ellipseSize);
    ellipse(windowWidth/2, windowHeight/2 + ellipseSize/2, ellipseSize , ellipseSize);
