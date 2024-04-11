# Outline SSH Refresher Bot

This Python application is designed to serve as a Telegram bot named "Outline SSH Refresher Bot." The bot facilitates the generation of SSH keys and QR codes for users. It interacts with users through Telegram and utilizes a PostgreSQL database to store user IDs.

## Setup

## **IT WILL ALL WORK AUTOMATICLY IF YOU RUN IT WITH DOCKER COMPOSE**

1. **Dependencies**: Ensure you have the required dependencies installed. The bot uses psycopg2 for interacting with the PostgreSQL database.

2. **Database Configuration**: Update the database connection details in the Database class constructor to match your PostgreSQL setup.

3. **Telegram Bot Token**: Obtain a Telegram bot token from the BotFather and configure it in your application code.

## Database Class

The Database class encapsulates interactions with the PostgreSQL database. It performs the following operations:

- **Initialization**: Establishes a connection to the PostgreSQL database and creates a table named users if it does not already exist.
- **save_id**: Saves a user ID to the ids column in the users table.
- **get_ids**: Retrieves all user IDs stored in the database as a set.
- **close**: Closes the database connection and cursor.

## Logging

The application utilizes Python's logging module to provide information-level logs. Logs are written to the console, helping track the bot's actions and database interactions.

## Usage

Integrate the provided Database class into your Telegram bot application to manage user IDs and interactions effectively. Customize the bot's functionality to generate SSH keys, QR codes, or other features based on your requirements.

Feel free to expand upon this codebase and enhance the capabilities of your Outline SSH Refresher Bot according to your needs.

# Thanks jadolg for wrapped API!
link to original repo https://github.com/jadolg/outline-vpn-api