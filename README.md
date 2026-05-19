# Training Telegram Bot
This project is a Telegram bot developed in Python for tracking workouts. The bot allows users to choose a training complex from a predefined list, go through exercises one by one, mark them as completed or skip them, and view their training history afterward. MySQL was used as the database management system, and the telebot framework was chosen to handle all Telegram interactions.

# Technology Stack
- Python 3.11;
- telebot;
- mysql-connector-python;
- MySQL;

# How to use it
### Clone repository
Firstly, the project should be cloned using the following command in the console:
```bash
git clone https://github.com/Temka0994/training-telegram-bot.git
```
After this navigate to the training-telegram-bot folder:
```bash
cd training-telegram-bot
```

### Requirements
Additionally, all the requirements should be downloaded using the following command:
```bash
pip install telebot mysql-connector-python
```

### Telegram Bot Token
You need to create a Telegram bot and obtain its token. This can be done via [@BotFather](https://t.me/BotFather) in Telegram.

Once you have the token, open [main.py](./main.py) and replace the placeholder value in the following line with your own token:
```python
bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')
```

### Database
You need to set up a MySQL database with the required tables for exercises, complexes, and history. Once the database is created, open [connection_manager.py](./connection_manager.py) and insert your database credentials (host, user, password, database name) into the `ConnectionManager` configuration.

The database stores the following data:
- **Exercises** — individual exercises with descriptions and image URLs;
- **Complexes** — training complexes grouping exercises by muscle group;
- **History** — a log of completed training sessions per user.

### Final step
Once everything is configured, run the bot with the following command:
```bash
python main.py
```

The bot will start polling for messages. Open Telegram, find your bot, and send the `/start` command to begin.

# Features
- Choose a training complex by muscle group: Legs, Arms, Shoulders, Back, or Core;
- View the full list of exercises in the selected complex before starting;
- Go through exercises one by one with photo and description;
- Mark each exercise as **Done** or **Skip** it;
- After completing a complex, the session is saved to the history;
- View your full training history at any time.