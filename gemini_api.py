import google.generativeai as genai
import os 


sys_prompt = """You are provided with the following extracted text content from an image:
{TEXT}
Answer the users question strictly based on the content of this text.
Extract specific details or provide relevant information only from the text provided.
Do not include external information or unrelated details in your response.
{USER_QUESTION}
"""



def get_extracted_details(text, usr_prompt):
   
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    final_prompt = sys_prompt.format(TEXT=text,USER_QUESTION=usr_prompt)

    try: 
        response = model.generate_content(final_prompt)
        return response.text
    except Exception as e:
        return e
