# Serverless AWS Translate

Serverless computing is a method of providing backend services on an as-used basis. A serverless provider allows users to write and deploy code without the hassle of worrying about the underlying infrastructure. A company that gets backend services from a serverless vendor is charged based on their computation and do not have to reserve and pay for a fixed amount of bandwidth or number of servers, as the service is auto-scaling. Note that despite the name serverless, physical servers are still used but developers do not need to be aware of them.


<img src="test.png" />

## How can use it? 
 - Check your AWS credentials. (tip:  ~/.aws/credentials)
 - pip install chalice (if you haven't)
 - chalice deploy (if you want to use on local you can replace deploy to local)
 - postman > post[body] > {"url":"https://example.com"}
 
