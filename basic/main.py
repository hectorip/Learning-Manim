from manimlib import *

CONFIG = {
    "camera_config":{"background_color": "#003399"}
}
class SquareToCircle(Scene):
    def construct(self):
        # Setting background color
        self.camera.background_color = WHITE
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(RED, opacity=0.5)
        circle.set_stroke(BLUE_E, width=10)
        self.play(FadeIn(square))
        self.play(Transform(square, circle))
        # self.play(FadeOut(square))
