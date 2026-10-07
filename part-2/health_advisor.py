from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

#1- Chef
chef = Agent(
    role="chef",
    goal="Give 5 different recipes using ingredients : {ingredients}",
    backstory="You're  a Chef who has experience on cooking delicious foods"
              "Your expertize lies in recommending some new foods to the customers"
              "Please generate and give recipe of 5 different foods using this ingredients : {ingredients} "
              "describing stepwise process, time to cook, other ingredients needed and calorie count"
              "Your recipe will be critically analyzed by nutritionist to recommend food for diabetes patients ",
    llm=llm,
	  verbose=True
)

2# Nutritionist
nutritionist = Agent(
    role="nutritionist",
    goal="Critically analyze the recipe given by chef using these ingredients: {ingredients}",
    backstory="You're a nutritionist and have good knowledge on working with Diabetic patients "
              "There are recipe recommended by chef using these ingredients : {ingredients}. "
              "please critically analyze the recipe and suggest best food out of given 5 for Diabetic patients"
              "Also give reasons why you dont recommend other 4 recipes and choose this one",
    llm=llm,
    verbose=True
)

cook = Task(
    description=(
        "1. Write recipe of 5 different foods using these ingredients  : {ingredients}.\n"
    ),
    expected_output="5 different recipes using {ingredients}"
                    "Stepwise guide to cook"
                    "List of all additional ingredients required for cooking"
                    "The expected taste of the food",
    agent=chef,
)

recommend = Task(
    description=(
        "1. Read the receipes provided by chef using {ingredients} \n"
        "2. critically analyze all receipes keeping in mind what should suit to diabetic patients.\n"
        "3. Suggest one best food out of all 5 receipes given by chef.\n"
        "4. Prove that other 4 receipes suggested by chef is not good for diabetic patients.\n"

    ),
    expected_output="A well-written critical pointwise analysis of all 5 recipes using {ingredients}"
                    "Suggest one receipe to diabetic patients based on your own knowledge and evidence "
                    "Reject all other 4 receipes with knowledge and evidence "
                    "Finally, give the stepwoise receipe of what you selected and a nice message",
    agent=nutritionist,
)

crew = Crew(
    agents=[chef, nutritionist],
    tasks=[cook, recommend],
    verbose=True
)

def main():
    ingredient = input("Enter ingredient name: ")
    if ingredient == '.exit':
        return
    result = crew.kickoff(inputs={"ingredients": ingredient})
    print(result)
  
if __name__ == "__main__":
  main()
