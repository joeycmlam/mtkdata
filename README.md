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
   
> aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 122621547060.dkr.ecr.us-west-2.amazonaws.com/mysys-repo


step 3: create a repositorys
        sudo aws ecr create-repository \
            --repository-name repo-mysys \
            --image-scanning-configuration scanOnPush=true \
            --region us-west-2
            

3. tag image
	> docker tag mysys.mktdata:0.5 122621547060.dkr.ecr.us-west-2.amazonaws.com/mysys-repo:0.5
           
         
         
4. push image
> docker push 122621547060.dkr.ecr.us-west-2.amazonaws.com/mysys-repo:0.5


Repeat similar the above similar steps on EC2 in order to pull the docker image


5. login EC2 and then login ecr docker pull on EC2 machine
> docker pull 122621547060.dkr.ecr.us-west-2.amazonaws.com/mysys-repo:0.5

5. run the process
> docker run  -d -p 80:80 -t 122621547060.dkr.ecr.us-west-2.amazonaws.com/repo-mysys:0.5
	
	
	
POST-RELEASE check

curl http://ec2-52-12-203-177.us-west-2.compute.amazonaws.com:80/



curl http://ec2-52-12-203-177.us-west-2.compute.amazonaws.com:80/get_price/C
