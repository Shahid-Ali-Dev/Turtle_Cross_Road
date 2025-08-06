# 🐢 Turtle Cross Road Game

A simple yet fun arcade-style crossing game made using the `turtle` graphics module in Python. The objective is to help the turtle player cross the road while avoiding fast-moving cars. With each successful crossing, the level increases and the game speeds up.

![Python](https://img.shields.io/badge/Made%20With-Python3-blue?style=flat-square)
![Module](https://img.shields.io/badge/Library-turtle-yellow?style=flat-square)
![Level](https://img.shields.io/badge/Difficulty-Beginner--Intermediate-green?style=flat-square)

---

## 🎮 Gameplay Features

- Move the turtle upward using the **Up Arrow key**
- Dodge the cars driving horizontally across the screen
- Each successful cross increases the game level and speed
- Game over message appears upon collision with a car

---

## 🧱 Project Structure

```text
turtle_cross_road/
│
├── main.py               # Main game loop
├── player.py             # Player class controlling the turtle

├── car_manager.py        # CarManager class handling car creation and movement
├── scoreboard.py         # Scoreboard class displaying level and game over
