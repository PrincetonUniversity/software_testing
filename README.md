# Gotcha! How to Write Software Tests to Improve Code Quality

## About

Software testing is the process of verifying and validating that code works as expected. The most granular level is unit testing, where each standalone unit in a code (e.g., function) is exercised to help ensure that it works correctly, even in edge and corner cases. Whether you write unit tests after your code is written or as you go, software tools exist to help make the testing process less manual and more systematic.

This workshop covers some best practices for testing code and gives participants a hands-on introduction to testing frameworks for interpreted (Python) with suggestions for compiled languages (C/C++). Though the emphasis will be on unit testing, other forms of testing such as system tests, integration tests, and regression tests will be discussed.

## Setup

Make sure you can run the Python script `test_circle_area.py` on Adroit or another machine:

```bash
$ ssh <YourNetID>@adroit.princeton.edu  # VPN required if off-campus
$ git clone https://github.com/PrincetonUniversity/software_testing.git
$ cd software_testing/02_unittest
$ module load anaconda3/2022.5
$ python test_circle_area.py
```
<!--
## Attendance

[Link](https://docs.google.com/spreadsheets/d/1IvaQ32-BcRHdQhDz979HX-7U7qjzRDyp/edit#gid=395939115)

## Workshop Survey

Toward the end of the workshop please complete [this survey](http://bit.ly/PUBootcampWinter2021survey).
-->

## Reminders

- If you have not already registered for the live workshop then please [register](https://cglink.me/2gi/r1924494). 
- Wintersession will send participants a survey after the workshop.
- Request an account on [Adroit](https://forms.rc.princeton.edu/registration/?q=adroit) if you wish to use Adroit to run examples.

## Getting Help

If you encounter any difficulties with the material in this guide then please send an email to <a href="mailto:cses@princeton.edu">cses@princeton.edu</a> or attend a <a href="https://researchcomputing.princeton.edu/education/help-sessions">help session</a>.

## Authorship

This guide was created by Jonathan Halverson, William Hasling and members of Princeton Research Computing.
