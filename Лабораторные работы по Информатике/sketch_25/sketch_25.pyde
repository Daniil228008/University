def setup ():
    size (600 , 600)
    smooth ()
    strokeWeight (30)
    stroke (100)


def draw ():
    background (0);
    line(frameCount ,100 , 100 + frameCount , 200)
    line (100+ frameCount ,100 , frameCount , 200)
    println ( frameCount )
          
            
