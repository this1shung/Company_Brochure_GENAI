import json
from src.core.website import Website
from src.core.environment import openai, MODEL
from src.prompts.user_prompts import get_links_user_prompt

link_system_prompt = """You are provided with a list of links found on a webpage. 
You are able to decide which of the links would be most relevant to include in a brochure about the company, 
such as links to an About page, or a Company page, or Careers/Jobs pages.

You should respond in JSON as in this example:
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links(url):
    website = Website(url)
    response = openai.chat.completions.create(model=MODEL, messages=[
        {"role": "system", "content": link_system_prompt},
        {"role": "user", "content": get_links_user_prompt(website)}
    ],
    response_format={"type": "json_object"})

    result = response.choices[0].message.content
    return json.loads(result)  

def get_all_details(url):
    result = "Landing page:\n"
    result += Website(url).get_contents()
    
    links = get_links(url)
    print("Found links:", links)

    for link in links["links"]:
        if "url" in link and link["url"]:  
            result += f"\n\n{link['type']}\n"
            result += Website(link["url"]).get_contents()
        else:
            result += f"\n\n{link['type']}\nURL not found"
    
    return result
