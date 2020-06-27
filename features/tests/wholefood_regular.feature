# Created by andrei at 6/27/20
Feature: Every product on the page has a text "Regular"
  # Enter feature description here

  Scenario: Verify every product on the page has a text "Regular"
    Given Open Amazon wholefood page
    Then Verify every product on the page has a text "Regular" and a product name