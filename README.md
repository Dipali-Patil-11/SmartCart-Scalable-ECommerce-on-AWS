# 📌 SmartCart – Scalable E-Commerce Web Application on AWS

## 🚀 Project Overview

SmartCart is a cloud-based scalable e-commerce web application developed using core AWS services. The project demonstrates how modern e-commerce platforms such as Amazon, Flipkart, and Meesho achieve high availability, automatic scaling, and serverless backend processing.

The application allows users to browse products, view product images stored in Amazon S3, and add products to a shopping cart using a serverless REST API. The frontend is hosted on an EC2 instance behind an Application Load Balancer (ALB), while an Auto Scaling Group (ASG) automatically provisions new EC2 instances when demand increases.

## 🎯 Project Objectives
- Build a scalable cloud-based e-commerce application.
- Demonstrate High Availability using Application Load Balancer.
- Automatically scale web servers using Auto Scaling Group.
- Implement serverless backend using AWS Lambda.
- Store product and cart information using DynamoDB.
- Store product images using Amazon S3.
- Monitor infrastructure using Amazon CloudWatch.

## 🏗 Architecture
```text
                    Users
                      │
                      ▼
        Application Load Balancer (ALB)
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      EC2 Instance 1        EC2 Instance 2
              ▲
              │
      Auto Scaling Group
              │
              ▼
      SmartCart Web Application
              │
              ▼
         Amazon API Gateway
              │
              ▼
          AWS Lambda
              │
      ┌───────┴────────┐
      ▼                ▼
 Amazon DynamoDB     Amazon S3
(Product Data)    (Product Images)
```

## ☁ AWS Services Used
| Service | Purpose |
|---------|---------|
| Amazon EC2 | Hosts the SmartCart website |
| Amazon S3 | Stores product images |
| Amazon DynamoDB | Stores product catalog and shopping cart data |
| AWS Lambda | Handles Add-to-Cart requests |
| Amazon API Gateway | Exposes REST API |
| Application Load Balancer | Distributes incoming traffic |
| Auto Scaling Group | Automatically launches additional EC2 instances |
| Launch Template | Defines EC2 configuration |
| Amazon Machine Image (AMI) | Creates identical EC2 instances |
| Amazon CloudWatch | Monitors CPU utilization and triggers Auto Scaling |
| Security Groups | Controls inbound and outbound traffic |

## ✨ Features
- Product catalog display
- Product images loaded from Amazon S3
- Add to Cart functionality using REST API
- Serverless backend processing
- High Availability using ALB
- Automatic EC2 scaling using Auto Scaling Group
- CPU-based scaling through CloudWatch
- Responsive web interface
- Cloud-native architecture

## 📂 Project Workflow
1. User opens SmartCart website.
   ↓
2. Application Load Balancer receives the request.
   ↓
3. ALB forwards the request to an EC2 instance.
   ↓
4. Product images are loaded directly from Amazon S3.
   ↓
5. User clicks Add to Cart.
   ↓
6. API Gateway receives the POST request.
   ↓
7. AWS Lambda processes the request.
   ↓
8. Shopping cart data is stored in Amazon DynamoDB.
   ↓
9. CloudWatch continuously monitors CPU utilization.
   ↓
10. Auto Scaling launches additional EC2 instances during high traffic.
    ↓
11. ALB automatically distributes traffic across all healthy instances.

## 📁 Project Structure
```text
SmartCart-Scalable-ECommerce-on-AWS
│
├── index.html
├── images/
│   ├── laptop.jpg
│   ├── phone.jpg
│   ├── shoes.jpg
│   └── bag.jpg
├── README.md
├── architecture.png
├── screenshots/
│   ├── website.png
│   ├── ec2.png
│   ├── s3.png
│   ├── lambda.png
│   ├── apigateway.png
│   ├── dynamodb.png
│   ├── alb.png
│   ├── autoscaling.png
│   ├── cloudwatch.png
│   └── targetgroup.png
```

## 📊 Project Highlights
- Built a scalable cloud architecture using AWS.
- Implemented serverless backend with Lambda and API Gateway.
- Used DynamoDB for NoSQL data storage.
- Hosted frontend on EC2 with Apache.
- Configured Application Load Balancer for traffic distribution.
- Created Launch Template and AMI for identical EC2 deployment.
- Configured Auto Scaling Group for dynamic infrastructure scaling.
- Monitored application metrics using CloudWatch.
- Demonstrated High Availability and Fault Tolerance.

## 🔮 Future Enhancements
- User authentication using Amazon Cognito
- Payment Gateway integration
- Product search and filtering
- Order history
- Wishlist feature
- Admin Dashboard
- Inventory Management
- Email notifications using Amazon SNS
- Product recommendations using Amazon Personalize

## 🎓 Learning Outcomes
Through this project, I gained practical experience with:
- Designing scalable cloud architectures
- Deploying web applications on AWS
- Implementing Auto Scaling and Load Balancing
- Building serverless REST APIs
- Working with DynamoDB and S3
- Monitoring cloud infrastructure with CloudWatch
- Understanding High Availability and Fault Tolerance

## 👨‍💻 Developed By
**Dipali Patil**  
*B.Tech – Artificial Intelligence & Machine Learning (AIML)*  
AWS Cloud & Python Enthusiast
