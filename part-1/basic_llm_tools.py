import getpass
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun


welcome_template="""
Hello {name}! As an AI consultant. How can I help you?
Type '.exit' to close the program.
""" 

model = ChatOllama(model="llama3.2",temperature=0)

@tool
def my_tool_fn(country):
    """Get the capital city of a country."""
    capitals = {
        "India": "New Delhi",
        "USA": "Washington, D.C.",
        "UK": "London",
        "France": "Paris",
    }
    return capitals.get(country, "Capital not found")

search = DuckDuckGoSearchRun()

tools = [my_tool_fn, search]

agent = create_agent(tools=tools, model=model)

def show_welcome_message():
  name = getpass.getuser()
  prompt_template = PromptTemplate(input_variables=["name"], template=welcome_template)
  formatted_prompt = prompt_template.format(name=name)
  print(formatted_prompt)

def reply(query):
    for event in agent.stream(
        {
            "messages": [
                {"role": "user", "content": query}
            ]
        }
    ):
        print(event)
  # response = agent.invoke({"messages":[
  #   {"role":"user","content":query}
  # ]})
  # print(response["messages"][-1].content)  

def main():
    show_welcome_message()
    
    while(True):
      query = input("\nEnter your query: ")
      if query == '.exit':
        return
      reply(query=query)


if __name__ == "__main__":
    main()