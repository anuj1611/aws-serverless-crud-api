# 🚀 Serverless CRUD Application using AWS Lambda, API Gateway & DynamoDB

This project demonstrates how to build a **fully serverless, scalable, and pay-per-use CRUD REST API** using **AWS Lambda**, **Amazon API Gateway**, and **Amazon DynamoDB**.  
It supports Create, Read, Update, and Delete operations, all triggered through API endpoints.

---

## 🧩 Tech Stack

- **AWS Lambda** – Serverless compute for executing backend logic.
- **Amazon API Gateway** – To expose RESTful API endpoints.
- **Amazon DynamoDB** – NoSQL database for storing data.
- **AWS IAM** – To manage secure permissions for Lambda.
- **CloudFormation / Terraform (Optional)** – For Infrastructure as Code (IaC).
- **Amazon CloudWatch** – For logging and monitoring.
- **Amazon SNS (Optional)** – For alert notifications.

---

## 🗂️ Project Architecture Overview

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

## ⚙️ Step-by-Step Workflow

Below is the **exact workflow** we followed to build this project from scratch:

---

### **1️⃣ Create the DynamoDB Table**

- Go to **AWS Console → DynamoDB → Create Table**
- Table name: `ItemsTable`
- Partition key: `id` (String)
- Keep other settings as default (On-Demand capacity)
- Click **Create Table**

✅ **Result:** DynamoDB table ready to store items.

---

### **2️⃣ Create IAM Role for Lambda**

- Go to **IAM → Roles → Create Role**
- Trusted entity type: **AWS Service**
- Use case: **Lambda**
- Attach policies:
  - `AmazonDynamoDBFullAccess`
  - `CloudWatchFullAccess`
- Name the role: `LambdaDynamoDBRole`
- Click **Create Role**

✅ **Result:** A secure role with DynamoDB & CloudWatch permissions created.

---

### **3️⃣ Create Lambda Functions**

We created **4 Lambda functions**, one for each CRUD operation.

| Function Name          | Purpose                        | Operation  |
|------------------------|--------------------------------|-------------|
| `CreateItemFunction`   | Adds a new item to DynamoDB     | POST `/items` |
| `GetItemsFunction`     | Retrieves all items             | GET `/items` |
| `UpdateItemFunction`   | Updates an existing item        | PUT `/items/{id}` |
| `DeleteItemFunction`   | Deletes an item by ID           | DELETE `/items/{id}` |

Each Lambda uses **Python (boto3)** to interact with DynamoDB.

✅ **Result:** All Lambda functions tested successfully inside AWS Lambda Console.

---

### **4️⃣ Connect API Gateway to Lambda**

- Go to **API Gateway → Create API → REST API**
- Create a new **Resource** named `/items`
- Under `/items`, create the following **Methods**:
  - `POST` → Integrate with `CreateItemFunction`
  - `GET` → Integrate with `GetItemsFunction`
- Create another resource `/items/{id}`
  - `PUT` → Integrate with `UpdateItemFunction`
  - `DELETE` → Integrate with `DeleteItemFunction`
- Enable **Lambda Proxy Integration** for all.

✅ **Result:** API Gateway connected with all Lambda functions.

---

### **5️⃣ Deploy the API**

- Go to **Actions → Deploy API**
- Create a new stage named **prod**
- Copy the **Invoke URL**, e.g.:

  ```
  https://<api-id>.execute-api.<region>.amazonaws.com/prod
  ```

✅ **Result:** Public API endpoints are now live and callable from Postman.

---

### **6️⃣ Test Using Postman**

Use the following endpoints:

| Method | Endpoint | Description | Example Body |
|--------|-----------|--------------|---------------|
| **POST** | `/items` | Create an item | `{ "name": "Test Item", "description": "Created via Postman" }` |
| **GET** | `/items` | Read all items | — |
| **PUT** | `/items/{id}` | Update an item | `{ "name": "Updated Item", "description": "Modified" }` |
| **DELETE** | `/items/{id}` | Delete an item | — |

✅ **Result:** All CRUD operations returned correct responses and updated DynamoDB successfully.

---

### **7️⃣ Add Monitoring & Alerts**

- **CloudWatch Logs:** Automatically receives Lambda logs.
- **CloudWatch Alarms:** Send alerts for failures or high latency.
- **Amazon SNS (Optional):** For email notifications.

✅ **Result:** Monitoring and alerting integrated successfully.

---

### **8️⃣ (Optional) Infrastructure as Code**

You can automate all resources using:
- **AWS SAM Template**
- **Terraform**
- **CloudFormation Stack**

✅ **Result:** Reproducible, automated setup.

---

## 🧱 Architecture Diagram

Below is the final simplified architecture diagram:

```
Client (Postman / Browser)
    ↓
API Gateway (prod)
    ↓
Lambda (Create / Read / Update / Delete)
    ↓
DynamoDB (ItemsTable)
    ↓
CloudWatch Logs & SNS Alerts
```

---

## 📊 Project Highlights

✅ 100% Serverless (no servers or EC2 required)  
✅ Pay-per-use pricing  
✅ Scalable CRUD API  
✅ Clean IAM-based security  
✅ Tested with Postman  
✅ Observable with CloudWatch  

---

## 🧪 Example Response

**POST /items**
```json
{
  "message": "Item created successfully!",
  "item": {
    "id": "1009b968-52f2-46a3-bc5a-276b0112ed89",
    "name": "Postman Test Item",
    "description": "Created via Postman"
  }
}
```

---

## 🧠 Learnings & Key Takeaways

- Gained hands-on experience with **AWS Lambda and API Gateway integration**  
- Learned to manage **IAM roles & permissions** effectively  
- Understood **DynamoDB CRUD operations using boto3**  
- Practiced **API testing with Postman**  
- Created a **scalable, production-ready serverless system**

---

## 📁 Repository Structure

```
aws-serverless-crud-api/
│
├── create_item.py
├── get_items.py
├── update_item.py
├── delete_item.py
├── README.md
├── architecture.png
└── diagram.mmd
```

---

## 🏁 Conclusion

You’ve successfully built a **complete Serverless REST API** using AWS managed services — secure, scalable, and cost-efficient.  
This project demonstrates the power of **Serverless Architecture** for real-world backend systems.

---

## 📚 Author

**Anuj Dhiraj Bhagat**  
*Cloud & Software Developer*  
📧 anuj@example.com  
💻 GitHub: [@anujbhagat](https://github.com/anujbhagat)

---

⭐ **If you found this project helpful, give it a star on GitHub!**
