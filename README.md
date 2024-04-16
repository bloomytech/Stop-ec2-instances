**SERVERLESS EC2 INSTANCE SHUT DOWN SCHEDULER FOR ORGANISATION WORKING HOURS**

** Scenario:**: In some companies, there is no need to run EC2 instances round the clock. they require instances to operate during specific time periods. 
 To address this, We will implement Lambda function for stopping the instances and set up cloudwatch events that will triger the lambda fucntion at exactly 12:00.

   ![266763781-287063a4-964a-4f8b-b88e-25535b7f4691](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/4d616088-3e4b-4e0b-8c25-50105cb966c4)
**Steps:**
**Step 1**
**Creating Instances or use existing instances**

**Step 2:**

**Creating the Policy:**
 1. Navigate to the IAM Console
 2. Click on "Policies" and then click on " Create policy"
       ![266684770-92ea0ecd-8106-4e7f-80fc-c815093cf319](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/cbe2f9c6-2277-4b8b-894f-1cfcd1057ea7)
 3. Select services as Ec2.
 4. And Actions are DescribeInstances, StopInstances
 
 5.  ![266685226-ca8dc00e-4931-4646-a984-f251d83ebf6a](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/bc57141c-17ff-4ed6-a650-0ceb70481ee6)
 
 6.  ![stop instance](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/771b6c11-8ce9-43d9-b941-439bebb7ef4d)

 7.  ![266685318-8543cf1c-26d3-41dd-9121-99015183f760](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/679c00f6-ff57-4542-87e8-8a1aee085989) NB: change the policy name to stop-ec2-instance and the description to stop ec2 running instances

 8.  ![266685384-78b57e8c-b8b5-470e-9af1-e7789b09f522](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/c6fa773a-885f-4bb2-a2a3-5678c25db4a5)

 9.  ![266685404-1a1da31e-d564-4264-9b4e-fdb5438ed705](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/46fdea5e-0157-4250-8e1d-39f859f6314e)
 10. Now that we have created a policy for stopping instances, we are going to create a Lambda function with its role and attach the policy to that role.

     **Step 3**

     **Creating the Lambda functions:**
     1. Navigate to Lambda on the management console
     2. Follow the outlined steps below
   
     3.  ![266688772-0c16bb73-c4e2-4d0d-94a3-d7eb6a7b2468](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/bf897d6f-d51a-43be-94b1-c178b03c6f37)
   
     4.  ![266688789-0e1249d5-b472-46bb-8f8f-9cfffaed63e9](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/e2f3c913-36fd-4131-bdbd-068e17f34f80)
     5. Remove the default function and paste stop-ec2-instance-py python code
   
     6.  ![lambda function](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/dc381107-2d1d-4358-9bda-4ff6c8717e92)
     7. Click on "Deploy" to save the changes
     8. Click on "Test"

     9.  ![266689003-00a475ec-d570-47ef-9487-9a7ad6f99c67](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/06d3fe27-0830-442e-baba-849410788f59) NB. change event name to stop instance
     10. Click on " Configuration" on the Lambda functin Tab and click on the "Stop-Ec2-Instances-role-ik9mtlab". It will open a new tab to add permision to the role
     11.  ![lambda role](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/b6e159e4-0850-4cd4-9137-6feb803b5507)
     12. Select the policy you created before and click "Add permision"
     13. Now go back to the Lambda console and then test the code. You will see Execution succeeded and the instances in stopped state.
     14. Now we are ready to proceed and create schedules for this Functions
    
     **Step 4**

     **Creating the Schedues Using Cloud watch**
     1. Navigate to the CloudWatch console
     2. Follow the outlined steps below
   
     3.   ![266693720-a932c63f-8a3b-46aa-ade2-ed0d9dd8cdac](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/e7eefbc8-01b6-4d46-b2a4-baa4208adf11)
   
     4.   ![266693744-cfd0914c-7c0c-4064-ae3e-72874467fe7c](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/fa373ba0-6959-4479-ab18-3aac17192b21)

     5.   ![name stop](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/52458940-5369-4038-bbe5-46de29f89aae)

     6.  Click "Continue in EventBrigde Scheduler"
     7.  Select "Recurring Schedule" and "Cron-Based Schedule"
     8.  Set the Cron Tab as follow to automatically triger by 12:00 based on your time zone
   
     9.    ![cron job](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/a66795ea-cdab-4d73-8dd6-5bd6fc7021fd)

     10.    ![266693988-70f29eaa-73fc-49ec-9c39-a6d1214d14f3](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/6d03a1f0-fbea-46a6-86d8-8fd6368f2fe0)

     11.    ![266694020-8935ecd6-ce42-4347-b48c-3b5564679c03](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/328f1b6c-015e-43fe-ac17-e8a702bfb192)
     12.   Choose your Lambda function to stop ec2 instance and click " Next"
     13.   Also choose "NONE" from the Action after schedule completion
     14.    ![266694241-ea584d14-d997-46d7-b1ec-f07cb88a9ede](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/51f3d9f9-f442-463e-affd-8e0b47550f3d)
     15.    ![266694270-b76d4878-b391-4d9c-9b12-07b1b1ebfb5d](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/1acee5b4-62f2-4a0f-aadd-56dd886241cd)

        We have successfully cretaed a Lambda function that will be triggered by CloudWatch EventBridge schedule to shut down running ec2 instances by 12:00am everyday.

