*** Settings ***
Library        RequestsLibrary

Library        Collections


*** Test Cases ***
####     Test_Register       ####
test_Login_Incomplete_parameter
    ${payload}    Create Dictionary
    Create Session    login    http://127.0.0.1:8000
    ${r}=    Get Request    login    /user_login/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    Incomplete parameter!
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10010)
    Should Be Equal    ${sta}    ${status}

test_login_User_name_does_not_exist!
    ${payload}    Create Dictionary    username=eee    password=a111
    Create Session    login    http://127.0.0.1:8000
    ${r}=    Get Request    login    /user_login/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    User name does not exist!
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10011)
    Should Be Equal    ${sta}    ${status}

test_login_Password_Error
    ${payload}    Create Dictionary    username=aaa    password=a111
    Create Session    login    http://127.0.0.1:8000
    ${r}=    Get Request    login    /user_login/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    Password Error!
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10012)
    Should Be Equal    ${sta}    ${status}


####     Test_Register       ####
#这里忽略了格式错误，
#项目中在form中定义了输入格式，
#但目前还不清楚对于form的测试。
test_Register_Incomplete_parameter
    ${payload}    Create Dictionary
    Create Session    register    http://127.0.0.1:8000
    ${r}=    Get Request    register    /user_register/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    Incomplete parameter!
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10010)
    Should Be Equal    ${sta}    ${status}

test_Register_Username_already_exists
    ${payload}    Create Dictionary    username=aaa    pwd=a123    pwd_again=a123
    Create Session    register    http://127.0.0.1:8000
    ${r}=    Get Request    register    /user_register/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    User name already exists!
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10011)
    Should Be Equal    ${sta}    ${status}

test_Register_Passwords_do_not_match
    ${payload}    Create Dictionary    username=eee    pwd=e123    pwd_again=e321
    Create Session    register    http://127.0.0.1:8000
    ${r}=    Get Request    register    /user_register/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    Passwords do not match
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10012)
    Should Be Equal    ${sta}    ${status}

test_Register_Success
    ${payload}    Create Dictionary    username=eee    pwd=e123    pwd_again=e123
    Create Session    register    http://127.0.0.1:8000
    ${r}=    Get Request    register    /user_register/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    Register Success
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10013)
    Should Be Equal    ${sta}    ${status}





