# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Amazon Search functionality

Scenario: User can search for a product
    Given Open Amazon page
    When Search for Dress
    Then Product results for Dress are shown
#    And First result contains Dress


Scenario: User can select Books department
    Given Open Amazon page
    When Select stripbooks department
    And Search for Faust
    Then Books department is selected


Scenario: User can select Gift card department
    Given Open Amazon page
    When Select gift-cards department
    And Search for Gift
    Then Gift Cards department is selected