from src.core.environment import openai, MODEL
from src.extractors.link_extractor import get_all_details
from src.prompts.user_prompts import get_brochure_user_prompt

# System prompt directly in the module
brochure_system_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
Include details of company culture, customers and careers/jobs if you have the information."

def create_brochure(company_name, url):
    details = get_all_details(url)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url, details)}
        ],
    )
    result = response.choices[0].message.content
    return result