import pygame
import sys
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "50, 308"


class ShuloGuti:
    def __init__(self):
        self.board = {
            'protagonist': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            'antagonist': [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
        }

        self.current_turn = 1  # protagonist 1 || antagonist 0
        self.screen_w = 343
        self.screen_h = 500
        self.bg_color = (80, 80, 80)
        self.line_color = (200, 200, 200)
        self.circle_size = 10

        self.line_gap = 75
        self.line_start = 100
        self.space = 20

        self.protagonist_color = (0, 255, 0)
        self.antagonist_color = (255, 0, 0)

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption('ShuloGuti Game')

    def draw_single_line(self, start_pos, end_pos, width=2):
        pygame.draw.line(self.screen, self.line_color, start_pos, end_pos, width)

    def draw_lines(self):
        
        # Diagonal lines
        diagonal_lines = [
            ((self.space, self.line_start + self.line_gap * 2), (self.screen_w - self.space - self.line_gap, self.line_start - self.line_gap), 3),
            ((self.space, self.line_start + self.line_gap * 2), (self.space + self.line_gap * 3, self.line_start + self.line_gap * 5), 3),
            ((self.screen_w - self.space, self.line_start + self.line_gap * 2), (self.space + self.line_gap, self.line_start - self.line_gap), 3),
            ((self.screen_w - self.space, self.line_start + self.line_gap * 2), (self.space + self.line_gap, self.line_start + self.line_gap * 5), 3),
            ((self.space, self.line_start), (self.space + self.line_gap * 4, self.line_start + self.line_gap * 4), 3),
            ((self.screen_w - self.space, self.line_start), (self.space, self.line_start + self.line_gap * 4), 3)
        ]
        for start_pos, end_pos, width in diagonal_lines:
            self.draw_single_line(start_pos, end_pos, width)

        # Horizontal lines
        horizontal_lines = [
            ((self.space + self.line_gap, self.screen_h - self.space - 5), (self.space + self.line_gap * 3, self.screen_h - self.space - 5), 2),
            ((self.space + self.line_gap * 1.5 - 5, self.screen_h - self.space - (self.line_gap / 2)),
             (self.space + self.line_gap * 2.5 + 5, self.screen_h - self.space - (self.line_gap / 2)), 2),
            ((self.space + self.line_gap, self.space + 4), (self.space + self.line_gap * 3, self.space + 4), 2),
            ((self.space + self.line_gap * 1.5 - 5, self.space + (self.line_gap / 2)),
             (self.space + self.line_gap * 2.5 + 5, self.space + (self.line_gap / 2)), 2)
        ]
        for start_pos, end_pos, width in horizontal_lines:
            self.draw_single_line(start_pos, end_pos, width)

        # Vertical and horizontal grid lines
        for index in range(5):
            self.draw_single_line((self.space, (self.line_gap * index + 1) + self.line_start),
                                  (self.screen_w - self.space, self.line_start + (self.line_gap * index + 1)))
            if index != 2:
                self.draw_single_line((self.space + (self.line_gap * index + 1), self.line_start),
                                      (self.space + (self.line_gap * index + 1), self.screen_h - self.line_start))
            else:
                self.draw_single_line((self.space + (self.line_gap * index + 1), self.space + 5),
                                      (self.space + (self.line_gap * index + 1), self.screen_h - self.space - 5))

    def draw_guti(self, position, color=None):
        if color is None:
            color = self.protagonist_color
        pygame.draw.circle(self.screen, color, position, self.circle_size)

    def get_guti_position(self, index=1):
        grid = [(x, y) for y in range(5) for x in range(5)]
        for i in range(5 if (index >= 7) and (index <= 31) else 0):
            for j in range(5):
                if i == grid[index - 7][0] and j == grid[index - 7][1]:
                    return (
                        self.space + (self.circle_size / 3) + self.line_gap * i,
                        self.line_start + (self.circle_size / 3) + self.line_gap * j
                    )

        for i in range(index if index <= 3 else 0):
            if index == i + 1:
                return (
                    self.line_gap + self.space + (self.circle_size / 3) + self.line_gap * i,
                    self.space + self.circle_size / 2
                )

        for i in range(1, 4 if (index >= 4) and (index <= 6) else 0):
            if index + 1 == i + 4:
                return (
                    self.line_gap * 0.5 * i + self.space + (self.circle_size / 3) + self.line_gap,
                    self.space + (self.circle_size / 10) + (self.line_gap / 2)
                )

        for i in range(3 if (index >= 35) and (index <= 37) else 0):
            if index == i + 35:
                return (
                    self.line_gap + self.space + (self.circle_size / 3) + self.line_gap * i,
                    self.space + (self.circle_size / 2) + self.line_gap * 6
                )

        for i in range(1, 4 if (index >= 32) and (index <= 34) else 0):
            if index + 1 == i + 32:
                return (
                    self.line_gap * 0.5 * i + self.space + (self.circle_size / 3) + self.line_gap,
                    self.space + (self.circle_size / 1) + (self.line_gap / 2) + self.line_gap * 5
                )

    def is_guti_clicked(self, guti_pos, mouse_pos):
        distance = ((guti_pos[0] - mouse_pos[0]) ** 2 + (guti_pos[1] - mouse_pos[1]) ** 2) ** 0.5
        return distance <= self.circle_size

    def draw_text(self, text, position, font_size=20, color=(255, 255, 255)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def run(self):
        selected_guti_index = None

        while True:
            gutis_assign = []

            for index in self.board['protagonist']:
                gutis_assign.append((
                    self.get_guti_position(index),
                    self.protagonist_color,
                    index
                ))

            for index in self.board['antagonist']:
                gutis_assign.append((
                    self.get_guti_position(index),
                    self.antagonist_color,
                    index
                ))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for position, _, index in gutis_assign:
                        eligible = None
                        if self.current_turn == 1:
                            eligible = (index >= 1) and (index <= 16)
                        else:
                            eligible = (index >= 17) and (index <= 32)

                        if self.is_guti_clicked(position, mouse_pos) and eligible:
                            selected_guti_index = index

            self.screen.fill(self.bg_color)
            self.draw_lines()

            # Draw gutis
            for position, color, index in gutis_assign:
                if selected_guti_index == index:
                    self.draw_guti(position, (0, 0, 255))
                else:
                    self.draw_guti(position, color)

            score = 2
            # Winning status
            self.draw_text(f"Score: {score}", (self.space, self.space + self.line_gap / 2))

            pygame.display.flip()


if __name__ == "__main__":
    game = ShuloGuti()
    game.run()
