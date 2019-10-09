#!/usr/bin/python

import argparse

def find_max_profit(prices):

    buy_in_price = prices[0]


    max_profit = -prices[0]

    for i in prices:
      # print(i)
      if i - buy_in_price > max_profit and prices.index(i) != 0:
        max_profit = i - buy_in_price

      if i < buy_in_price:
        buy_in_price = i

    return max_profit






  # bip = []
  # mpsf = []

  # for i in range(0,len(prices)-1):
  #   if prices[i+1] > prices[i]:
  #     bip.append(prices[i])
  #   else:
  #     mpsf.append(prices[i])
  #
  # max_profit =  mpsf[-1] - bip[0]
  # return max_profit



  # create foloop to run through each index in the array
  # save the lowest number in the array to a variable
  # find the largest number to sell at afterwards

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))