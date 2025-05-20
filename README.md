# ChatRoom

A real-time chat application built with Django and Django Channels.

## Features

- Real-time messaging using WebSockets
- User authentication (signup, login, logout)
- Chat rooms with unique URLs
- Profile management
- Password change functionality

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chatroom
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Server

### For WebSocket Support (Recommended for Chat)

Run the server using Daphne (ASGI server):
```bash
daphne -b 0.0.0.0 -p 8000 chatroom.asgi:application
```

### For Regular Django Development (No WebSocket Support)

Run the server using Django's development server:
```bash
python manage.py runserver
```

## Testing the Chat

1. Open your browser and go to:
   ```
   http://localhost:8000/
   ```

2. Sign up or log in with a user account.

3. Join or create a chat room.

4. Send messages in the chat room.

5. Check the browser console (F12) for WebSocket connection status:
   - You should see: "WebSocket connection established"
   - Messages should appear instantly in the chat window.

6. Test with multiple users:
   - Open another browser window or use incognito mode.
   - Log in as a different user and join the same chat room.
   - Send messages from both users to see real-time updates.

## Troubleshooting

- If WebSocket connections fail, ensure you are running the server with Daphne.
- Check the browser console for any error messages.
- Ensure all dependencies are installed correctly.

## License

This project is licensed under the MIT License. 