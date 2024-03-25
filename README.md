# majority_report_code
[![Update Majority Report Live json](https://github.com/rustymyers/majority_report_code/actions/workflows/python-app.yml/badge.svg)](https://github.com/rustymyers/majority_report_code/actions/workflows/python-app.yml)

Uses YouTube RSS feed to get MR Live episodes to derive Fun Half links. Fun Half links are stored in json for each day, updated at 12:35 PM EST with a GitHub Action. 

The GitHub Action runs the scripts and writes changes to the json back to the master branch. This provides an automatically updated json for MR Live youtube links at the staic link:

[https://raw.githubusercontent.com/rustymyers/majority_report_code/main/fun_half.json](https://raw.githubusercontent.com/rustymyers/majority_report_code/main/fun_half.json)
