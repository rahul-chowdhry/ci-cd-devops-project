
# PROJECT REPORT

# Automated CI/CD Pipeline Using GitHub Actions, Python Flask, Pytest and Docker

## Submitted By
Rahul Kumar

## 1. Introduction

DevOps is a software development approach that combines development and operations practices to improve software delivery.

Continuous Integration (CI) is the process of automatically checking and testing code changes whenever developers push code to a shared repository.

This project demonstrates an automated CI pipeline using GitHub Actions, Python Flask, Git and Pytest.

## 2. Project Objective

The main objectives are:

1. Implement Source Code Management using Git and GitHub.
2. Develop a web application using Python Flask.
3. Create automated test cases using Pytest.
4. Configure GitHub Actions for automatic workflow execution.
5. Validate application changes automatically.
6. Understand the CI/CD workflow.

## 3. Technologies

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Flask | Web application framework |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | CI workflow automation |

## 4. System Architecture

Developer
   |
   v
Git Repository
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   v
Install Dependencies
   |
   v
Build Preparation
   |
   v
Pytest Automated Testing
   |
   v
Success / Failure

## 5. Application Modules

### Home Page
Displays the welcome message.

### Health API
Checks whether the application is running.

### About API
Returns project details and version information.

### E-commerce Order API
Accepts product name, quantity and unit price.

Calculates total order amount and validates input.

## 6. Testing

Automated tests were written using Pytest.

Tests cover:

1. Home page response.
2. Health endpoint.
3. About endpoint.
4. Invalid route.
5. Order calculation.
6. Invalid quantity.
7. Negative price.
8. Empty product name.
9. Invalid JSON.

### Local Testing Result

9 tests passed according to the provided terminal output.

## 7. CI Pipeline Implementation

GitHub Actions workflow was configured in:

.github/workflows/ci-cd.yml

The workflow runs automatically when code is pushed to the main branch or a pull request is created.

The pipeline performs:

- Repository checkout.
- Python setup.
- Dependency installation.
- Application build preparation.
- Automated test execution.
- Success or failure reporting.

## 8. Practical Demonstration

A new E-commerce Order API feature was implemented.

Example:

Product: Keyboard

Quantity: 2

Unit Price: ₹1,500

Total: ₹3,000

The API returned a successful response.

The updated source code and test files were committed and pushed to GitHub.

Commit: 9299e46

## 9. Results

The Flask application was tested locally.

The automated test suite reported 9 passed.

The latest GitHub push triggered the automated workflow.

The GitHub Actions workflow was reported successful.

## 10. Limitations

- No production database is configured.
- Orders are calculated but not saved.
- No real payment gateway is integrated.
- Docker execution was skipped.
- Automatic deployment is not configured.

The implemented and verified scope is Continuous Integration.

## 11. Future Enhancements

- Docker containerization.
- Automated deployment to a hosting platform.
- Database integration.
- User authentication.
- Payment processing.
- Application monitoring.

## 12. Conclusion

This project demonstrates a practical Continuous Integration pipeline.

It automates code validation and testing using GitHub Actions and Pytest.

It helps reduce manual work, improve code quality and identify software errors early.

The project provides a foundation for implementing a complete CI/CD deployment pipeline.
