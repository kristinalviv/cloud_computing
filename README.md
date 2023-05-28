# cloud_computing

## Terraform intro

Terraform is a Infrastructure as code (IaC) tool, which allow you to manage infrastructure with configuration files 
rather than through a graphical user interface. 

Project shows how to deploy and delete EC2 instance in AWS.
Prerequites:
```
Terraform installed
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KE are set as environment variables (to authenticate the Terraform AWS provider)
```

## DB task

Project intent to show how to trigger AWS lambda to insert records from SQS into MySQL DB.

Repo contains code per AWS lambda, which is triggered by SQS to read event and insert it into MySQL DB.

Also, CloudWatch logs were added per lambda and SQS run.

## DB backup/restore

Project shows how to backup and restore DB in AWS.

Repo contains code to create several record in AWS RDS (MySQL)

After DB snapshot need to be created from UI.

Repo also have code per some of previous inserted records updation.

Then DB need to bee restored from previously cerated snapshot.

Latest code in lambda shows thet DB contain all records as they were before update.


## Haunting CVEs
  
Project intent to show how to find CVEs in real docker image. Trivy is used as a scanner.

Trivy is an open source tool focused on detecting vulnerabilities in OS-level packages,IaC misconfigurations, SBOM discovery, Cloud scanning, Kubernetes security risks, and more.

As an example 'ghcr.io/mlflow/mlflow:v2.3.0' image is scanned by [trivy](https://trivy.dev) [repo](https://github.com/aquasecurity/trivy). Only fixed HIGH and CRITICAL vulnerabilities were intended to be found.

To not persist the installation binaries on our system, a Docker image is used
```
docker run --rm -v ~/.trivy:/root/.cache/ aquasec/trivy:0.40.0 image ghcr.io/mlflow/mlflow:v2.3.0 --severity HIGH,CRITICAL --ignore-unfixed
```
