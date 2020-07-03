import alpaca_trade_api as tradeapi
import config

def run(paper):
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

    F = api.polygon.historic_agg_v2('F', 1, 'minute', "2020-06-05", "2020-05-08").df
    print(F)

if __name__ == "__main__":
    getStatus()