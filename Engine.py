
import OrderBook

if __name__ == '__main__':
    market = OrderBook.make_random_market()
    OrderBook.do_all_matches(market)
