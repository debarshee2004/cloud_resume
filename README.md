<div align="center">
  <img src="./assets/images/azure.png" alt="logo" width="600" />
</div>

# Cloud Resume Challenge using Azure.

Welcome to the Azure Cloud Resume Challenge! This project is designed to help you showcase your skills in Microsoft Azure through a hands-on, practical approach. Follow the steps below to create an impressive resume website hosted on Azure:

## Overview

This challenge involves building a personal resume website using Azure services. The primary goal is to demonstrate your proficiency in deploying, configuring, and managing Azure resources. The challenge is divided into tasks, each focusing on different Azure services.

## Tasks

1. **Static Website**: Create a static resume website using HTML/CSS or a static site generator.

2. **Azure Storage Account**: Host your website files in an Azure Storage Account.

3. **Azure CDN**: Implement Azure CDN to deliver content globally, ensuring low-latency access.

4. **Azure Functions**: Develop a serverless function to handle a contact form on your website.

5. **Azure Cosmos DB**: Store form submissions in Azure Cosmos DB, showcasing NoSQL database skills.

6. **Azure DevOps**: Set up a CI/CD pipeline to automate the deployment process.

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

## Docker Integration in Azure Cloud Resume Challenge

In the Azure Cloud Resume Challenge, Docker can be employed to enhance the development, deployment, and scalability aspects of your resume website. Here's how you can leverage Docker within the challenge:

### 1. **Containerized Development Environment**

Use Docker containers to create a consistent development environment. Define a `Dockerfile` specifying the necessary dependencies and configurations for your website. This ensures that all team members, as well as the Azure environment, have the same environment setup, mitigating the "it works on my machine" issue.

### 2. **Multi-Stage Docker Builds**

Implement multi-stage Docker builds to optimize the image size. Use a multi-stage build to separate the build environment from the runtime environment. This reduces the final Docker image size, leading to faster deployment times and efficient use of resources.

### 3. **Containerized Website Deployment**

Package your resume website into a Docker container. This containerized approach ensures that your application, along with all its dependencies, is encapsulated. Deploy this container to Azure App Service, Azure Kubernetes Service (AKS), or any other Azure service supporting container deployments.

### 4. **Scalability and Reproducibility**

Docker facilitates scalability by allowing easy replication of containers. Leverage container orchestration services like Azure Kubernetes Service (AKS) to scale your website based on demand. Docker's containerization ensures reproducibility, making it straightforward to deploy consistent instances across multiple environments.

### 5. **Integration with Azure DevOps**

Integrate Docker into your Azure DevOps CI/CD pipeline. Create Docker images during the CI process, and push them to a container registry in Azure. This ensures a streamlined deployment process, with versioned Docker images readily available for deployment.

### 6. **Docker Compose for Local Testing**

Utilize Docker Compose for local testing of your website along with associated services like Azure Functions and Cosmos DB. This helps ensure that your application functions correctly in a containerized environment before deployment to Azure.

An example `Dockerfile` in the project.

```Dockerfile
ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY . .

EXPOSE 7071

CMD func start
```

By incorporating Docker into the Azure Cloud Resume Challenge, you enhance the portability, consistency, and efficiency of your application's development and deployment processes.

## Getting Started

1. Fork this repository to your GitHub account.

2. Clone the forked repository to your local machine.

3. Follow the instructions in each task folder to complete the challenges.

4. Commit your changes and push them to your GitHub repository.

5. Deploy your resume website to Azure.

## Resources

- [Azure Documentation](https://docs.microsoft.com/en-us/azure/)
- [Azure DevOps Documentation](https://docs.microsoft.com/en-us/azure/devops/)
- [GitHub Pages](https://pages.github.com/)

## License

This project is licensed under the [MIT License](LICENSE).

## Conclusion

Feel free to explore, modify, and enhance the code to suit your needs. If you encounter any issues or have suggestions, please open an issue or create a pull request.