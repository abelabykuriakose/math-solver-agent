from dotenv import load_dotenv
from agent import MathAgent

load_dotenv()

def main():
    agent = MathAgent()
    
    print("\n" + "="*60)
    print("📐 Welcome to your Interactive Math AI Agent! 📐")
    print("Type 'exit' or 'quit' to end the session.")
    print("="*60 + "\n")
    
    while True:
        user_problem = input("Describe a math problem to solve: ")
        if user_problem.strip().lower() in ['exit', 'quit']:
            print("\n👋 Calculator session closed. Happy coding!\n")
            break
            
        if not user_problem.strip():
            continue
            
        # Execute the multi-step reasoning solver
        final_answer = agent.solve(user_problem)
        
        print("\n🏁 " + "-"*20 + " VERIFIED SOLUTION " + "-"*20)
        print(final_answer)
        print("="*60 + "\n")

if __name__ == "__main__":
    main()