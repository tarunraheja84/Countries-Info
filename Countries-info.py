import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v2/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 404:
        print(f"Error: {country_name} not found.")
        return None
    data = response.json()[0]
    return {
        "name": data["name"],
        "capital": data["capital"],
        "region": data["region"],
        "subregion": data["subregion"],
        "population": data["population"],
        "languages": [lang["name"] for lang in data["languages"]]
    }

print("Welcome to the Language & Country Learning Tool!")
print("Enter a country name to learn about its language and other information.")
while True:
    country_name = input("Enter a country name (or 'quit' to exit): ")
    if country_name.lower() == "quit":
        break
    country_info = get_country_info(country_name)
    if country_info:
        print(f"Language(s) spoken in {country_info['name']}:")
        for language in country_info['languages']:
            print(f"- {language}")
        print(f"Capital: {country_info['capital']}")
        print(f"Region: {country_info['region']}")
        print(f"Subregion: {country_info['subregion']}")
        print(f"Population: {country_info['population']}")
        print()

