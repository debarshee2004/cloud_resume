<div align="center">
  <img src="./assets/images/azure.png" alt="logo" width="600" />
</div>

# Cloud Resume Challenge using Azure.

[The Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/) is an initiative designed to help individuals showcase their skills in cloud computing and enhance their resumes by building a comprehensive cloud-based project. Created by Forrest Brazeal, a cloud advocate and educator, the challenge encourages participants to create a modern, dynamic resume using various cloud services and technologies.

The primary goal of the Cloud Resume Challenge is to provide a practical and hands-on approach for individuals looking to demonstrate their proficiency in cloud computing platforms such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP). Participants are tasked with building a personal resume website hosted on the cloud, implementing features like serverless functions, databases, and other cloud-native services.

Key components of the Cloud Resume Challenge often include deploying a static website, incorporating serverless functions for dynamic content, integrating a database for data storage, and optimizing the solution for performance, security, and cost-effectiveness. The challenge not only emphasizes technical skills but also encourages participants to document their journey and share their code on platforms like GitHub, fostering a collaborative and learning-focused community.

# Architecture of the Project.

[![](https://app.eraser.io/workspace/CVaxS2XMBTPulDj2i09k/preview?elements=-QcFS67VkoJ3RrK3yyZuTQ&type=embed)](https://app.eraser.io/workspace/CVaxS2XMBTPulDj2i09k?elements=-QcFS67VkoJ3RrK3yyZuTQ)

*Image shows the diagram of the architecture of the system*

This is beginner friendly project which teaches you about some Azure services and how to use git via a tool like Github to create a Continuous Integration and Continuous Deployment pipelines with the help of Github Actions.

## The Frontend

This frontend consists of a basic static website made of HTML, CSS and JavaScript. Now with that we are adding the small logic of showing the visitor counter, the `main.js` file of the project consists of the visitor counter update function.

```js
window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const getVisitCount = () => {
    let count = 30;
    fetch(productionApiUrl).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called function API.");
        count =  response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });
    return count;
}
```

Finally it was hosted using *Static Website Hosting* feature of Azure Blob Storage. 

## The Backend

This is the main part of the project. Here we are creating a Azure Serverless Function as an API to update and fetch data from Cosmos DB of Azure.

### Azure Functions

Azure Functions is a serverless compute service provided by Microsoft Azure, enabling developers to build and deploy event-driven, scalable applications without managing infrastructure. It allows users to write code in various languages, responding to events such as HTTP requests, database changes, or timer triggers. With automatic scaling, developers pay only for the resources consumed during execution, promoting cost efficiency. Azure Functions simplifies application development by abstracting infrastructure concerns, facilitating the creation of lightweight, modular functions that seamlessly integrate with other Azure services, fostering rapid development and deployment of microservices and serverless applications.

This Azure Function, written in Python, connects to Cosmos DB, retrieves user view counter data based on the provided user_id parameter, and responds with the user's view count. It uses the azure.cosmos library to interact with Cosmos DB, making it a concise and efficient way to fetch data from the database.

```py
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Azure Cosmos DB connection settings
    endpoint = 'your_cosmos_db_endpoint'
    key = 'your_cosmos_db_key'
    database_name = 'your_database_name'
    container_name = 'your_container_name'

    # Create a Cosmos DB client
    client = CosmosClient(endpoint, key)

    # Get a reference to the database and container
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    # Query Cosmos DB to fetch user view counter data (modify the query accordingly)
    query = 'SELECT * FROM c WHERE c.userId = "exampleUserId"'
    items = container.query_items(query, enable_cross_partition_query=True)

    # Process the fetched data (modify this part based on your needs)
    user_views = [item['views'] for item in items]

    # Return the fetched data as an HTTP response (modify this part based on your needs)
    return func.HttpResponse(f"User views: {user_views}", status_code=200)

```

### Cosmos DB

Azure Cosmos DB is a globally distributed, multi-model database service by Microsoft Azure, designed for seamless scalability and low-latency access to data. It supports various data models, including document, key-value, graph, and column-family, catering to diverse application needs. With automatic and instant scalability, it ensures high availability and fault tolerance across global regions. Cosmos DB provides comprehensive indexing and querying capabilities, enabling developers to efficiently retrieve and process data. It also offers multi-region writes, robust security features, and integration with popular APIs and SDKs, making it a versatile choice for building responsive and globally distributed applications.

Here's a sample JSON representation for a Cosmos DB Core SQL document based on the described Azure Function fetching user view counter data:

```json
{
  "id": "<DocumentId>",
  "user_id": "<UserId>",
  "view_counter": 100
}
```

Explanation:
- `"id"`: A unique identifier for the document.
- `"user_id"`: Identifier for the user.
- `"view_counter"`: The counter representing the number of views for the user. This value can be adjusted based on the actual view count for each user in your application.