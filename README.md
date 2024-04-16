![266694225-1d11c5b3-a734-470c-bdf5-ab29d6f3f14c](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/4bdca5b4-6cc7-4a4b-a25f-996e58e9a761)![266693720-a932c63f-8a3b-46aa-ade2-ed0d9dd8cdac](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/1b8499e1-83fc-463f-9cf0-94231c0a935d) Stop-ec2-instances
Lambda function to stop  ec2 instances
![266763781-287063a4-964a-4f8b-b88e-25535b7f4691](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/4d616088-3e4b-4e0b-8c25-50105cb966c4)
**Steps:**
**Step 1: **
**Creating Instances or use existing instances**

**Step 2:**

**Creating the Policy:**
 1. Navigate to the IAM Console
 2. Click on "Policies" and then click on " Create policy"
![266684770-92ea0ecd-8106-4e7f-80fc-c815093cf319](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/cbe2f9c6-2277-4b8b-894f-1cfcd1057ea7)
 3. Select services as Ec2.
 4. And Actions are DescribeInstances, StopInstances
 5. ![266685226-ca8dc00e-4931-4646-a984-f251d83ebf6a](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/bc57141c-17ff-4ed6-a650-0ceb70481ee6)
 6. ![stop instance](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/771b6c11-8ce9-43d9-b941-439bebb7ef4d)
 7. ![266685318-8543cf1c-26d3-41dd-9121-99015183f760](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/679c00f6-ff57-4542-87e8-8a1aee085989) NB: change the policy name to stop-ec2-instance and the description to stop ec2 running instances
 8. ![266685384-78b57e8c-b8b5-470e-9af1-e7789b09f522](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/c6fa773a-885f-4bb2-a2a3-5678c25db4a5)
 9. ![266685404-1a1da31e-d564-4264-9b4e-fdb5438ed705](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/46fdea5e-0157-4250-8e1d-39f859f6314e)
 10. Now that we have created a policy for stopping instances, we are going to create a Lambda function with its role and attach the policy to that role.

     **Step 3**

     **Creating the Lambda functions:**
     1. Navigate to Lambda on the management console
     2. Follow the outlined steps below
     3. ![266688772-0c16bb73-c4e2-4d0d-94a3-d7eb6a7b2468](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/bf897d6f-d51a-43be-94b1-c178b03c6f37)
     4. ![266688789-0e1249d5-b472-46bb-8f8f-9cfffaed63e9](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/e2f3c913-36fd-4131-bdbd-068e17f34f80)
     5. Remove the default function and paste stop-ec2-instance-py python code
     6. ![lambda function](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/dc381107-2d1d-4358-9bda-4ff6c8717e92)
     7. Click on "Deploy" to save the changes
     8. Click on "Test"
     9. ![266689003-00a475ec-d570-47ef-9487-9a7ad6f99c67](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/06d3fe27-0830-442e-baba-849410788f59) NB. change event name to stop instance
     10. Click on " Configuration" on the Lambda functin Tab and click on the "Stop-Ec2-Instances-role-ik9mtlab". It will open a new tab to add permision to the role
     11. ![lambda role](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/b6e159e4-0850-4cd4-9137-6feb803b5507)
     12. Select the policy you created before and click "Add permision"
     13. Now go back to the Lambda console and then test the code. You will see Execution succeeded and the instances in stopped state.
     14. Now we are ready to proceed and create schedules for this Functions
    
     **Step 4**

    ** Creating the Schedules Using Cloud Watch:**
      1. Navigate to the CloudWatch Console
      2. Follow the outlined steps below
      
      3.![266693720-a932c63f-8a3b-46aa-ade2-ed0d9dd8cdac](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/6b5171df-97ad-41e6-99e0-798dee4fcb71)

      4. ![266693744-cfd0914c-7c0c-4064-ae3e-72874467fe7c](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/d443bb3f-8c56-455c-9362-007b867a3bca)

      5.![name stop](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/e2944316-0833-425d-931b-e439d58be145)

      6. click " Continue in EventBrigde Scheduler"
      7. Select " Recurring Schedule" and "Cron-Based schedule"
      
      8. ![cron job](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/a2791ab9-488d-4590-b2e5-7c83ce7f870b)

      9. ![266693836-ed864740-4d80-4c4f-80d7-2fa74737d3c4](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/b1081d86-58e0-41ca-a95a-7936b7bcfeb1)
      10. Click "Next"
      11. ![266694020-8935ecd6-ce42-4347-b48c-3b5564679c03](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/648a7583-f2f5-4db0-82b3-3817e314bd06)

      12. Choose your Lambda function for Stop-ec2-instance
      13. Click "Next"
     
      14. ![266694225-1d11c5b3-a734-470c-bdf5-ab29d6f3f14c](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/c292954c-bf71-49d6-b8e2-97ba8cd93192)

      15.![266694241-ea584d14-d997-46d7-b1ec-f07cb88a9ede](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/f4973706-6dcf-428c-a425-39bf10b7f530)

      16.![266694270-b76d4878-b391-4d9c-9b12-07b1b1ebfb5d](https://github.com/bloomytech/Stop-ec2-instances/assets/142004482/5144a3be-5d09-4d8f-ba2a-81806e507762)

      
We have successfully cretaed a Lambda function that will be triggered by CloudWatch EventBridge schedule to shut down running ec2 instances by 12:00am everyday.

