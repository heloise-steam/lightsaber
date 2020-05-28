from sense_hat import SenseHat

sense = SenseHat()

r = 255
g = 0
b = 255
text_col = (255,0,0)
back_col = (0,255,0)

sense.show_message("Hello!",text_colour=text_col, back_colour=back_col)

sense.clear((r, g, b))
