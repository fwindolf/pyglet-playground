from enum import Enum

class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED =   (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE =  (0, 0, 255)

    def rgb(self):
        return self.value

    def random():
        return (random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255))
