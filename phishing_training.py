import time

def print_header(title):
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50)

def introduction():
    print_header("🛡️ Welcome to Phishing Awareness Training 🛡️")
    print("In this module, you will learn how to identify phishing attacks.")
    print("Phishing is a cyber attack where attackers disguise themselves as a trustworthy entity")
    print("to trick you into revealing sensitive information like passwords or credit card numbers.\n")
    
    print("Key Red Flags to watch out for:")
    print("1. Urgent or threatening language (e.g., 'Your account will be suspended!').")
    print("2. Suspicious sender email addresses (e.g., support@paypal-update-123.com).")
    print("3. Generic greetings (e.g., 'Dear Customer' instead of your name).")
    print("4. Unexpected attachments or weird links.")
    input("\nPress Enter to start the Quiz...")

def quiz():
    print_header("🧠 Phishing Awareness Quiz 🧠")
    score = 0
    total_questions = 3
    
    # Question 1
    print("\nQ1: You receive an email from 'admin@bank-alert-security.com' saying:")
    print("    'Your bank account is compromised! Click here to verify your details immediately.'")
    print("What should you do?")
    print("  A) Click the link and verify my details to secure my account.")
    print("  B) Ignore the email and contact the bank directly using their official website.")
    print("  C) Reply to the email asking if it's real.")
    
    ans1 = input("Your answer (A/B/C): ").strip().upper()
    if ans1 == 'B':
        print("✅ Correct! Always contact the institution directly. The sender email is suspicious.")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is B. Never click links in urgent, suspicious emails.")
        
    time.sleep(1)
    
    # Question 2
    print("\nQ2: Which of the following URLs is most likely a phishing link for Facebook?")
    print("  A) https://www.facebook.com/login")
    print("  B) https://en-gb.facebook.com/")
    print("  C) http://www.faceb00k-login-secure.com/auth")
    
    ans2 = input("Your answer (A/B/C): ").strip().upper()
    if ans2 == 'C':
        print("✅ Correct! 'faceb00k' with zeros and lack of 'https' are clear red flags.")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is C. Look closely at spelling and HTTPS.")

    time.sleep(1)
    
    # Question 3
    print("\nQ3: What is 'Social Engineering' in the context of phishing?")
    print("  A) Hacking into a social media server.")
    print("  B) Manipulating people into giving up confidential information.")
    print("  C) Creating fake social media profiles.")
    
    ans3 = input("Your answer (A/B/C): ").strip().upper()
    if ans3 == 'B':
        print("✅ Correct! Phishing relies heavily on psychological manipulation.")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is B.")

    time.sleep(1)
    
    # Final Results
    print_header("🏆 Training Completed 🏆")
    print(f"Your Score: {score} out of {total_questions}")
    if score == total_questions:
        print("Excellent! You are a Phishing Detection Master! 🌟")
    elif score >= 1:
        print("Good job! But keep your eyes open for red flags. 👀")
    else:
        print("You might be at risk! Please review the training material again. 🚨")

def main():
    introduction()
    quiz()
    print("\nThank you for completing the Phishing Awareness Module by Md Mudassir Ansari.")

if __name__ == "__main__":
    main()
