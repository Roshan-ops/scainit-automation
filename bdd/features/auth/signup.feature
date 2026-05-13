Feature: Scainit Signup

  @signup @smoke
  Scenario: Get Started button is disabled by default
    Given the user is on the signup page
    Then the Get Started button should be disabled

  @signup @smoke
  Scenario: Get Started button is enabled after entering valid signup details
    Given the user is on the signup page
    When the user enters valid signup details
    Then the Get Started button should be enabled

  @signup @smoke @regression
  Scenario: User signs up with valid details
    Given the user is on the signup page
    When the user enters valid signup details
    And the user clicks on Get Started
    Then the OTP page should be displayed

  @signup @regression
  Scenario: User cannot signup with temporary email
    Given the user is on the signup page
    When the user enters a temporary email address
    And the user clicks on Get Started
    Then temporary email validation should be displayed
    
  @signup @regression
  Scenario Outline: User cannot signup with invalid password
    Given the user is on the signup page
    When the user enters signup details with password "<password>"
    Then password validation should be displayed
    And the Get Started button should be disabled

    Examples:
      | password   |
      | Test@12    |
      # | test@1234  |

  @signup @regression
  Scenario Outline: User cannot signup with invalid phone number
    Given the user is on the signup page
    When the user enters signup details with phone "<phone>"
    Then phone validation should be displayed
    And the Get Started button should be disabled

    Examples:
      | phone            |
      | 987654321        |
      | 9876543 |
