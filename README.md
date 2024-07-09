# Report for Assignment 1 resit

## Project chosen

Name: opsdroid

URL: https://github.com/DAViduull01/SEP-Assignment1-resit.git

Number of lines of code and the tool used to count it: 25.594 , lizard

Programming language: Python

## Coverage measurement with existing tool

The tool executed was Coverage.py and it was used in the project’s directory with the following command: ‘coverage run -m unittest discover’ .



## Coverage improvement

### Individual tests

<Function 1> ‘_get_messages’

This commit is for both functions: https://github.com/opsdroid/opsdroid/compare/main...DAViduull01:SEP-Assignment1-resit:main

Old coverage (coverage html):


New coverage (coverage html):


Before the modifications the coverage was 0% because there were no tests to cover this function. After the modifications, which include simulating async iteration, testing with no messages, valid messages, and bot messages, and verifying the correct sleep interval, the coverage result went up to 100%.


<Function 2> ‘parse_message’

This commit is for both functions: https://github.com/opsdroid/opsdroid/compare/main...DAViduull01:SEP-Assignment1-resit:main

Old coverage (coverage html):


New coverage (coverage html):


Before the modifications, the coverage was 0% because the only two tests were not covering the function properly. After the modifications the coverage went up to 100%. This improvement is due to the addition of tests that cover edge cases such as handling empty messages and logging errors for incomplete JSON inputs. These tests ensure that more branches of the code are executed and potential error scenarios are handled correctly, thus increasing the overall coverage.












### Overall

Old coverage results:
















New coverage results:

<img width="1512" alt="Screenshot 2024-07-09 at 20 25 02" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/ff227d7e-bd81-4971-8a5c-a84136703028">
<img width="1512" alt="Screenshot 2024-07-09 at 20 25 16" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/f9cf34ad-c96d-42ea-b860-128b93d8ac10">

