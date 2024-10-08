import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedIn.linkedIn import scrape_linkedin_profile

load_dotenv()  # Load the environment



if __name__ == "__main__":

    summary_template = """
        On given information {information} about a person, create:
        1. a short summary 
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")    #temperature defines the creativity in the responses, 0 represents no creativity

    llm =  ChatOllama(model="llama3")   # using  llama3 MOdel

    # llm = ChatOllama(model="mistral")  # using  mistral MOdel

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/rsaxenaishabh/", mock=True)

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
