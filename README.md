# slackatto

Small repository used to explore the slack API

# slackatto

Small repository used to explore the slack API
This is a sample repository used to integrate and explore the slack events API. The main purpose of this experient is to build a user directory capable of being in sync with changes to user in a slack workspace. If a user is added to the workspace, our directory should have the ability to show that user in our client. When a user edits his/her profile, that change needs to be captured by our server and the change needs to be displayed in our interface...

## Server Architecture

The server portion of this project has a single responsibility: to keep track of the users in a slack workspace. The serverless API will listen to the events sent over by the slack API and based on the type of event it will manage users. The API Gateway will receive a request from slack and it will route it to a lambda function. In the serverless domain, if there are no requests, there's no infrastructure running. Behind the scenes AWS manages the infrastructure, for practical purposes, no requests, means your "function" is not actively working. This has several advantages including scalability out of the box. Ifrastructure as code is easy to adopt and the costs of running a serverless API make this technology a very viable approach.

The persistance store selected for this project is the no-sql db dynamo. The main reason to select this database is the fact that 1. it plays well with the serverless mentality. 2. It integrates seamlessly with a lambda function 3. In order to keep track of the users in a workspace, we can store the json representation received by slack as an entry in the table. No additional fields or overhead requried. Last but not least, the scalable capabilities of dynamo are incredible.

Last but most definitely not least! This project uses two projects dear to my heart: juniper and minik. Juniper is an open source project I built and now maintain and it is used to build lambda functions. You can see where and how it is used in the `Makefile`. Minik is a micro web framework I developed and also maintain. This project came to life as a way to build a no batteries included web framework. A minimalist mentality was used when developing that project and right now it is used in production by the EAB.

The server portion of this project can be used as a small blueprint on how to build a serverless project from scratch.

## Resources

https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/
https://docs.aws.amazon.com/AmazonS3/latest/dev/HostingWebsiteOnS3Setup.html#step3-add-bucket-policy-make-content-public
