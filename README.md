# Serverless CRUD Application using AWS Lambda, API Gateway & DynamoDB

This project demonstrates how to build a **fully serverless, scalable, and pay-per-use CRUD REST API** using **AWS Lambda**, **Amazon API Gateway**, and **Amazon DynamoDB**.  
It supports Create, Read, Update, and Delete operations, all triggered through API endpoints.

---

## Tech Stack

- **AWS Lambda** – Serverless compute for executing backend logic.
- **Amazon API Gateway** – To expose RESTful API endpoints.
- **Amazon DynamoDB** – NoSQL database for storing data.
- **AWS IAM** – To manage secure permissions for Lambda.
- **Amazon CloudWatch** – For logging and monitoring.
- **Amazon SNS** – For alert notifications.

---

## Project Architecture Overview

### High-Level Flow:
```
Client (Postman / Browser)
   ↓
API Gateway (REST Endpoints)
   ↓
AWS Lambda (CRUD Functions)
   ↓
DynamoDB (ItemsTable)
   ↓
CloudWatch (Logs & Metrics)
```
---
<img width="1536" height="1024" alt="AWS CRUD API high level arcitecture diagram" src="https://github.com/user-attachments/assets/746f3881-2e52-4edf-acbb-b595b12bb7bc" />


---
<img width="1718" height="688" alt="AWS CRUD API Detailed arcitecture diagram" src="https://github.com/user-attachments/assets/a9049c03-4fd3-4272-9f56-c13b9b3f2cb7" />

---


## Step-by-Step Workflow

Below is the **exact workflow** I followed to build this project from scratch:

---

### **1️) Create the DynamoDB Table**

- Go to **AWS Console → DynamoDB → Create Table**
- Table name: `ItemsTable`
- Partition key: `id` (String)
- Keep other settings as default (On-Demand capacity)
- Click **Create Table**

---
<img width="1919" height="976" alt="Screenshot 2025-10-18 114328" src="https://github.com/user-attachments/assets/7a5a0ae4-4624-4624-8406-a06e5fdc80a6" />

---

<img width="1919" height="971" alt="Screenshot 2025-10-18 114457" src="https://github.com/user-attachments/assets/092e88ca-5cfa-4b49-b45b-c598a79e7ecc" />


---
**Result:-** DynamoDB table ready to store items.

---

### **2️) Create IAM Role for Lambda**

- Go to **IAM → Roles → Create Role**
- Trusted entity type: **AWS Service**
- Use case: **Lambda**
- Attach policies:
  - `AmazonDynamoDBFullAccess`
  - `CloudWatchFullAccess`
- Name the role: `LambdaDynamoDBRole`
- Click **Create Role**

---
<img width="1919" height="979" alt="Screenshot 2025-10-18 122441" src="https://github.com/user-attachments/assets/6fc0a59c-b601-4a77-9ea1-3f8c8c19e997" />

---
<img width="1919" height="972" alt="Screenshot 2025-10-18 123033" src="https://github.com/user-attachments/assets/f8eb56da-e90f-43a7-9099-d524c0159713" />

---


**Result:-** A secure role with DynamoDB & CloudWatch permissions created.

---

### **3️) Create Lambda Functions**

We created **4 Lambda functions**, one for each CRUD operation.

| Function Name          | Purpose                        | Operation  |
|------------------------|--------------------------------|-------------|
| `CreateItemFunction`   | Adds a new item to DynamoDB     | POST `/items` |
| `GetItemsFunction`     | Retrieves all items             | GET `/items` |
| `UpdateItemFunction`   | Updates an existing item        | PUT `/items/{id}` |
| `DeleteItemFunction`   | Deletes an item by ID           | DELETE `/items/{id}` |

Each Lambda uses **Python (boto3)** to interact with DynamoDB.

---
<img width="1919" height="969" alt="Screenshot 2025-10-18 123907" src="https://github.com/user-attachments/assets/38bcc3c5-6534-42d4-a52a-70c281473723" />

---

<img width="1919" height="977" alt="Screenshot 2025-10-18 124523" src="https://github.com/user-attachments/assets/da6d9f8f-bfbd-4560-b5ce-72396ffa9dfa" />

---
<img width="1919" height="969" alt="Screenshot 2025-10-18 133123" src="https://github.com/user-attachments/assets/cb8b0bf4-1e8c-4c13-85d8-e490b7a9b5bd" />

---
<img width="1919" height="978" alt="Screenshot 2025-10-18 133804" src="https://github.com/user-attachments/assets/70d018ec-0175-4546-a23e-3a01aae54e5b" />

---
<img width="1919" height="976" alt="Screenshot 2025-10-18 133949" src="https://github.com/user-attachments/assets/0b70c21a-b5c6-4857-a350-8c1bc6432cf6" />

---




**Result:-** All Lambda functions tested successfully inside AWS Lambda Console.

---

### **4️) Connect API Gateway to Lambda**

- Go to **API Gateway → Create API → REST API**
- Create a new **Resource** named `/items`
- Under `/items`, create the following **Methods**:
  - `POST` → Integrate with `CreateItemFunction`
  - `GET` → Integrate with `GetItemsFunction`
- Create another resource `/items/{id}`
  - `PUT` → Integrate with `UpdateItemFunction`
  - `DELETE` → Integrate with `DeleteItemFunction`
- Enable **Lambda Proxy Integration** for all.

---
<img width="1919" height="977" alt="Screenshot 2025-10-18 135748" src="https://github.com/user-attachments/assets/c0e24a5c-b7b7-4b70-9f6e-ddb720810d1c" />

---
<img width="1919" height="973" alt="Screenshot 2025-10-18 140759" src="https://github.com/user-attachments/assets/bd021e9d-f03b-4530-8c07-8b219cb1d451" />

---
<img width="1919" height="972" alt="Screenshot 2025-10-18 140851" src="https://github.com/user-attachments/assets/6e721401-da41-485e-ba38-8f9dd11e6561" />

---
<img width="1919" height="977" alt="Screenshot 2025-10-18 141118" src="https://github.com/user-attachments/assets/ca6d2eed-54e8-4619-87ed-43da4ea732a5" />

---
<img width="1919" height="960" alt="Screenshot 2025-10-18 142222" src="https://github.com/user-attachments/assets/4de07061-493a-45f3-9eff-03720ed41464" />

---
<img width="1919" height="978" alt="Screenshot 2025-10-18 142339" src="https://github.com/user-attachments/assets/d906b2e9-af71-4fd4-91e8-49c3f2afa7e3" />

---
<img width="1919" height="974" alt="Screenshot 2025-10-18 142549" src="https://github.com/user-attachments/assets/639ad5d0-d4d5-4b86-b34a-2d659c30c24f" />

---


**Result:** API Gateway connected with all Lambda functions.



---

### **5️) Deploy the API**

- Go to **Actions → Deploy API**
- Create a new stage named **prod**
- Copy the **Invoke URL**, e.g.:

  ```
  https://<api-id>.execute-api.<region>.amazonaws.com/prod
  ```
  ---
  <img width="1919" height="959" alt="Screenshot 2025-10-18 142659" src="https://github.com/user-attachments/assets/acb0ae97-5cb8-4654-86c6-fae5d226a016" />
  
  ---


**Result:** Public API endpoints are now live and callable from Postman.

---

### **6️) Test Using Postman**

Use the following endpoints:

| Method | Endpoint | Description | Example Body |
|--------|-----------|--------------|---------------|
| **POST** | `/items` | Create an item | `{ "name": "Test Item", "description": "Created via Postman" }` |
| **GET** | `/items` | Read all items | — |
| **PUT** | `/items/{id}` | Update an item | `{ "name": "Updated Item", "description": "Modified" }` |
| **DELETE** | `/items/{id}` | Delete an item | — |


---
<img width="1439" height="1014" alt="Screenshot 2025-10-18 170917" src="https://github.com/user-attachments/assets/d246ffe9-9eb1-408d-8288-274de511aadc" />

---
<img width="1443" height="971" alt="Screenshot 2025-10-18 170932" src="https://github.com/user-attachments/assets/9b5f9702-a553-4b39-9357-de95871b32df" />

---
<img width="1447" height="963" alt="Screenshot 2025-10-18 170942" src="https://github.com/user-attachments/assets/11e44971-d427-40b2-8536-7b0533cd0d4e" />

---
<img width="1441" height="968" alt="Screenshot 2025-10-18 170949" src="https://github.com/user-attachments/assets/414cf88e-1499-4f03-af89-55d78a3a2b47" />

---




**Result:** All CRUD operations returned correct responses and updated DynamoDB successfully.

---

## Step 7: Add Monitoring & Alerts using CloudWatch and SNS

Monitoring and alerting are crucial for production-grade systems. Below are the exact steps I followed to enable logging, monitoring, and alert notifications for my Lambda functions.


### PART 1 — Enable and View **CloudWatch Logs** for Lambda

Every Lambda automatically sends logs to **CloudWatch**, but let’s confirm and check them.

#### Steps:

1. Go to **AWS Console → Lambda → your function (e.g., CreateItemFunction)**  
2. Scroll down to **Monitor → View logs in CloudWatch**  
3. You’ll see a log group like:  
   ```
   /aws/lambda/CreateItemFunction
   ```  
4. Inside this log group, you can open individual **Log Streams** to view:
   - Start and end time of Lambda invocation  
   - Any `print()` or `console.log()` outputs  
   - Error messages if Lambda failed

---
<img width="1919" height="974" alt="Screenshot 2025-11-01 232449" src="https://github.com/user-attachments/assets/8affd3d3-b307-456e-b286-46d7db83c284" />

---
<img width="1919" height="976" alt="Screenshot 2025-11-01 232602" src="https://github.com/user-attachments/assets/e33fee8c-dbb5-40af-99ea-48ec390fbe55" />

---
<img width="1919" height="849" alt="Screenshot 2025-11-01 233303" src="https://github.com/user-attachments/assets/d00fa7c8-0012-4b42-8f95-0bf394298224" />

---



**Result:**  
Lambda is already logging to CloudWatch automatically.  
Now let’s turn those logs into **alerts**.

### PART 2 — Create a CloudWatch Alarm + SNS Email Alert

This will send me an email when Lambda fails (e.g., due to an exception or timeout).


#### **Create an SNS Topic**

1. Go to **AWS Console → SNS → Topics → Create Topic**
2. Choose **Standard** type
3. Name it something like:
   ```
   LambdaErrorAlerts
   ```
4. Click **Create topic**

---
<img width="1919" height="852" alt="Screenshot 2025-11-01 233807" src="https://github.com/user-attachments/assets/8f139ac1-3234-4d4b-a6c8-d887dd385748" />

---
<img width="1919" height="901" alt="Screenshot 2025-11-01 233827" src="https://github.com/user-attachments/assets/756cb549-ea74-41ae-b980-3e9f69f81001" />

---


#### **Subscribe to the Topic**

1. After creating the topic → Click on it → **Create Subscription**
2. Protocol → `Email`
3. Endpoint → Enter your email address (the one you want alerts on)
4. Check your inbox and click **Confirm subscription**

Once confirmed, your status will show as **Confirmed** in the SNS dashboard.

---
<img width="1919" height="969" alt="Screenshot 2025-11-01 233845" src="https://github.com/user-attachments/assets/fa84201a-d03b-4649-8521-825341555b7f" />

---
<img width="1919" height="967" alt="Screenshot 2025-11-01 234116" src="https://github.com/user-attachments/assets/5052549b-e746-4e8d-bf01-fffd6818afe6" />

---

#### ** Create a CloudWatch Alarm for Lambda**

1. Go to **AWS Console → CloudWatch → Alarms → All Alarms → Create alarm**
2. Choose **Select metric**
3. Choose:
   ```
   Lambda Metrics → By Function Name → <YourFunctionName> → Errors
   ```
4. Click **Select metric**
5. Under **Conditions**, set:
   - Threshold type → Static  
   - Whenever `Errors` is **≥ 1** for **1 datapoint**
6. Under **Actions → Alarm state trigger → In Alarm**, select:
   - **Send a notification to → LambdaErrorAlerts**
7. Give it a name:
   ```
   LambdaErrorAlarm-CreateItemFunction
   ```
8. Click **Create Alarm**

We can repeat this for your other functions if you wish (Get, Update, Delete).

---
<img width="1919" height="973" alt="Screenshot 2025-11-01 234251" src="https://github.com/user-attachments/assets/b76c3493-a172-46c5-943b-9b1fe0b6d30b" />

---
<img width="1919" height="976" alt="Screenshot 2025-11-02 000302" src="https://github.com/user-attachments/assets/a5b067fc-7a18-4e62-8438-3a558d44f43c" />

---
<img width="1919" height="979" alt="Screenshot 2025-11-02 000309" src="https://github.com/user-attachments/assets/f08ebec7-c5eb-4546-b704-a7f0f4b7a54e" />

---
<img width="1919" height="978" alt="Screenshot 2025-11-02 001116" src="https://github.com/user-attachments/assets/2408e96a-dbbd-41e7-910c-955aba0174b8" />

---
<img width="1919" height="979" alt="Screenshot 2025-11-02 001736" src="https://github.com/user-attachments/assets/c9c9152c-1877-4f36-81c7-a7b595302835" />

---
<img width="1919" height="972" alt="Screenshot 2025-11-02 002010" src="https://github.com/user-attachments/assets/6cd18368-2234-41e1-8286-99e859209509" />

---


---

**Final Result:**  
The system now automatically sends **email alerts** whenever any Lambda function fails.

---


## Project Highlights

- 100% Serverless (no servers or EC2 required)  
- Pay-per-use pricing  
- Scalable CRUD API  
- Clean IAM-based security  
- Tested with Postman  
- Observable with CloudWatch  


---

## Learnings & Key Takeaways

- Gained hands-on experience with **AWS Lambda and API Gateway integration**  
- Learned to manage **IAM roles & permissions** effectively  
- Understood **DynamoDB CRUD operations using boto3**  
- Practiced **API testing with Postman**  
- Created a **scalable, production-ready serverless system**


---

⭐ **If you found this project helpful, give it a star!**
