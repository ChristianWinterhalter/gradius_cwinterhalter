import spritesheet


class SpriteStripAnim(object):
    """sprite strip animator

    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.
    """

    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1, start_frame=0):
        """construct a SpriteStripAnim

        filename, rect, count, and colorkey are the same arguments used
        by spritesheet.load_strip.

        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.

        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.filename = filename
        ss = spritesheet.Spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = start_frame
        self.frames = frames
        self.f = frames
        self.loop = loop
        self.start_frame = start_frame

    def iter(self):
        """Resets the animation to the starting frame."""
        self.i = self.start_frame
        self.f = self.frames
        return self

    def current(self):
        return self.images[self.i]

    def next(self):
        """Proceed to the next frame to the right on the spritesheet from current."""
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            if self.i == len(self.images):
                if not self.loop:
                    self.i -= 1
                elif self.loop:
                    self.i = self.start_frame
            image = self.images[self.i]
            self.f = self.frames

        return image

    def previous(self):
        """Proceed to the next frame to the left on the spritesheet from current."""
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i -= 1
            if self.i < 0:
                if not self.loop:
                    self.i += 1
                elif self.loop:
                    self.i = self.start_frame
            image = self.images[self.i]
            self.f = self.frames

        return image

    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
