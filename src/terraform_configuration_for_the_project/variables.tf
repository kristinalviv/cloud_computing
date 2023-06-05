variable "region" {
    default = "us-east-1"
    description = "AWS Region to deploy to terraform"
}

variable "app" {
    default = "cloud_computing"
    description = "app prefix used for all resources in this example"
}

variable "event_generation_lambda_name" {
    description = "Name for lambda function"
    default = "sqs_generator_lambda"
}

variable "event_processing_lambda_name" {
    description = "Name for lambda function"
    default = "sqs_processor_lambda"
}