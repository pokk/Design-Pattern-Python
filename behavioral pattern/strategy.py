""" Created by wu.jieyi on 2016/03/14. """
from abc import ABCMeta, abstractmethod


class PayWay(metaclass=ABCMeta):
    """
    Strategy interface.
    """

    @abstractmethod
    def pay(self, amount):
        pass


# PayPal strategy.
class PayPal(PayWay):
    def __init__(self, pp_id, pwd):
        self._pp_id = pp_id
        self._pp_pwd = pwd

    def pay(self, amount):
        print('pay %d by paypal...' % amount)


# Credit Card strategy.
class CreditCard(PayWay):
    def __init__(self, owner_name, card_number, expire_year, expire_month):
        self._cc_name = owner_name
        self._cc_num = card_number
        self._cc_expire_year = expire_year
        self._cc_expire_month = expire_month

    def pay(self, amount):
        print('pay %d by credit card...' % amount)


# Cash strategy.
class Cash(PayWay):
    def __init__(self, currency):
        self._c_currency = currency

    def pay(self, amount):
        print('pay %d by %s cash....' % (amount, self._c_currency))


class Cart:
    def __init__(self):
        self.total = 0
        self._shopping_list = {}

    def add_item(self, item_name, item_price):
        self._shopping_list.update({str(item_name): item_price})

    def remove_item(self, item_name):
        self._shopping_list.pop(str(item_name))

    # Change the strategy here.
    def pay_amount(self, payway):
        self._cal_total()
        payway.pay(self.total)

    def _cal_total(self):
        self.total = 0
        for k, v in self._shopping_list.items():
            self.total += v


def main():
    cart = Cart()
    cart.add_item('Sea Food', 23)
    cart.add_item('Book', 40)
    cart.add_item('Sun Glass', 99)

    cart.pay_amount(PayPal('NewId', 'NewPwd'))
    cart.pay_amount(Cash('US dollar'))
    cart.pay_amount(CreditCard('MyName', '11111111', 3000, 10))


if __name__ == '__main__':
    main()
