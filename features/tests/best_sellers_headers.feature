# Created by andrei at 7/3/20
Feature: Verify user can click on top links on Bestsellers page, and they are open
  Clicks on Best Sellers link on the top menu
  Clicks on each top link and verify that new page opens


  Scenario: Click on Best Sellers link on the top menu, click on each top link and verify that new page opens
    Given Open Amazon page
    When Click on Best sellers link
    Then Verify user can click on top links on Bestsellers page, and they are open