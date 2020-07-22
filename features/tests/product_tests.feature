# Created by andrei at 7/21/20
Feature: Tests for product page


  Scenario: Size tooltip is shown upon hovering over Add to cart button
    Given Open Amazon product B074TBCSC8 page
    When Hover over Add to cart button
    Then Verify size selection tooltip is shown