import pytest
from engine2d import Engine2D
from typing import List
from circle import Circle
from triangle import Triangle
from quad import Quad

engine = Engine2D();
triangles = [
(1, 1, 2, 2, 3, 3),
(8, 6, 4, 74, 4, 5)
]
quads = [
(1, 1, 2, 2),
(8, 6, 4, 74)
]
circles = [
(1, 1, 2),
(8, 6, 4)
]
count = 0

@pytest.mark.parametrize(
    "color", [5, 6]
)
def test_change_color(
    color
):
    engine.change_color(color)
    assert engine.get_color() == color
    
@pytest.mark.parametrize(
    "x, y, x1, y1, x2, y2", triangles
)
def test_add_triangle(
    x, y, x1, y1, x2, y2
):
    global count
    engine.add_triangle(x, y, x1, y1, x2, y2)
    count += 1
    assert len(engine.get_canvas()) == count

@pytest.mark.parametrize(
    "x, y, s1, s2", quads
)    
def test_add_quad(
    x, y, s1, s2
):
    global count
    engine.add_quad(x, y, s1, s2)
    count += 1
    assert len(engine.get_canvas()) == count

@pytest.mark.parametrize(
    "radius, x, y", circles
)    
def test_add_circle(
    radius, x, y
):
    global count
    engine.add_circle(radius, x, y)
    count += 1
    assert len(engine.get_canvas()) == count
    
def test_draw():
    global count
    engine.draw()
    count = 0
    assert len(engine.get_canvas()) == count
 