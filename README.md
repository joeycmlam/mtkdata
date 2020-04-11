# Market Data

This is a simple example package. You can use
[Github-flavored Markdown](https://github.com/joeycmlam/mktdata/)
to write your content.

Name: mktdata

Build Command: docker build -t mysys.mktdata:0.2 .

Start Command: docker run -d -p 5000:5000 -t mysys.mktdata:0.1


Deploy to aws

1. login aws
	> aws configure
	key: 		
	secret key: 

2. login aws ecr
	> aws ecr get-login --region us-west-2
	> docker login -u AWS https://122621547060.dkr.ecr.us-west-2.amazonaws.com --password

3. tag image
	> docker tag mysys.mktdata:1.3 122621547060.dkr.ecr.us-west-2.amazonaws.com/repo-mysys:1.3
3. push image
	> docker push 122621547060.dkr.ecr.us-west-2.amazonaws.com/repo-mysys:latest



