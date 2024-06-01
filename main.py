import pygame
import sys
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "200, 308"


class ShuloGuti:
    def __init__(self):
        self.board = [16, 16]
        self.board = [
            [1 for _ in range(self.board[0])],
            [0 for _ in range(self.board[1])],
        ]

        self.current_turn = 0
        self.screen_w = 343
        self.screen_h = 500
        self.bg_color = (80, 80, 80)
        self.line_color = (200, 200, 200)

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption('ShuloGuti Game')

    def draw_single_line(self, start_pos, end_pos, width=2):
        pygame.draw.line(self.screen, self.line_color, start_pos, end_pos, width)

    def draw_lines(self):
        line_gap = 75
        line_start = 100
        space = 20

        # Diagonal lines
        diagonal_lines = [
            ((space, line_start + line_gap * 2), (self.screen_w - space - line_gap, line_start - line_gap), 3),
            ((space, line_start + line_gap * 2), (space + line_gap * 3, line_start + line_gap * 5), 3),
            ((self.screen_w - space, line_start + line_gap * 2), (space + line_gap, line_start - line_gap), 3),
            ((self.screen_w - space, line_start + line_gap * 2), (space + line_gap, line_start + line_gap * 5), 3),
            ((space, line_start), (space + line_gap * 4, line_start + line_gap * 4), 3),
            ((self.screen_w - space, line_start), (space, line_start + line_gap * 4), 3)
        ]
        for start_pos, end_pos, width in diagonal_lines:
            self.draw_single_line(start_pos, end_pos, width)

        # Horizontal lines
        horizontal_lines = [
            ((space + line_gap, self.screen_h - space - 5), (space + line_gap * 3, self.screen_h - space - 5), 2),
            ((space + line_gap * 1.5 - 5, self.screen_h - space - (line_gap / 2)),
             (space + line_gap * 2.5 + 5, self.screen_h - space - (line_gap / 2)), 2),
            ((space + line_gap, space + 4), (space + line_gap * 3, space + 4), 2),
            ((space + line_gap * 1.5 - 5, space + (line_gap / 2)),
             (space + line_gap * 2.5 + 5, space + (line_gap / 2)), 2)
        ]
        for start_pos, end_pos, width in horizontal_lines:
            self.draw_single_line(start_pos, end_pos, width)

        # Vertical and horizontal grid lines
        for index in range(5):
            self.draw_single_line((space, (line_gap * index + 1) + line_start),
                                  (self.screen_w - space, line_start + (line_gap * index + 1)))
            if index != 2:
                self.draw_single_line((space + (line_gap * index + 1), line_start),
                                      (space + (line_gap * index + 1), self.screen_h - line_start))
            else:
                self.draw_single_line((space + (line_gap * index + 1), space + 5),
                                      (space + (line_gap * index + 1), self.screen_h - space - 5))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.draw_lines()
            pygame.display.flip()


if __name__ == "__main__":
    game = ShuloGuti()
    game.run()
