from sense_hat import SenseHat

sense = SenseHat()

r = 50
g = 0
b = 50
text_col = (255,0,0)
back_col = (0,0,50)

sense.show_message("HI STEAMETTES!!!",text_colour=text_col, back_colour=back_col)

sense.clear((r, g, b))
