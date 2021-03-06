#! python
# encoding=utf-8

import argparse

parser = argparse.ArgumentParser(description="Calculates the value of a monthly investment in shares at maturity")
parser.add_argument("monthly_investment", metavar="monthly_investment", type=str, help="The amount in £'s invested each month")
parser.add_argument("--option-price", nargs='?', default=263.76, help="The option price in pence")
parser.add_argument("--sale-price", nargs='?', default=263.76, help="The sale price that will be achieved on maturity in pence")
parser.add_argument("--months-to-maturity", nargs='?', default=36, help="How many months you will be investing for")

args = parser.parse_args()

monthly_investment = float(args.monthly_investment)
option_price = float(args.option_price)
sale_price = float(args.sale_price)
months_to_maturity = float(args.months_to_maturity)
total_investment = monthly_investment * months_to_maturity
n_shares = (total_investment / (option_price / 100))
total_share_price_at_maturity = n_shares * (sale_price/100)
total_profit = total_share_price_at_maturity - total_investment

print u"For an investment of £{investment} per month for {months} months".format(investment=monthly_investment, months=months_to_maturity)
print u"You would have invested £%0.2f" % total_investment
print u"At an option price of %0.2fp" % option_price
print u"You would get %0.2f shares" % n_shares
print u"Which at a sale price of %0.2fp" % sale_price
print u"Would be worth £%0.2f at maturity" % total_share_price_at_maturity
print u"A profit of £%0.2f" % total_profit
print u"Or a percentage gain of %0.2f%%" % (total_profit*100/total_investment)