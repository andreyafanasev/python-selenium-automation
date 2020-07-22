# Created by andrei at 7/22/20
Feature: Opens  product B074TBCSC8 page, hovers over New Arrivals, then verifies that the user sees the deals.
  # Enter feature description here

  Scenario: Verifies that the user sees the deals then hover over New Arrivals on product B074TBCSC8 page.
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals link
    Then Verify that the deals are shown