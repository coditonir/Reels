# Reels 2
# spirograph
# coditon.ir

from turtle import * 

bgcolor('black')
pensize(2)
speed(0.5)
 

for i in range(12):
   
    for colors in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        color(colors)
         
        circle(100)
         
        left(10)
     
    hideturtle()