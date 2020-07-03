import alpaca_trade_api as tradeapi
import config

def getHistory():
    APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
    APCA_API_KEY_ID = config.API_KEY
    APCA_API_SECRET_KEY = config.SECRET_KEY

    api = tradeapi.REST(
        base_url = APCA_API_BASE_URL,
        key_id = APCA_API_KEY_ID,
        secret_key = APCA_API_SECRET_KEY
    )

    limit = 5
    barset = api.get_barset('F', 'day', limit=limit)
    f_bars = barset['F']

    week_open = f_bars[0].o
    week_close = f_bars[-1].c
    percent_change = (week_close - week_open) / week_open * 100
    print('F moved {}% over the last {} days'.format(percent_change, limit))

if __name__ == "__main__":
    getHistory()