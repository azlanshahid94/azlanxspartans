import time

def fancy_banner():
    """Display a professional multi-line SPARTANS banner"""
    banner = """
    ███████╗██████╗  █████╗ ████████╗ █████╗ ███╗   ██╗███████╗
    ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██╔════╝
    █████╗  ██████╔╝███████║   ██║   ███████║██╔██╗ ██║█████╗  
    ██╔══╝  ██╔═══╝ ██╔══██║   ██║   ██╔══██║██║╚██╗██║██╔══╝  
    ███████╗██║     ██║  ██║   ██║   ██║  ██║██║ ╚████║███████╗
    ╚══════╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
    """
    
    for line in banner.split("\n"):
        print(line)
        time.sleep(0.1)

def main():
    fancy_banner()
    print("\nWelcome to Spartans Tool! Choose an option:\n")
    
    while True:
        print("1️⃣  Post Tool")
        print("2️⃣  Convo Tool")
        print("3️⃣  Facebook Account")
        print("4️⃣  Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            print("\n📝 Opening Post Tool...\n")
            # Add post tool functionality here
        elif choice == "2":
            print("\n💬 Opening Convo Tool...\n")
            # Add conversation tool functionality here
        elif choice == "3":
            print("\n🔗 Opening Facebook Account...\n")
            # Add Facebook account functionality here
        elif choice == "4":
            print("\n👋 Exiting... Goodbye!")
            break
        else:
            print("\n❌ Invalid choice, please try again!\n")

if __name__ == "__main__":
    main()
