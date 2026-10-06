import getpass
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

welcome_template="""
Hello {name}! How can I help you today?
Type '.exit' to close the program.
  """ 
  
model = ChatOllama(model="llama3.2",temperature=0)

def show_welcome_message():
  name = getpass.getuser()
  prompt_template = PromptTemplate(input_variables=["name"], template=welcome_template)
  formatted_prompt = prompt_template.format(name=name)
  print(formatted_prompt)

def reply(question):
  response = model.invoke(question)
  print(response.content)  

def main():
    show_welcome_message()
    
    while(True):
      question = input("\nHow may I help you: ")
      if question == '.exit':
        return
      reply(question=question)


if __name__ == "__main__":
    main()