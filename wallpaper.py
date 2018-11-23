#!/usr/bin/env python3

"""
___________BY MOHAMMD ISLAM
"""

from __future__ import print_function
import os
import sys
import math
import time
from PIL import Image, ImageDraw
import random
from random import randint
from termcolor import cprint


DEFAULT_WALL_WIDTH = 1280
DEFAULT_WALL_HEIGHT = 800


class DrawingInImage:
    """
    This class used to draw images utalizing lines, points and polygaons
    """

    def __init__(self):
        self.arg_names = [
            'Command',
            'scree_width',
            'screen_height',
            'repetition'
        ]
        self.args = dict(zip(self.arg_names, sys.argv))
        self.width = int(sys.argv[1]) if 'scree_width' and 'screen_height' \
            in self.args.keys() else DEFAULT_WALL_WIDTH
        self.height = int(sys.argv[2]) if 'scree_width' and 'screen_height' \
            in self.args.keys() else DEFAULT_WALL_HEIGHT
        self.repetition = int(
            sys.argv[3]) if 'repetition' in self.args.keys() else 10
        self.box_width = 5
        self.box_height = 5
        self.im = Image.new('RGB',
                            (self.width, self.height),
                            color=(0, 0, 0))
        self.draw = ImageDraw.Draw(self.im)

    def drawLine(self):
        """
        Draws a line with random x and y coordinate
        """
        self.x_val = random.triangular(-5, self.width)
        self.y_val = random.triangular(-5, self.height)
        self.x2_val = self.x_val + random.randrange(self.box_width)
        self.y2_val = self.y_val + random.randrange(self.box_height)
        self.draw.line([self.x_val, self.y_val, self.x2_val, self.y2_val],
                       fill=(
            random.randrange(255),
            random.randrange(255),
            random.randrange(255)),
            width=1
        )

    def drawPoint(self):
        self.x_val = random.triangular(-5, self.width)
        self.y_val = random.triangular(-5, self.height)
        self.x2_val = self.x_val + random.randrange(self.box_width)
        self.y2_val = self.y_val + random.randrange(self.box_height)
        self.draw.point([self.x_val, self.y_val, self.x2_val, self.y2_val],
                        fill=(
            random.randrange(255),
            random.randrange(255),
            random.randrange(255)),
        )

    def drawPolygon(self):
        self.x_val = random.triangular(-5, self.width)
        self.y_val = random.triangular(-5, self.height)
        self.x2_val = self.x_val + random.randrange(self.box_width)
        self.y2_val = self.y_val + random.randrange(self.box_height)
        self.draw.polygon(
            [
                random.choice([self.x_val*2, -self.x_val]),
                random.choice([self.y_val*2, -self.y_val]),
                random.choice([self.x2_val//2, -self.x2_val]),
                random.choice([self.y2_val//2, -self.y2_val]),
                random.choice([-self.y_val*2, self.y_val*2]),
                random.choice([-self.x_val*2, self.x_val*2]),
                random.choice([-self.y_val//2, self.y_val*2]),
                random.choice([-self.x_val//2, self.x_val//2])
            ],
            fill=(
                round(random.randrange(0, 200)),
                round(random.randrange(0, 255)),
                round(random.randrange(0, 255))
            ))

    def return_im(self):
        return self.im


class Cools():
    """
    Filter_imag("626201613142.png")
    """

    def __init__(self, filename):
        self.image = filename
        self.pix = self.image.load()
        self.size = self.image.size

        self.line_len_factor: int = round(self.size[0]*.03)
        self.line_wid: int = 1

        self.blank_image = self.image
        # self.blank_image = Image.new('RGB', (self.size[0], self.size[1]))

        self.draw = ImageDraw.Draw(self.blank_image)

        print("line_len_factor : ", self.line_len_factor)
        print("line_wid : ", self.line_wid)
        print("size : ", self.size)

        list_start_time: float = time.time()

        list(
            map(
                lambda width:
                list(
                    map(lambda height:

                        self.draw.line(
                            [width,
                             height,
                             round(
                                 width + round(sum(self.pix[width, height])/self.line_len_factor) * math.cos(randint(0, 360))),
                             round(
                                 height + round(sum(self.pix[width, height])/self.line_len_factor) * math.sin(randint(0, 360)))],

                            fill=self.pix[width, height],
                            width=self.line_wid
                        ),
                        range(self.size[1])
                        )
                ),
                range(self.size[0])
            )
        )

        print("List Comprehension finished in", str(
            (time.time()-list_start_time)/60)[:4], " minutes")

    def save(self, filename):
        self.blank_image.save(filename)


current_wd = os.path.dirname(os.path.realpath(sys.argv[0]))
walls_directory = os.path.join(current_wd, "walls")


if __name__ == '__main__':
    wall_num = 0
    for i in range(10):
        # list(map(lambda x: putToScreen.drawLine(), range(500)))
        putToScreen = DrawingInImage()

        list(map(lambda x: putToScreen.drawPolygon(), range(putToScreen.repetition)))

        wall_num += 1
        ckll = Cools(putToScreen.return_im())

        if not os.path.exists(walls_directory):
            os.makedirs(walls_directory)
        filename = os.path.join(walls_directory, f'wall{wall_num}.png')
        cprint(str(f"{wall_num:05}") + "-"*(10-len(str(wall_num))) +
               f'wall{wall_num}.png', color="blue")
        
        ckll.save(filename)

    cprint(putToScreen.args, color='grey', attrs=["bold", "dark"])
    cprint(
        f"Successfully created {wall_num} random wallpapers", on_color='on_green')
