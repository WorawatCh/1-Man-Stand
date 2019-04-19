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
                                      600,
                                      arcade.color.SKY_BLUE)

    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      600,
                                      0,
                                      arcade.color.DARK_SPRING_GREEN)


def draw_line():
    arcade.draw_line(150, 0,
                     150, 600,
                     arcade.color.BLACK, 4)
    arcade.draw_line(0, 500,
                     SCREEN_WIDTH, 500,
                     arcade.color.BLACK, 4)
    arcade.draw_line(0, 400,
                     SCREEN_WIDTH, 400,
                     arcade.color.BLACK, 4)
    arcade.draw_line(0, 300,
                     SCREEN_WIDTH, 300,
                     arcade.color.BLACK, 4)
    arcade.draw_line(0, 200,
                     SCREEN_WIDTH, 200,
                     arcade.color.BLACK, 4)
    arcade.draw_line(0, 100,
                     SCREEN_WIDTH, 100,
                     arcade.color.BLACK, 4)


def draw_player():
    player = arcade.Sprite('images/soilder.png')
    player.set_position(80, 300)
    player.draw()


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
    draw_player()

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


if __name__ == "__main__":
    main()
