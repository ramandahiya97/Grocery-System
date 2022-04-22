*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***

#<<ADMIN LOGIN>>
Test Case 1
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  admin
    Input Text  //input[@name='pwd']  12345
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Select show products from Admin Module>>
Test Case 2
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  admin
    Input Text  //input[@name='pwd']  12345
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Press Keys  //a[@name='show_all_products']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Delete Product from Admin Module>>

Test Case 3
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  admin
    Input Text  //input[@name='pwd']  12345
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Press Keys  //a[@name='delete_products']  [return]
    Input Text  //input[@id='product_id']  200012
    Press Keys  //button[@id='delete_prod']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Sign up>>
Test Case 4
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Press Keys  //label[normalize-space()='Sigup now']  [return]
    Input Text  //input[@placeholder='Enter your name']  raman
    Input Text  //input[@placeholder='Enter Gender']  male
    Input Text  //input[@placeholder='Enter your email']  raman@gmail.com
    Input Text  //input[@placeholder='Enter phone number']  123456789
    Input Text  //input[@name='password']  1234
    Press Keys  //form[@action='/signup']//input[@value='Submit']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Customer Login>>
Test Case 5
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  raman@gmail.com
    Input Text  //input[@name='pwd']  1234
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<About us page from Customer module>>
Test Case 6
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  raman@gmail.com
    Input Text  //input[@name='pwd']  1234
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Press Keys  //a[@href='/about']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Product page from Customer Module>>
Test Case 7
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  raman@gmail.com
    Input Text  //input[@name='pwd']  1234
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Press Keys  //a[normalize-space()='Product']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Register Complaint from Customer Module>>
Test Case 8
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  raman@gmail.com
    Input Text  //input[@name='pwd']  1234
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Press Keys  //a[normalize-space()='CONTACT']  [return]
    Input Text  //input[@id='id']  1
    Input Text  //input[@id='name']  Raman Dahiya
    Input Text  //input[@id='pname']  123456789
    Input Text  //input[@id='date']  04202022
    Input Text  //textarea[@id='subject']  Order Delayed
    Press Keys  //input[@value='Submit']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Forgot Password>>
Test Case 9
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    press keys  //a[normalize-space()='Forgot password?']  [return]
    Input Text  //input[@placeholder='Enter your username']  raman
    Input text  //input[@placeholder='Enter your email']  raman@gmail.com
    Input text  //input[@placeholder='Enter phone number']  123456789
    press keys  //input[@value='Submit']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Check Order history from Customer Module>>
Test Case 10
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  raman@gmail.com
    Input Text  //input[@name='pwd']  1234
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Press Keys  //a[normalize-space()='Product']  [return]
    Press Keys  //a[normalize-space()='Order History']  [return]
    Set Browser Implicit Wait  05
    Close Browser

#<<Logout>>
Test Case 11
    Open Browser  http://127.0.0.1:1000/  chrome
    Maximize Browser Window
    Input Text  //input[@placeholder='Enter your username']  raman@gmail.com
    Input Text  //input[@name='pwd']  1234
    Press Keys  //form[@action='/verify']//input[@value='Submit']  [return]
    Press Keys  //a[normalize-space()='LOGOUT']  [return]
    Set Browser Implicit Wait  05
    Close Browser
*** Variables ***
*** Keywords ***
