import time
from proxy_core import init_proxy
from agent_client import ask_ai
from commands import handle_command

def main():
    print("🚀 Initializing The Last God App...")
    init_proxy()
    time.sleep(1)
    
    print("\n✨ The Last God v1.0 (Claude Code Engine Active)")
    print("Type your query or '/help' for commands. Type 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input(" > ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                print("Exiting app. Bye!")
                break
            
            if user_input.startswith('/'):
                handle_command(user_input)
                continue
                
            print("⏳ Thinking...")
            response = ask_ai(user_input)
            print(f"\n{response}\n")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()

