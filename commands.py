import os

def handle_command(command):
    if command == "/help":
        print("💡 Available Commands: /help, /clear, /exit")
        return True
    elif command == "/clear":
        os.system('clear' if os.name == 'posix' else 'cls')
        return True
    return False

