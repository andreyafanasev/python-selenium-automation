# Created by Andrei Afanasev at 6/16/20
#  Homework lesson 4, 06.14.2020

Feature: Verify Amazon BestSellers page has 5 links: Best sellers, New releases, Movers & Shakers,
  Most vished for and Gift ideas


  Scenario: Verify Amazon BestSellers page has 5 links
    Given Open Amazon page
    When Click on Best sellers link
    Then Verify Amazon BestSellers page has 5 links