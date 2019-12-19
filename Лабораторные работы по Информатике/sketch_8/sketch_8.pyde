def setup():
    size(700, 700);
    noLoop();

def draw(): 
    background(120, 170, 200);
    smooth();
    strokeWeight(50);
    stroke(200);

    translate(width/2, height/2 - 100);
    line(-100,0,100,0);

    translate(0, 100);
    scale(1.5, 1.5);
    line(-100,0,100,0);

    translate(0, -150);
    scale(1, 1);
    line(-100,0,100,0);
