from src.generators.brochure_generator import create_brochure

def main():
    print("BrochureForge - Automated Business Brochure Generator")
    company_name = "Huggingface"
    company_url = "https://huggingface.co"
    
    print(f"\nGenerating brochure for {company_name}...")
    brochure = create_brochure(company_name, company_url)
    
    filename = f"{company_name.replace(' ', '_')}_brochure.md"
    with open(filename, "w") as f:
        f.write(brochure)
    print(f"Brochure saved to {filename}")

if __name__ == "__main__":
    main()