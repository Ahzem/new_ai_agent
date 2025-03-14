from dotenv import load_dotenv
from agents.agent_team import create_agent_team
from agents.web_search_agent import create_web_search_agent
from agents.finance_agent import create_finance_agent
from agents.knowledge_base_agent import create_knowledge_base_agent

def display_menu():
    print("\nAvailable Agents:")
    print("1. Web Search Agent")
    print("2. Finance Agent")
    print("3. Agent Team")
    print("4. Company Knowledge Agent")
    print("5. Exit")

def main():
    load_dotenv()

    # Create instances of agents
    web_search_agent = create_web_search_agent()
    finance_agent = create_finance_agent()
    agent_team = create_agent_team()
    knowledge_agent = create_knowledge_base_agent()

    print("Welcome to AI Agent System!")
    
    while True:
        display_menu()
        choice = input("\nSelect an agent (1-5): ").strip()
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a number between 1 and 5.")
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
        elif choice == '4':
            knowledge_agent.print_response(question)

if __name__ == "__main__":
    main()