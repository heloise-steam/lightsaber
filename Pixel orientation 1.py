from sense_hat import SenseHat
sense = SenseHat()

sense.clear((0, 0, 0))

sense.set_rotation(0)

#eyes
sense.set_pixel(2, 2, (255, 0, 0))
sense.set_pixel(4, 2, (255, 0, 0))
#nose
sense.set_pixel(3, 4, (0, 0, 255))
#mouth
mouth_col = (133, 25, 200)
sense.set_pixel(1, 5, mouth_col)
sense.set_pixel(2, 6, mouth_col)
sense.set_pixel(3, 6, mouth_col)
sense.set_pixel(4, 6, mouth_col)
sense.set_pixel(5, 5, mouth_col)

#sense.flip_v()
