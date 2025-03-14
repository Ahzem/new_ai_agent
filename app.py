from dotenv import load_dotenv
from agents.agent_team import create_agent_team
from agents.web_search_agent import create_web_search_agent
from agents.finance_agent import create_finance_agent

def display_menu():
    print("\nAvailable Agents:")
    print("1. Web Search Agent")
    print("2. Finance Agent")
    print("3. Agent Team")
    print("4. Exit")

def main():
    load_dotenv()

    # Create instances of agents
    web_search_agent = create_web_search_agent()
    finance_agent = create_finance_agent()
    agent_team = create_agent_team()

    print("Welcome to AI Agent System!")
    
    while True:
        display_menu()
        choice = input("\nSelect an agent (1-4): ").strip()
        
        if choice == '4':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select a number between 1 and 4.")
            continue

        question = input("\nEnter your question: ").strip()
        
        if not question:
            print("Please enter a valid question.")
            continue

        print("\nProcessing your request...\n")
        
        if choice == '1':
            web_search_agent.print_response(question)
        elif choice == '2':
            finance_agent.print_response(question)
        elif choice == '3':
            agent_team.print_response(question)

if __name__ == "__main__":
    main()