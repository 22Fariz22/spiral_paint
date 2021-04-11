# spiral_paint
I share a script that redraws a photo with a spiral. Optionally, you can select line thickness, color or black and white.
I will briefly tell you what this script does.
The spiral is drawn through Archimedes 'formulas (Archimedes' spiral).
The image is conventionally divided into 6 shades of gray from 255 values.
Create an array where the conditional gray values will be written.
The turtle will take these values to select the thickness of the line (pensize).
Next, we need to correlate the beginning of the turtle's movement with the center of the image.
The turtle, using xcor() and ycor(), will look at the values in the array at every step and, with conditions, create the thickness of the line.
If you have any ideas how you can improve the script or can make an animated clip or something else, I invite you to join this project.
