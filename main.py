import curses
import sys
from time import sleep
from _curses import error as cerr

import cv2
from PIL import Image

TIMEOUT = 0.0001  # Скорость рендера, зависит от мощностей


def draw_frames(stdscr, path, res=120):
    stdscr.clear()
    framex = 0
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    cap = cv2.VideoCapture(path)
    while cap.isOpened():
        exist, frame = cap.read()

        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        width, height = img.size
        step = int(height / res)

        q, w = 1, 30
        for y in range(0, height, step):
            for x in range(0, width, step):
                r, g, b = img.getpixel((x, y))

                brightness = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
                ascii_index = int(brightness / 25)
                ascii_index = min(ascii_index, len(ascii_chars) - 1)

                try:
                    stdscr.addstr(q, w, ascii_chars[ascii_index])

                except cerr:  # Cuts frame if there's not enough place to put pixels (depends on res arg)
                    break

                w += 2

            q += 1
            w = 30

        framex += 1
        stdscr.refresh()
        stdscr.addstr(1, 3, f'Frame: {framex}')

        sleep(TIMEOUT)


curses.wrapper(draw_frames, sys.argv[1] if len(sys.argv) > 1 else 'VideoExamples/BadApple.mp4')
