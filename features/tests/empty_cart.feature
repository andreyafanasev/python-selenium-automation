# Created by Andrei at 6/7/20
Feature: User clicks on the cart icon and Shopping Cart is empty

  Scenario: Open amazon.com, click on the cart icon and verify that Your Shopping Cart is empty.
    Given Open Amazon page
    When Click on cart icon
    Then User sees that cart is empty