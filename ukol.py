import requests
import json

ico = input("IČO subjekt: ")
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

response = requests.get(url)
data = response.json()

obchodni_jmeno = data.get('obchodniJmeno')
address = data.get('textovaAdresa')

print(obchodni_jmeno)
print(address)

search_name = input("Název subjektu pro vyhledání: ")

headers = {
    "accept": "application/json",
    "content-Type": "application/json",
}
data = json.dumps({"obchodniJmeno": search_name})

url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
response = requests.post(url, headers=headers, data=data)
response_data = response.json()

total_found = response_data.get('celkem')
print(f"Nalezeno subjektů: {total_found}")
for subjekt in response_data.get('ekonomickeSubjekty', []):
    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")

# bonusova uloha

def find_legal_form(code, legal_forms):
     for item in legal_forms:
        if item['kod'] == code:
             return item['nazev']
     return "Neznámá právní forma"
headers = {
     "accept": "application/json",
     "Content-Type": "application/json",
 }
data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
legal_forms_url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"
legal_response = requests.post(legal_forms_url, headers=headers, data=data)
legal_data = legal_response.json()
legal_forms = legal_data['ciselniky'][0]['polozkyCiselniku']

print(f"Nalezeno subjektů: {total_found}")
for subjekt in response_data.get('ekonomickeSubjekty', []):
     legal_form_name = find_legal_form(subjekt['pravniForma']['kod'], legal_forms)
     print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}, {legal_form_name}")