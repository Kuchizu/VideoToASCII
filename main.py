import curses
from time import sleep

from PIL import Image

TIMEOUT = 0.01  # Скорость рендера, зависит от мощностей


def draw_frames(stdscr):
    stdscr.clear()
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    for i in range(6571):
        img = Image.open(f'Frames/{i}.jpg')
        width, height = img.size
        step = int(height / 65)

        q, w = 0, 40
        for y in range(0, height, step):
            for x in range(0, width, step):
                r, g, b = img.getpixel((x, y))

                brightness = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
                ascii_index = int(brightness / 25)
                ascii_index = min(ascii_index, len(ascii_chars) - 1)

                stdscr.addstr(q, w, ascii_chars[ascii_index])
                w += 2

            q += 1
            w = 40

        stdscr.refresh()
        sleep(TIMEOUT)


curses.wrapper(draw_frames)
