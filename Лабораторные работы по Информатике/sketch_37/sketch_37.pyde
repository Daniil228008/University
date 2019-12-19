void setup() { 
              2 size(500, 500); 
              3 smooth(); 
              4 background(255); 
              5 noStroke(); 
              6 colorMode(HSB); 
              7 } 
8 
9 boolean flug = true; 
10 
11 void draw() { 
                12 if(flug)
13 for (int i = 0; i < 10; i++) { 
14 for (int j = 0; j < 5; j++) { 
15 fill(10, random(0, 255), random(10, 250)); 
16 rect(j*40+50, i*40+50, 35, 35); 
17 rect((10-j)*40+10, i*40+50, 35, 35); 
18 } 
19 } 
20 } 
21 } 
22 
23 void mouseClicked(){ 
24 flug = !flug; 
25 }  
