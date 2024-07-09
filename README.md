# Report for Assignment 1 resit

## Project chosen

Name: opsdroid

URL: https://github.com/DAViduull01/SEP-Assignment1-resit.git

Number of lines of code and the tool used to count it: 25.594 , lizard

Programming language: Python

## Coverage measurement with existing tool

The tool executed was Coverage.py and it was used in the project’s directory with the following command: ‘coverage run -m unittest discover’ .
<img width="1512" alt="Screenshot 2024-07-09 at 21 25 26" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/b5427681-fa6e-4c82-ad84-cab24fb1be60">
<img width="1512" alt="Screenshot 2024-07-09 at 21 25 37" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/5cad4cbe-81b5-4b30-9200-cf6baec8a042">



## Coverage improvement

### Individual tests

<Function 1> ‘_get_messages’

This commit is for both functions: https://github.com/opsdroid/opsdroid/compare/main...DAViduull01:SEP-Assignment1-resit:main

Old coverage (coverage html):
<img width="1267" alt="Screenshot 2024-07-09 at 21 27 04" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/79dc7f8d-c906-4b62-8fd2-6964f772723d">


New coverage (coverage html):
<img width="854" alt="Screenshot 2024-07-09 at 19 35 32" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/9732b260-2390-46c8-9699-71e83ce24023">


Before the modifications the coverage was 0% because there were no tests to cover this function. After the modifications, which include simulating async iteration, testing with no messages, valid messages, and bot messages, and verifying the correct sleep interval, the coverage result went up to 100%.


<Function 2> ‘parse_message’

This commit is for both functions: https://github.com/opsdroid/opsdroid/compare/main...DAViduull01:SEP-Assignment1-resit:main

Old coverage (coverage html):
<img width="1268" alt="Screenshot 2024-07-09 at 21 27 22" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/e65c1178-634e-4b18-a15b-52da5537a007">


New coverage (coverage html):
<img width="854" alt="Screenshot 2024-07-09 at 15 10 47" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/63c8650a-7537-4de6-bf1b-c9f953a8379a">


Before the modifications, the coverage was 0% because the only two tests were not covering the function properly. After the modifications the coverage went up to 100%. This improvement is due to the addition of tests that cover edge cases such as handling empty messages and logging errors for incomplete JSON inputs. These tests ensure that more branches of the code are executed and potential error scenarios are handled correctly, thus increasing the overall coverage.












### Overall

Old coverage results:

<img width="1512" alt="Screenshot 2024-07-09 at 21 25 26" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/b32349b6-e669-48ca-9045-8497c80de9f2">
<img width="1512" alt="Screenshot 2024-07-09 at 21 25 37" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/23b4b072-6fbd-4240-861e-eadeb3509e91">
















New coverage results:

<img width="1512" alt="Screenshot 2024-07-09 at 20 25 02" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/ff227d7e-bd81-4971-8a5c-a84136703028">
<img width="1512" alt="Screenshot 2024-07-09 at 20 25 16" src="https://github.com/DAViduull01/SEP-Assignment1-resit/assets/122388645/f9cf34ad-c96d-42ea-b860-128b93d8ac10">

