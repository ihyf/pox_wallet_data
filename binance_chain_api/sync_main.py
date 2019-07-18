import json
import asyncio
import time
from decimal import Decimal
from binance_chain.constants import TimeInForce, OrderType, OrderSide
from binance_chain.http import AsyncHttpApiClient
from binance_chain.environment import BinanceEnvironment
from binance_chain.messages import NewOrderMsg
from binance_chain.wallet import Wallet

loop = None


class Hyf(object):

    def __init__(self, loop, env, private_key_string, symbol):
        self.loop = loop
        self.env = env
        self.test_net_url = "https://testnet-dex.binance.org/"
        self.main_net_url = "https://dex.binance.org/"
        self.symbol = symbol
        self.private_key_string = private_key_string
        self.wallet = Wallet(private_key=private_key_string, env=self.env)

    async def _create_cli(self):
        cli = await AsyncHttpApiClient.create(loop=self.loop, env=self.env)
        return cli

    async def get_buy_sell_one(self, cli, symbol) -> float:
        """获取买卖单第一个价格"""
        order_book = await cli.get_order_book(symbol=symbol)
        buy_order_list = order_book.get("bids", [])
        sell_order_list = order_book.get("asks", [])
        if len(buy_order_list) == 0 or len(sell_order_list) == 0:
            return 0, 0
        buy_one = buy_order_list[0][0]
        sell_one = sell_order_list[0][0]
        return Decimal(float(buy_one)), Decimal(float(sell_one))

    async def new_order_msg(self, order_type, side, symbol, price, quantity):
        """下订单"""
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

    async def broadcast_transaction(self, cli, order_msg, sync=False):
        res = await cli.broadcast_msg(order_msg, sync)
        return res

    async def start_order(self, total_quantity, quantity):
        """开始刷单"""
        cli = await self._create_cli()
        real_total = 0
        for i in range(0, int(total_quantity/quantity)):
            try:
                start = time.time()
                buy_one, sell_one = await self.get_buy_sell_one(cli=cli, symbol=self.symbol)
                avg = Decimal((buy_one+sell_one)/2).quantize(Decimal('0.000000'))
                print(avg)
                buy_order_msg = await self.new_order_msg(order_type=OrderType.LIMIT, side=OrderSide.BUY, symbol=self.symbol,
                                                   price=avg, quantity=quantity)
                sell_order_msg = await self.new_order_msg(order_type=OrderType.LIMIT, side=OrderSide.SELL, symbol=self.symbol,
                                                    price=avg, quantity=quantity)
                sell_order_order = await self.broadcast_transaction(cli=cli, order_msg=sell_order_msg)
                print(sell_order_order)
                buy_order_order = await self.broadcast_transaction(cli=cli, order_msg=buy_order_msg)
                print(buy_order_order)
                end = time.time()
                print("time :" + str(end-start))
                real_total += quantity
                asyncio.sleep(1)

            except Exception as e:
                print("start_order error:")
                print(e)
                break
        await cli.session.close()
        print("real_total: " + str(real_total))
        return True


if __name__ == "__main__":
    test_env = BinanceEnvironment.get_testnet_env()
    master_env = BinanceEnvironment.get_production_env()
    private_key_str = "c5b07f6a2f2794521a954e519093e98d768f24ca80675d192ff1d90e6fc055c3"
    symbol2 = "ANN-457_BNB"

    main_net_address = "bnb1ewt0w4z4zfnjvmvnqg5fvl35lvp364yk7rhs8l"
    main_net_private_key_str = "a2ef355c3d1c58851f84ef7476239db8939434b6c89ad946a94ebdf438037c68"
    symbol1 = "COS-2E4_BNB"
    loop = asyncio.get_event_loop()
    hyf = Hyf(loop=loop, env=master_env, private_key_string=main_net_private_key_str, symbol=symbol1)
    loop.run_until_complete(hyf.start_order(200, 10))
    loop.close()
