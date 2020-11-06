s3_bucket=sls-tmp-artifacts
stack_name ?= slackatto-prod
aws_region ?= us-east-2
sam_template_base=sam
sam_template=$(sam_template_base).yml
sam_output=$(sam_template_base)-new.yml


build:
	juni build

deploy:
	sam package \
	    --s3-bucket $(s3_bucket) \
	    --template-file $(sam_template) \
	    --output-template-file ./dist/$(sam_output) \
	    --profile $(profile) \
	    --region ${aws_region}

	sam deploy \
	    --template-file ./dist/$(sam_output) \
	    --stack-name $(stack_name) \
	    --capabilities CAPABILITY_IAM \
	    --profile $(profile) \
	    --region ${aws_region}
