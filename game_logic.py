from home_screen import HomeScreen

import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


class GameLogic:
    def __init__(self, screen):
        self.screen = screen
        self.home_screen = HomeScreen()

        self.screen.onclick(self.start_game, btn=1)

    def start_game(self, x, y):
        self.clear_main_screen()
        self.game_loop()

    def clear_main_screen(self):
        self.home_screen.clear_main_screen()

    def game_loop(self):
        snake = Snake()
        food = Food()
        scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkey(snake.up, "Up")
        self.screen.onkey(snake.down, "Down")
        self.screen.onkey(snake.left, "Left")
        self.screen.onkey(snake.right, "Right")

        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            snake.move()

            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()

            if (
                    snake.head.xcor() > 280
                    or snake.head.xcor() < -280
                    or snake.head.ycor() > 280
                    or snake.head.ycor() < -280
            ):
                game_is_on = False
                scoreboard.game_over()

            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    game_is_on = False
                    scoreboard.game_over()
