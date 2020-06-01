# Created by andrei at 6/1/20
Feature: Logged out user sees Sign in page when clicking Orders


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Orders icon
    Then Logged out user sees Sign in page