import requests

class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.exchange_rate

def get_usd_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['rate']
    else:
        raise Exception("Не вдалося отримати курс валют.")

def main():
    try:
        usd_exchange_rate = get_usd_exchange_rate()
        print(f"Курс долара США: {usd_exchange_rate} UAH")

        converter = CurrencyConverter(usd_exchange_rate)

        amount_in_uah = float(input("Введіть кількість гривень: "))
        amount_in_usd = converter.convert_to_usd(amount_in_uah)

        print(f"{amount_in_uah} UAH дорівнює {amount_in_usd:.2f} USD")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()