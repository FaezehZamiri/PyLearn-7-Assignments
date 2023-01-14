import arcade
import numpy as np

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

arcade.open_window(400, 400, "Complex Loops -Box")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if (np.mod(column,2)==0 and np.mod(row,2)==0) or (np.mod(column,2)!=0 and np.mod(row,2)!=0):
            arcade.draw_rectangle_filled(x, y, 12,12, arcade.color.ALIZARIN_CRIMSON,45)

        elif (np.mod(row,2)==0 and np.mod(column,2)!=0) or (np.mod(row,2)!=0 and np.mod(column,2)==0):
            arcade.draw_rectangle_filled(x, y, 12,12, arcade.color.BABY_BLUE,45)

arcade.finish_render()
arcade.run()