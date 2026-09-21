import re

def normalize_input(user_input: str) -> str:
    cleaned = user_input.lower().strip()
    cleaned = re.sub(r'[^\w\s]', '', cleaned)
    return cleaned

def run_chatbot():
    print("🤖 Bot: Hello! I'm your assistant. Type 'help' to see options or 'exit' to quit.")
    
    current_state = "main"
    
    while True:
        try:
            user_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\n🤖 Bot: Session terminated. Goodbye!")
            break
            
        normalized = normalize_input(user_input)
        
        if normalized in ["exit", "quit", "bye"]:
            print("🤖 Bot: Goodbye! Have a great day.")
            break
            
        # Nested state logic router
        if current_state == "main":
            if "help" in normalized:
                print("🤖 Bot: Here are the topics I can help with:\n- Account (manage profile, passwords)\n- Technical (troubleshoot errors, bugs)\n- Billing (invoices, refunds)")
            elif "account" in normalized:
                current_state = "account"
                print("🤖 Bot: [Account Menu] Would you like to 'reset password' or 'update profile'? (Type 'back' to return)")
            elif "technical" in normalized or "tech" in normalized:
                current_state = "technical"
                print("🤖 Bot: [Technical Menu] Are you facing a 'connection error' or 'app crash'? (Type 'back' to return)")
            elif "billing" in normalized:
                current_state = "billing"
                print("🤖 Bot: [Billing Menu] Do you need help with an 'invoice' or a 'refund'? (Type 'back' to return)")
            else:
                print("🤖 Bot: I didn't quite catch that. Type 'help' to see available options.")
                
        elif current_state == "account":
            if "back" in normalized or "main" in normalized:
                current_state = "main"
                print("🤖 Bot: Returned to main menu. Type 'help' for options.")
            elif "reset" in normalized or "password" in normalized:
                print("🤖 Bot: To reset your password, check your email for the secure recovery link.")
            elif "profile" in normalized:
                print("🤖 Bot: To update your profile, head over to your user dashboard settings.")
            else:
                print("🤖 Bot: I can only help with 'reset password' or 'update profile' here. Type 'back' to return.")
                
        elif current_state == "technical":
            if "back" in normalized or "main" in normalized:
                current_state = "main"
                print("🤖 Bot: Returned to main menu. Type 'help' for options.")
            elif "connection" in normalized or "error" in normalized:
                print("🤖 Bot: Please check your internet connection or restart your router. Let me know if that works!")
            elif "crash" in normalized or "app" in normalized:
                print("🤖 Bot: Try clearing your app cache or reinstalling the latest version.")
            else:
                print("🤖 Bot: I can only assist with 'connection error' or 'app crash' in this section. Type 'back' to return.")
                
        elif current_state == "billing":
            if "back" in normalized or "main" in normalized:
                current_state = "main"
                print("🤖 Bot: Returned to main menu. Type 'help' for options.")
            elif "invoice" in normalized:
                print("🤖 Bot: Your latest invoices can be downloaded directly from your billing portal.")
            elif "refund" in normalized:
                print("🤖 Bot: Refunds typically take 3 to 5 business days to process back to your original payment method.")
            else:
                print("🤖 Bot: I can only help with 'invoice' or 'refund' inquiries here. Type 'back' to return.")

if __name__ == "__main__":
    run_chatbot()
