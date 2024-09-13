import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI


GEMINI_API_KEY = os.environ['GOOGLE_AI_API_KEY']
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)


def get_response(query):
    response = ""
    for chunks in llm.stream(query):
        print(chunks, end="")
        response += chunks
    
    return response


def build_prompt(code):

  template = """As a proficient software engineer with expertise in code validation and optimization, your task is to thoroughly examine the provided code for any errors or potential improvements. If the code is error-free, suggest enhancements to handle any unexpected scenarios, if any. Offer alternative, more efficient ways to accomplish the task by providing the optimized code and an example. Additionally, offer guidance to improve the coder's skills based on the code you received.
  Withing your response, always include the code within three backticks like ```#code``` in-order to clearly seperate out the code & text from each other.
  
  Code to examine:
  ```
  {code_to_analyze}
  ```

  Output: """

  prompt_template = PromptTemplate.from_template(template)

  prompt = prompt_template.format(code_to_analyze=code)
  print(prompt)
  
  return prompt


st.title(":blue[CodeLens]:computer::mag:")
st.subheader("""CodeLense provides code validation by pointing out errors or bugs in your code, suggests code optimization & recommendations on your code!""")

st.markdown("___")
st.markdown("#### Provide your code below to and click on 'Analyze' button below to get started!")
code = st.text_area("Code to Analyze:", key="codeInput")
submit_button = st.button("Analyze")
print(code)


if submit_button:
  my_prompt = build_prompt(code)
  code_analysis_result = get_response(my_prompt)

  st.write(code_analysis_result)