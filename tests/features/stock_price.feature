Feature: Stock Price Retrieval
  As a user
  I want to get stock prices
  So that I can track market data

  Scenario: Successfully get AAPL stock price
    Given I have a stock symbol "AAPL"
    When I request the stock price
    Then I should receive a price value of 203.19

  Scenario: Successfully get C stock price
    Given I have a stock symbol "C"
    When I request the stock price
    Then I should receive a price value of 63.05

  Scenario: Handle invalid stock symbol
    Given I have a stock symbol "INVALID"
    When I request the stock price
    Then I should receive a price value of 0.0

  Scenario: Handle empty stock symbol
    Given I have an empty stock symbol
    When I request the stock price
    Then I should receive a price value of 0.0