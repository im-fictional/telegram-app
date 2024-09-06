# Telegram Bot using Pyrogram

## Project Description

This project is a Telegram bot written in Python using the **Pyrogram** library. The bot allows users to automate various actions in Telegram, such as spamming, editing messages with a typing effect, copying messages, and even processing voice messages by converting them to text.

## Features

### 1. Command `.print text`
- **Purpose**: This command edits a message with a typing effect, adding each letter one by one to mimic typing.
- **Usage**: Type `.print text`, and the bot will start editing the message, showing the text being "typed" letter by letter.

### 2. Command `.spam text n`
- **Purpose**: This command spams the given message a specified number of times.
- **Usage**: Type `.spam text number_of_times`, and the bot will send the specified message the desired number of times.

### 3. Command `.copy n`
- **Purpose**: Spams a reply to a message. Whether it's text, stickers, or images, the bot will repeat them.
- **Usage**: Reply to the message you want to copy and type `.copy number_of_times`.

### 4. Command `.voice`
- **Purpose**: Processes a voice message and converts it to text using the Google Speech Recognition API.
- **Usage**: Reply to a voice message with the `.voice` command, and the bot will try to recognize the speech and send the transcribed text as a reply.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```
   
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Fill in your API credentials in the file:
    ```python
    app = Client(
        "user",
        api_id=YOUR_API_ID,
        api_hash="YOUR_API_HASH"
    )
    ```

4. Run the bot:
    ```bash
    python bot.py
    ```

## Required Libraries

- **Pyrogram**: To interact with Telegram API.
- **SpeechRecognition**: For voice-to-text conversion.
- **Soundfile**: To handle audio files.
- **time, random, os**: Standard libraries for time management and file operations.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to update or adjust any details as necessary!
