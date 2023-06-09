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
  
Project intent to show how to find CVEs in real docker image. Trivy and Grype are used as a scanners.

**Trivy** is an open source tool focused on detecting vulnerabilities in OS-level packages,IaC misconfigurations, SBOM discovery, Cloud scanning, Kubernetes security risks, and more.

As an example 'ghcr.io/mlflow/mlflow:v2.3.0' image is scanned by [trivy](https://trivy.dev) [repo](https://github.com/aquasecurity/trivy). Only fixed HIGH and CRITICAL vulnerabilities were intended to be found.

To not persist the installation binaries on our system, a Docker image is used
```
docker run --rm -v ~/.trivy:/root/.cache/ aquasec/trivy:0.40.0 image ghcr.io/mlflow/mlflow:v2.3.0 --severity HIGH,CRITICAL --ignore-unfixed
```

**Grype** is a vulnerability scanner for container images and filesystems. 

As an example 'ghcr.io/mlflow/mlflow:v2.3.0' image is scanned by [grype](https://github.com/anchore/grype). Only fixed HIGH and CRITICAL vulnerabilities were intended to be found.

To not persist the installation binaries on our system, a Docker image is used
```
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock anchore/grype docker:ghcr.io/mlflow/mlflow:v2.3.0  --only-fixed
```

_This latest version contain bug (--only-fixed --fail-on High are not working). More detailed info [here](https://github.com/anchore/grype/issues/1094). Hence v0.54.0 was used, code below_


```
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock anchore/grype:v0.54.0 docker:ghcr.io/mlflow/mlflow:v2.3.0  --only-fixed --fail-on High
```

Trivy and Grype can be seen as equivalent tools, which are the best in class to identify and map installed software to CVEs. But even both results are pretty similar there are some discrepancies:

- trivy contain title with link with fix recommendations, while Grype not.

- Grype has additional vulnerabilities, which are missed in trivy. (certifi, libsystemd0, libudev1 and requests)

## Policies check

Project shows how to check your project compliance with standard policies. [checkov](https://github.com/bridgecrewio/checkov)

To start check, run following command:
```
PATH_TO_TF=/Users/khrystyna/Desktop/Ucu/Hometasks/Cloud_Computing/src/terraform
docker run --volume $PATH_TO_TF:/tf bridgecrew/checkov:2.3.199 --quiet --compact --directory /tf
```

Output will be an info regarding total passed checks, failed checks and skipped checks.

Two of them were fixed:

- Added metadata_options per ec2 instance and configured to securely access instance metadata.

```
metadata_options {
       http_endpoint = "disabled"
  }
```

- Enabled detailed monitoring for Amazon Elastic Compute Cloud (EC2) instance. (monitoring = true)

After fixing, only two failed checks left. 

## Pricing

Project give description of target price estimation for 1.000, 100.000 and 10.000.000 HTTP function invocation per month in AWS.

## Terraform configuration for the project

Project describes in terraform configuration of all the used in previous project cloud components: Lambda, S3 buckets, SQS, CloudWatch Log group, IAM policy creation.
Prerequites:
```
Terraform installed
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KE are set as environment variables (to authenticate the Terraform AWS provider)
```

Following commands can be used per infrastructure plan, creation and delete:
```
terraform init  
terraform plan
terraform apply

terraform destroy 
```
