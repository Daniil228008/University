def setup():
    size(900, 900);
    noLoop();
def draw():
    background(120, 150, 195);
    smooth();
    strokeWeight(25);

    translate(width/2, height /2);
    stroke(210);
    line(0,0,250,0);

    rotate(7*PI/4);
    stroke(175);
    line(0,0,250,30);

    rotate(7*PI/4);
    stroke(140);
    line(0,0,250,30);

    rotate(7*PI/4);
    stroke(105);
    line(0,0,250,30);

    rotate(7*PI/4);
    stroke(70);
    line(0,0,250,30);

    rotate(7*PI/4);
    stroke(35);
    line(0,0,250,30);

    rotate(7*PI/4);
    stroke(0);
    line(0,0,250,30);
