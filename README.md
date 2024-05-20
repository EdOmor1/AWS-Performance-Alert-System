# AWS-Performance-Alert-System

## Overview
This project creates an alert system that notifies you of significant changes in campaign performance metrics using AWS services.

## Architecture
![Architecture Diagram](diagrams/architecture_diagram.png)

## AWS Services Used
- Amazon CloudWatch
- AWS SNS
- AWS Lambda

## Features
- Monitors campaign performance metrics.
- Sends notifications via SNS when significant changes are detected.

## Prerequisites
- AWS account
- API access to advertising platforms

## Setup

### Step 1: Deploy Infrastructure
1. Deploy the CloudFormation stack using `infrastructure/cloudformation_template.yaml`.

### Step 2: Configure Lambda Functions
1. Update `src/lambda_function.py` with your API credentials and endpoints.
2. Deploy the Lambda functions using the AWS Lambda console or AWS CLI.

## Usage
1. The Lambda function runs periodically to fetch performance data.
2. If significant changes are detected, an alert is sent via SNS.
