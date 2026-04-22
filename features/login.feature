Feature: Login

  Scenario: User logs in with valid credentials
    Given the user is on the login page
    When the user enters valid email and password
    Then the user should be redirected to the dashboard


  Scenario: User logs in with invalid credentials
    Given the user is on the login page  
    When the user enters invalid email and password  
    Then an error message should be displayed 