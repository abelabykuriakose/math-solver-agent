from langchain_google_genai import ChatGoogleGenerativeAI
from tools import math_tool_registry

class MathAgent:
    def __init__(self):
        # We set temperature to 0.0 because math requires absolute precision, zero creativity!
        self.llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.0)
        self.tools = {tool.name: tool for tool in math_tool_registry}
        self.llm_with_tools = self.llm.bind_tools(math_tool_registry)

    def solve(self, word_problem: str) -> str:
        # System instructions guiding the model's scratchpad loop
        system_instructions = (
            "You are an elite, highly precise Mathematical Operations Agent.\n"
            "Your task is to solve complex word problems by breaking them down into steps.\n"
            "You have access to calculation tools: 'add', 'multiply', and 'power'.\n"
            "Do not attempt to compute large or complex operations in your head. Call the appropriate tool instead.\n"
            "Always state your current step plan before triggering a tool."
        )
        
        print("\n🧠 AI Thought Process Initialized...")
        
        # First Agent Pass
        ai_msg = self.llm_with_tools.invoke(f"{system_instructions}\n\nProblem: {word_problem}")
        
        # Keep processing tool calls in a loop until the AI stops calling tools and reaches a conclusion
        context_history = [ai_msg]
        
        while ai_msg.tool_calls:
            for tool_call in ai_msg.tool_calls:
                name = tool_call["name"]
                args = tool_call["args"]
                
                # Fetch the corresponding tool from our registry and execute it
                active_tool = self.tools[name]
                tool_output = active_tool.invoke(args)
                
                # Create a quick log string to pass back into the AI's short-term context
                feedback = f"Tool '{name}' execution completed. Output Result: {tool_output}"
                print(f"📥 [Passing back to AI Context] -> {feedback}")
                
                # Ask the model what its next step is based on this calculation result
                ai_msg = self.llm_with_tools.invoke(
                    f"{system_instructions}\n\nProblem: {word_problem}\n\nPast Progress Context: {feedback}"
                )
                
        # 🌟 PLACE THE CHANGE HERE 🌟
        # Ensure the final output is extracted cleanly as plain text prose
        content = ai_msg.content
        if isinstance(content, list) and len(content) > 0:
            if isinstance(content[0], dict) and "text" in content[0]:
                return content[0]["text"]
        elif isinstance(content, str):
            return content
        return str(content)