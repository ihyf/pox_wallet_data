import time
from decimal import Decimal

from binance_chain.constants import TimeInForce, OrderType, OrderSide, KlineInterval
from binance_chain.http import HttpApiClient
from binance_chain.wallet import Wallet
from binance_chain.environment import BinanceEnvironment
from binance_chain.messages import NewOrderMsg, LimitOrderBuyMsg, LimitOrderSellMsg, UnFreezeMsg, CancelOrderMsg


class Hyf(object):
    def __init__(self, env, private_key_string, symbol):
        self.test_net_url = "https://testnet-dex.binance.org/"
        self.main_net_url = "https://dex.binance.org/"
        self.symbol = symbol
        self.env = env
        self.private_key_string = private_key_string
        self.wallet = self._create_wallet_by_private_key()
        self.cli = HttpApiClient(env=testnet_env, api_url=self.test_net_url)

    def create_bnb_wallet(self) -> Wallet:
        """generate Mnemonic --> wallet"""
        w = Wallet.create_random_wallet(env=self.env)
        return w

    def _create_wallet_by_private_key(self) -> Wallet:
        w = Wallet(self.private_key_string, env=self.env)
        return w

    def broadcast_transaction(self, order_msg, sync=True):
        res = self.cli.broadcast_msg(order_msg, sync)
        return res

    def new_order_msg(self, order_type, side, symbol, price, quantity):
        """"""
        new_order_msg = NewOrderMsg(
            wallet=self.wallet,
            symbol=symbol,
            time_in_force=TimeInForce.GOOD_TILL_EXPIRE,
            order_type=order_type,
            side=side,
            price=price,
            quantity=Decimal(float(quantity))
        )
        return new_order_msg

    def cancel_order(self, order_id):
        cancel_order_msg = CancelOrderMsg(
            wallet=self.wallet,
            order_id=order_id,
            symbol=self.symbol,
        )
        res = self.broadcast_transaction(cancel_order_msg, sync=True)


    def limit_order_msg_buy(self, symbol, price, quantity):
        """Limit Order Buy"""
        limit_order_msg = LimitOrderBuyMsg(
            wallet=self.wallet,
            symbol=symbol,
            price=price,
            quantity=Decimal(float(quantity))
        )
        return limit_order_msg

    def limit_order_msg_sell(self, symbol, price, quantity):
        """Limit Order Sell"""
        limit_order_msg = LimitOrderSellMsg(
            wallet=self.wallet,
            symbol=symbol,
            price=price,
            quantity=Decimal(float(quantity))
        )
        return limit_order_msg

    def get_banlance(self, addr):
        balance = self.cli.get_account(addr)
        print(balance)
        return balance

    def get_order_book(self):
        order_book = self.cli.get_order_book(self.symbol)
        print(order_book)
        return order_book

    def unfreeze_tokens(self, base_symbol, amount):
        """解冻tokens"""
        unfreeze_msg = UnFreezeMsg(
            wallet=self.wallet,
            symbol=base_symbol,
            amount=Decimal(float(amount))
        )
        res = self.cli.broadcast_msg(unfreeze_msg, sync=True)
        print(res)
        return res

    def get_buy_sell_one(self, symbol) -> float:
        """获取买卖单第一个价格"""
        order_book = self.cli.get_order_book(symbol)
        buy_order_list = order_book.get("bids", [])
        sell_order_list = order_book.get("asks", [])
        if len(buy_order_list) == 0 or len(sell_order_list) == 0:
            return 0, 0
        buy_one = buy_order_list[0][0]
        sell_one = sell_order_list[0][0]
        return Decimal(float(buy_one)), Decimal(float(sell_one))

    def get_order_open(self, addr):
        open_orders = self.cli.get_open_orders(addr)
        print("open_orders")
        print(open_orders)
        return open_orders

    def get_order_close(self, addr):
        closed_orders = self.cli.get_closed_orders(addr)
        print("closed_orders")
        print(closed_orders)
        return closed_orders

    def start_order(self, total_quantity, quantity):
        """开始刷单"""

        for i in range(0, int(total_quantity/quantity)):
            try:
                buy_one, sell_one = self.get_buy_sell_one(self.symbol)
                avg = Decimal((buy_one+sell_one)/2).quantize(Decimal('0.000'))
                print(avg)
                buy_order_msg = self.new_order_msg(order_type=OrderType.LIMIT, side=OrderSide.BUY, symbol=self.symbol,
                                                   price=avg, quantity=quantity)
                sell_order_msg = self.new_order_msg(order_type=OrderType.LIMIT, side=OrderSide.SELL, symbol=self.symbol,
                                                    price=avg, quantity=quantity)

                buy_order_order = self.broadcast_transaction(order_msg=buy_order_msg)
                print(buy_order_order)
                sell_order_order = self.broadcast_transaction(order_msg=sell_order_msg)
                print(sell_order_order)

            except Exception as e:
                print("start_order error:")
                print(e)
                break
        return True


if __name__ == "__main__":
    testnet_env = BinanceEnvironment.get_testnet_env()
    master_env = BinanceEnvironment.get_production_env()

    address = "tbnb1cz5ukltlqnrh7t8sy47qkcmxdu5ks0nq5nflmm"

    private_key_str = "c5b07f6a2f2794521a954e519093e98d768f24ca80675d192ff1d90e6fc055c3"

    # 获取token列表
    # token_list = client.get_tokens()
    # print(token_list)

    symbol1 = "BZNT-464_BNB"
    symbol2 = "ANN-457_BNB"

    hyf = Hyf(env=testnet_env, private_key_string=private_key_str, symbol=symbol2)
    # hyf.start_order(total_quantity=1, quantity=1)
    # # hyf.get_order_book()
    hyf.get_banlance(address)
    # hyf.get_order_open(address)
    # hyf.get_order_close(address)


