import requests



class FinancialDataRetrievalSystem:
    def __init__(self, currency_api_key, share_api_key):
        # Initializing attributes
        self.currency_api_key = currency_api_key
        self.share_api_key = share_api_key

    def get_currency_exchange_rate(self, base_currency, target_currency):
        # Retrieving the current exchange rate between two currencies
        url = f'https://v6.exchangerate-api.com/v6/{currency_api_key}/latest/{base_currency}'
        response = requests.get(url)
        data = response.json()
        rate = data["conversion_rates"][target_currency]
        return rate

    def get_company_share_price(self, company_symbol):
        # Retrieving the current price of shares for a given company
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company_symbol}&interval=1min&apikey={share_api_key}'
        response = requests.get(url)
        data = response.json()
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        share_price = float(data['Time Series (1min)'][last_refreshed]['4. close'])
        return share_price




    def get_currency_conversion(self, amount, base_currency, target_currency):
        # Convert the given amount from one currency to another
        exchange_rate = self.get_currency_exchange_rate(base_currency, target_currency)
        conversion = amount * exchange_rate
        return conversion


# Example usage of the Financial Data Retrieval System
if __name__ == "__main__":
    # Configuring API keys
    currency_api_key = '0d65b5ce1edbe28c7e936b85'
    share_api_key = 'MMFUYOSBSKMLRI2G'
    # Initializing the FinancialDataRetrievalSystem object
    financial_system = FinancialDataRetrievalSystem(currency_api_key, share_api_key)
    operation = int(input('1.Convert currency\n2.Get share price of company\nEnter number for operation: '))
    if operation == 1:
        user_currency = input("Convert currency from: ")
        target_currency = input("to : ")
        currency_amount = float(input("with amount: "))
        converting = financial_system.get_currency_conversion(currency_amount, user_currency, target_currency)
        print(f"{currency_amount}{user_currency} = {converting:.2f}{target_currency}")
    elif operation == 2:
        company_symbol = input("Enter the company's symbol you want to check share price: ")
        share_price = financial_system.get_company_share_price(company_symbol)
        print(f"Share price of {company_symbol} is: {share_price:.2f}")
