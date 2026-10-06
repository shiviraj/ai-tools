import getpass
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

welcome_template = """
Hello {name}! As an AI consultant. How can I help you?
Type '.exit' to close the program.
"""

template = """
I want you to act as a consultant for a AI training
Return a list of topics and why it is important to learn in given area of AI
The description should be relevant to recent advancement in AI
What are some good topics to learn in {AI_topic}
"""

prompt = PromptTemplate(input_variables=["AI_topic"], template=template)
model = ChatOllama(model="llama3.2", temperature=0)
chain = prompt | model


def show_welcome_message():
    name = getpass.getuser()
    prompt_template = PromptTemplate(
        input_variables=["name"], template=welcome_template)
    formatted_prompt = prompt_template.format(name=name)
    print(formatted_prompt)


def reply(topic):
    response = chain.invoke({"AI_topic": topic})
    print(response.content)


def main():
    show_welcome_message()

    while (True):
        topic = input("\nEnter AI topic: ")
        if topic == '.exit':
            return
        reply(topic=topic)


if __name__ == "__main__":
    main()
