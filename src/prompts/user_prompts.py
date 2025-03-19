def get_links_user_prompt(website):
    """Generate user prompt for link extraction"""
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt

def get_brochure_user_prompt(company_name, url, details):
    """Generate user prompt for brochure creation"""
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += details
    user_prompt = user_prompt[:5_000]  # Truncate if more than 5,000 characters
    return user_prompt