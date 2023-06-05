resource "aws_sqs_queue" "queue" {
  name = "queue"
  delay_seconds = 0
  max_message_size          = 2048
  message_retention_seconds = 86400
  depends_on = [
  aws_lambda_function.sqs_processor_lambda,
  aws_lambda_function.sqs_generator_lambda
  ]
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:*:*:$queue",
      "Condition": {
        "ArnEquals": { "aws:SourceArn": "${aws_s3_bucket.processeddatafromsqs1terraform2.arn}" }
      }
    }
  ]
}
EOF
}

resource "aws_lambda_event_source_mapping" "event_source_mapping" {
  event_source_arn = aws_sqs_queue.queue.arn
  enabled          = true
  function_name    = aws_lambda_function.sqs_processor_lambda.arn
  batch_size       = 1
  depends_on = [
  aws_lambda_function.sqs_processor_lambda
  ]
}

