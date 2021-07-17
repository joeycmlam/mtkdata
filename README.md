# Market Data

This is a simple example package. You can use
[Github-flavored Markdown](https://github.com/joeycmlam/mktdata/)
to write your content.

Name: mktdata

Build Command: docker build -t mysys.mktdata:0.4 .

Start Command: docker run -d -p 5000:5000 -t mysys.mktdata:0.1


Deploy to aws
https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html

1. login aws
	> aws configure
	key: 		
	secret key: 

2. login aws ecr
	> aws ecr get-login --region us-west-2
    And then copy the output --> docker login -u AWS -p .... and removing -e none
                  


step 3: create a repositorys
        aws ecr create-repository \
            --repository-name repo-mysys \
            --image-scanning-configuration scanOnPush=true \
            --region us-east-1
            

3. tag image
	> docker tag mysys.mktdata:0.4 122621547060.dkr.ecr.us-west-2.amazonaws.com/repo-mysys:0.4
           
         
         
4. push image
	> docker push 122621547060.dkr.ecr.us-west-2.amazonaws.com/repo-mysys:latest


Repeat similar the above similar steps on EC2 in order to pull the docker image


5. pull on EC2 machine
	> docker pull 122621547060.dkr.ecr.us-west-2.amazonaws.com/repo-mysys:0.4

5. run the process
	docker run  -d -p 80:80 -t 122621547060.dkr.ecr.us-west-2.amazonaws.com/repo-mysys:0.4