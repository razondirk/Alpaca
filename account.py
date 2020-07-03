import alpaca_trade_api as tradeapi
import config

def getStatus(paper):
    if paper:
        APCA_API_KEY_ID = config.PAPER_API_KEY
        APCA_API_SECRET_KEY = config.PAPER_SECRET_KEY
        APCA_API_BASE_URL = config.PAPER_BASE_URL
    else:
        APCA_API_KEY_ID = config.LIVE_API_KEY
        APCA_API_SECRET_KEY = config.LIVE_SECRET_KEY
        APCA_API_BASE_URL = config.LIVE_BASE_URL

    api = tradeapi.REST(
        base_url = APCA_API_BASE_URL,
        key_id = APCA_API_KEY_ID,
        secret_key = APCA_API_SECRET_KEY
    )

    # Get our account information.
    account = api.get_account()
    #api.list_positions()
    print("{} | {} | {} | {} | {} || {}".format(account.id, account.account_number, account.status, account.currency, account.cash, account.portfolio_value))
    #sma = api.alpha_vantage.techindicators(symbol='AAPL', interval='weekly', time_period='10', series_type='close')
    #rsi = api.alpha_vantage.techindicators(techindicator='RSI', symbol='AAPL', interval='weekly', time_period='14', series_type='close')
    #print(sma)

if __name__ == "__main__":
    getStatus()