from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, LEFT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class MoonScene(Scene):
    def construct(self):
        moon = Circle(radius=1)
        moon.set_fill(WHITE, opacity=1.0)
        moon.set_color(WHITE)

        cut = Circle(radius=0.9,color=BLACK)
        cut.set_fill(BLACK, opacity=1.0)

        
        
        

        self.play(FadeIn(moon))
        self.play(FadeIn(cut))
        
from manim import *

class StarExample(Scene):
    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        star = Star(outer_radius=2, color=RED)
        circle = Circle() 
        star2 = Star(outer_radius=2)
        shapes = VGroup(star)
        shapes.add(star2.round_corners(radius=0.25))

        self.add(pentagram)
        self.play(Create(star), run_time=3)
        self.play(FadeOut(star), run_time=2)
        self.play(Transform(pentagram,circle))
        self.play(Transform(circle,shapes))