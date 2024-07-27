from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(RED, opacity=0.5)
        self.play(FadeIn(square))
        self.play(Transform(square, circle))
        # self.play(FadeOut(square))
