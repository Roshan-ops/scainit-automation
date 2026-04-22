Feature: Signup

  Scenario: User signs up with valid data
    Given the user is on the login page
    When the user navigates to the signup page
    And the user enters valid signup details
    Then the signup should be successful

  Scenario: User signs up with temporary email
    Given the user is on the login page
    When the user navigates to the signup page
    And the user enters a temporary email address
    Then a temporary email error should be displayed
    