from utils import run_llama

def slogan_creator(company):
    prompt = f"Generate 5 catchy business slogans for:\n{company}"
    return run_llama(prompt)

if __name__ == "__main__":
    company = input("Company/Product: ")
    print(slogan_creator(company))
