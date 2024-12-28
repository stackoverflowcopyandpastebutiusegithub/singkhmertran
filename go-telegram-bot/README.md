# Go Telegram Bot

This project is a Telegram bot implemented in Go that processes user input and responds with translations based on a predefined dictionary.

## Project Structure

```
go-telegram-bot
├── src
│   ├── main.go          # Entry point of the application
│   ├── handlers
│   │   └── singinoutkhmer.go  # Logic for processing user input
│   └── types
│       └── types.go     # Custom types and structures
├── go.mod               # Module definition and dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd go-telegram-bot
   ```

2. **Install dependencies:**
   Ensure you have Go installed, then run:
   ```
   go mod tidy
   ```

3. **Set up your Telegram bot:**
   - Create a new bot using the BotFather on Telegram and obtain your bot token.
   - Update the bot token in `src/main.go`.

4. **Run the bot:**
   ```
   go run src/main.go
   ```

## Usage

- Send messages to the bot, and it will respond with translations based on the input processed through the logic defined in `src/handlers/singinoutkhmer.go`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.