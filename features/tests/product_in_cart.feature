# Created by Andrei at 6/11/20
Feature: Verify that after user add 1 product to cart, counter was increased by 1


  Scenario: Open Amazon.com, search for product, add to cart, verify cart items counter increased by 1
    Given Open Amazon page
    When Input Dress into search field
    When Click on search icon
    When Click on product in list
    When Click on Choose the size button
    When Choose size
    When Click on Add to cart button
    Then Cart counter increased by 1