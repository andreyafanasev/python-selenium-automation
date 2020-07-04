# Created by Andrei at 7/2/20
Feature: Window handling


  Scenario: Company's website is open in a new tab
    Given Open a company's Yelp page
    When Click on a website link
    And Switch to a new window
    Then The HUNGER PANG website is open
    And The user can close the new window and go to original one