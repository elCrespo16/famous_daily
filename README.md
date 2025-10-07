# Famous Daily

**Famous Daily** is a Python + Docker application that automatically posts a predefined comment on the latest Instagram publication of a specified account, every day.
It is designed to be easily configurable via `.yaml` files and environment variables, with scheduling handled through `cron`.

---

## 🚀 Features

* Automatically comments on the latest Instagram post of a user.
* Daily scheduling via `cron`.
* Configuration through simple `.yaml` files in the `/data` directory.
* Telegram bot integration for notifications (optional).
* Easy installation with `./install.sh`.

---

## 📂 Project Structure

```
.
├── data/                # Folder containing .yaml files for target accounts
│   ├── example.yaml
│   └── ...
├── .env                 # Environment variables
├── docker-compose.yml   # Docker configuration
├── Dockerfile           # Docker build file
├── install.sh           # Script to build and install cron job
└── README.md            # Documentation
```

---

## 🛠️ Requirements

The application is containerized, so you only need **Docker** and **Docker Compose** installed.
Internally, it uses the following Python dependencies:

* [instagrapi==2.0.0](https://github.com/adw0rd/instagrapi) – Instagram private API client
* [pyTelegramBotAPI==4.14.0](https://github.com/eternnoir/pyTelegramBotAPI) – Telegram bot integration
* [ipython==8.17.2](https://ipython.org/) – Debugging / REPL
* [pydantic==1.10.9](https://docs.pydantic.dev/) – Data validation
* [PyYAML==6.0.1](https://pyyaml.org/) – YAML configuration parsing
* [Pillow>=10.1.0](https://pillow.readthedocs.io/) – Image processing

---

## ⚙️ Configuration

### 1. Environment variables

Create a `.env` file in the project root with the following keys:

```env
USERNAME=your_instagram_username
PASSWORD=your_instagram_password
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
DATA_PATH=./data
```

> 🔒 **Security note:** Never commit your `.env` file to version control.

---

### 2. YAML files in `/data`

Each account to target must have a `.yaml` file inside `/data`.
Example (`data/example.yaml`):

```yaml
name: Adele
username: adele
```

* `name` → Just a display name (for logging).
* `username` → The Instagram username to comment on.

---

## ▶️ Usage

### Installation

Run the provided script to build the image and set up the cron job:

```bash
./install.sh
```

This will:

1. Build the Docker image.
2. Install the cron job that runs `docker compose up` daily.

---

### Running manually

You can also run the app manually without waiting for cron:

```bash
docker compose up
```

---

## 📝 Notes

* The script will always comment the **same message** each day on the **latest post** of the target account(s).
* To change the message, edit the project’s source code (message handling section).
* Ensure your Instagram account has **two-factor authentication disabled** or handled via cookies, otherwise the login may fail.

---

## 📬 Telegram Notifications

If `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are set, the app will send notifications to your Telegram chat when comments are successfully posted (or if errors occur).

---

## 🔧 Development

To rebuild and start fresh:

```bash
docker compose build --no-cache
docker compose up
```

---

## 📜 License

MIT License. Free to use and modify.

