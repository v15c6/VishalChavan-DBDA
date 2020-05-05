# EC2 (Elastic Compute Cloud)

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment.

#### Now lets see how to create EC2 in AWS
* ##### Step1: Search EC2 service.
In search bar search for ec2 service. Select ec2 service and then launch the instance.
![](images/Screenshot%20(2).png)


* ##### Step2: Launch ec2 server.
After selecting ec2 service go to launch instance and launch instance.
![Screenshot (4)](images/Screenshot%20(4).png)



* ##### Step3: Choose an Amazon Machine Image (AMI).
An AMI is a template that contains the software configuration (operating system, application server, and applications) required to launch your instance. as of now, we are creating linux instance select free trail amazon linux 2 AMI.
![Screenshot (5)](https://github.com/v15c6/VishalChavan-DBDA/blob/master/images/Screenshot%20(5).png)

* #### Step4: Choose an Instance Type.
Amazon EC2 provides a wide selection of instance types optimized to fit different use cases. Instances are virtual servers that can run applications. They have varying combinations of CPU, memory, storage, and networking capacity, and give you the flexibility to choose the appropriate mix of resources for your applications.
![Screenshot (6)](https://github.com/v15c6/VishalChavan-DBDA/blob/master/images/Screenshot%20(6).png)


* #### Step5: Configure Instance Details.
Configure the instance to suit your requirements. You can launch multiple instances from the same AMI, request Spot instances to take advantage of the lower pricing, assign an access management role to the instance, and more. For now we set it as default.
![Screenshot (7)](https://github.com/v15c6/VishalChavan-DBDA/blob/master/images/Screenshot%20(7).png)

* #### Step6: Add Storage.
Your instance will be launched with the following storage device settings. You can attach additional EBS volumes and instance store volumes to your instance, or edit the settings of the root volume. You can also attach additional EBS volumes after launching an instance, but not instance store volumes.
![Screenshot (8)](https://github.com/v15c6/VishalChavan-DBDA/blob/master/images/Screenshot%20(8).png)


* #### Step7: Add Tags.
To help you manage your instances, images, and other Amazon EC2 resources, you can optionally assign your own metadata to each resource in the form of tags.
![Screenshot (9)](https://github.com/v15c6/VishalChavan-DBDA/blob/master/images/Screenshot%20(9).png)

* #### Step8: Configure Security Group.
A security group is a set of firewall rules that control the traffic for your instance. On this page, you can add rules to allow specific traffic to reach your instance. For example, if you want to set up a web server and allow Internet traffic to reach your instance, add rules that allow unrestricted access to the HTTP and HTTPS ports. For beign beginner we use the default security group.
![Screenshot (10)](https://github.com/v15c6/VishalChavan-DBDA/blob/master/images/Screenshot%20(10).png)

* #### Step9: Review Instance Launch.
In this step we review our instance launch details. You can go back to edit changes for each section.

![Screenshot (11)](https://github.com/v15c6/VishalChavan-DBDA/blob/master/images/Screenshot%20(11).png)



