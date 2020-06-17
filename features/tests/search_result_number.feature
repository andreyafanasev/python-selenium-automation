# Created by andrei at 6/16/20
Feature: Search results

  Scenario: Check the number of search result
    Given Open Amazon page
    When Input lego into search field
    And Click on search icon
    Then The number of items is equal to 60