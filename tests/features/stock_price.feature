Feature: Stock Price Retrieval
  As a user
  I want to get stock prices
  So that I can track market data

  Scenario: Successfully get stock price
    Given I have a valid stock symbol "AAPL"
    When I request the stock price
    Then I should receive a valid price value

  Scenario: Handle invalid stock symbol
    Given I have an invalid stock symbol "INVALID"
    When I request the stock price
    Then I should receive no price value

  Scenario: Handle empty stock symbol
    Given I have an empty stock symbol ""
    When I request the stock price
    Then I should receive no price value 