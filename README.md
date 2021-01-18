# Election Audit

*Prepared for Seth and Tom - 2021 JAN 17*

## Overview of Election Audit

### Purpose

The main purpose of this audit is to analyse the election results and submit the data findings to the election commission. This audit will inlcude the following data:

* Total number of votes cast
* Voter turnout and percentage of votes from each county, including the county with the highest turnout
* A complete list of candidates who received votes
* Total number of votes and the percentage of votes each candidate received and won, respectively
* The winner of the election (based on popular vote)

### Resources

* Data source: election_results.csv
* Software: Python 3.8.5, Visual Studio Code, 1.52.1

## Election Audit Results

* The total number of votes casted in this congressional election were **369,711**
* The number of votes and percentage of total votes for each county in the precinct is as follows:

     ![County_Breakdown](Resources/County_Breakdown.png)
* As confirmed in the above image, Denver was the county with the largest number of votes
* The following depicts a breakdown of the number of votes and precentage of total votes each candidate receieved:

     ![Candidate Breakdown](Resources/Candidate_Breakdown.png)
* **Diana DeGette** was the winner of this election, and the following image presents the total number of votes won as well as the overall percentage of votes recieved, thus securing the popular vote

     ![Winner](Resources/Winner.png)

## Election Audit Summary

As presented in this README file, it is clear that the script was able to carry out all functions and data analysis requests, and as such, the script can be easily modified as necessary for use in any election:
* For use in a federal election, the functions containing **county** can be swapped for **state** *(please see image below*
     ![State](Resources/State.png)
* 
