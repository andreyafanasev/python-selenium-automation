# Created by andrei at 7/2/20
Feature: Amazon main page popups


  Scenario: Sign in popus appears and then disappears
    Given Open Amazon page
    Then Verify Amazon popup is present and clickable
    When Sign in popup disappears
    Then Verify Amazon popup is not clickable