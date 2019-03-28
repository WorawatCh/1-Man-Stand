# Library imports
import arcade

# Constants - variables that do not change
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Drawing With Functions Example"


def draw_background():
   
    # Draw the sky in the top two-thirds
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      590,
                                      arcade.color.SKY_BLUE)

    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      590,
                                      0,
                                      arcade.color.DARK_SPRING_GREEN)

def draw_line():
    arcade.draw_line(0,550,SCREEN_WIDTH,550,arcade.color.BLACK,4)

def main():
    """
    This is the main program.
    """

    # Open the window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()

    # Call our drawing functions.
    draw_background()
    draw_line()

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


if __name__ == "__main__":
    main()
