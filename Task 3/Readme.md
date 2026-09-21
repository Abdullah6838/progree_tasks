
# 🤖 CLI State-Based Chatbot

 A simple **command-line chatbot built with Python** that uses a state-based conversation system to guide users through different support categories.

 The chatbot provides assistance for:

 - 👤 **Account** — Password reset and profile updates
- 🛠️ **Technical** — Connection errors and app crashes
- 💳 **Billing** — Invoices and refunds

 ## ✨ Features

 - Interactive command-line interface
- State-based conversation routing
- Input normalization using Python's `re` module
- Account, technical, and billing support menus
- Navigation back to the main menu
- Supports `exit`, `quit`, and `bye` commands
- Handles `Ctrl+C` and `EOF` gracefully
- No external dependencies required

 ## 📁 Project Structure

```
Task 4/
│
├── main.py
└── README.md
```

 ## ⚙️ Requirements

 - Python 3.7 or higher
- No third-party packages are required

 The project uses Python's built-in `re` module.

 ## 🚀 How to Run

 ### 1\. Clone or download the project

 Place the Python file in your desired project directory.

 ### 2\. Open a terminal

 Navigate to the project directory:

```
cd Task 4
```

 ### 3\. Run the chatbot

```
python main.py
```


 ## 💬 How to Use

 When the chatbot starts, it displays:

```
🤖 Bot: Hello! I'm your assistant. Type 'help' to see options or 'exit' to quit.
```

 Type:

```
help
```

 to view the available support categories.

 ### Account Support

 Enter:

```
account
```

 The chatbot provides options for:

 - Reset password
- Update profile

 Example:

```
You: account

🤖 Bot: [Account Menu] Would you like to 'reset password' or 'update profile'? (Type 'back' to return)

You: reset password

🤖 Bot: To reset your password, check your email for the secure recovery link.
```

 ### Technical Support

 Enter:

```
technical
```

 or:

```
tech
```

 Available topics:

 - Connection errors
- App crashes

 Example:

```
You: technical

🤖 Bot: [Technical Menu] Are you facing a 'connection error' or 'app crash'? (Type 'back' to return)

You: connection error

🤖 Bot: Please check your internet connection or restart your router. Let me know if that works!
```

 ### Billing Support

 Enter:

```
billing
```

 Available topics:

 - Invoices
- Refunds

 Example:

```
You: billing

🤖 Bot: [Billing Menu] Do you need help with an 'invoice' or a 'refund'? (Type 'back' to return)

You: invoice

🤖 Bot: Your latest invoices can be downloaded directly from your billing portal.
```

 ## 🔙 Navigation

 Inside any submenu, type:

```
back
```

 or:

```
main
```

 to return to the main menu.

 ## 🚪 Exit the Chatbot

 The chatbot can be closed using any of these commands:

```
exit
quit
bye
```

 You can also terminate the program with:

```
Ctrl+C
```

 or an EOF signal.

 ## 🧠 How It Works

 The chatbot uses a simple **finite-state machine (FSM)** approach.

 The main states are:

```
main
 ├── account
 ├── technical
 └── billing
```

 The `current_state` variable determines which section of the chatbot is active.

 For example:

```
current_state = "main"
```

 When the user selects Account:

```
current_state = "account"
```

 The chatbot then processes input according to the rules for the `account` state.

 Typing `back` changes the state back to:

```
current_state = "main"
```

 ## 🧹 Input Normalization

 User input is normalized before being processed:

```
def normalize_input(user_input: str) -> str:
    cleaned = user_input.lower().strip()
    cleaned = re.sub(r'[^\w\s]', '', cleaned)
    return cleaned
```

 This function:

 1. Converts input to lowercase.
2. Removes leading and trailing whitespace.
3. Removes punctuation and special characters.

 For example:

```
"  HELLO!!! "
```

 becomes:

```
"hello"
```

 ## 🛠️ Technologies Used

 - **Python**
- **Regular Expressions (`re`)**
- **Command-Line Interface (CLI)**
- **Finite-State Machine (FSM) concept**

 ## 🔮 Possible Improvements

 Future versions could include:

 - Natural-language processing
- More detailed troubleshooting
- Persistent user sessions
- Database integration
- Logging and analytics
- Web-based interface
- GUI interface
- API integration
- More advanced intent detection
- Unit tests
- Configuration files for chatbot responses
