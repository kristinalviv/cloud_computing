data "archive_file" "lambda_processing" {
  source_file  = "lambda_processing.py"
  output_path = "${var.app}-${var.event_processing_lambda_name}.zip"
  type        = "zip"
}

data "archive_file" "lambda_generating" {
  source_file  = "lambda_generating.py"
  output_path = "${var.app}-${var.event_generation_lambda_name}.zip"
  type        = "zip"
}

resource "aws_lambda_function" "sqs_processor_lambda" {
  function_name    = "${var.event_processing_lambda_name}"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "handler.lambda_handler"
  runtime          = "python3.10"

  filename         = data.archive_file.lambda_processing.output_path
  source_code_hash = data.archive_file.lambda_processing.output_base64sha256

  timeout          = 30
  memory_size      = 128

}

resource "aws_lambda_function" "sqs_generator_lambda" {
  function_name    = "${var.event_generation_lambda_name}"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "handler.lambda_handler"
  runtime          = "python3.10"

  filename         = data.archive_file.lambda_generating.output_path
  source_code_hash = data.archive_file.lambda_generating.output_base64sha256

  timeout          = 30
  memory_size      = 128

}

resource "aws_cloudwatch_log_group" "lambda_generator_logs" {
    name = "/aws/lambda/${aws_lambda_function.sqs_generator_lambda.function_name}"
    retention_in_days = 5
}

resource "aws_cloudwatch_log_group" "lambda_processing_logs" {
    name = "/aws/lambda/${aws_lambda_function.sqs_processor_lambda.function_name}"
    retention_in_days = 5
}