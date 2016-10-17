# README #

This README file explains the functionality of the policy evaluation engine. It elaborates the working model, features and limitations of the implementation.

### Functionalities implemented ###
    This implementation covers the following features-
      * Given a Sub_Id and Res_Id, evaluate a policy on the subject and resource attributes. Apply the obligations once the policy has been evaluated.

      * Given a config file which has n number of requests for same subject and resource, evaluate policies on all of them.

      * Given a config file which has n number of distinct and/or same subjects and resources, evaluate appropriate policy on all of them by sending the request to the appropriate subject co-ordinator.

      * At any point in the execution, if subject or resource conflict is encountered, take the appropriate action (as mentioned in the paper).

### Components ###
    The design has 5 major components. Following is the brief explanation all of the segments-

    Note:- Most of the components are written as specified by the original paper. However, Master and DB_Emulator are two new additions.

      ### DB_Emulator ###-
        This process acts as DB_Emulator. It acts as a DB Server process, updates the attributes when any of the coordinators send the updates and then it sends the DB updates to the workers after a specified time interval (Specified by parameters in the config file- minDBLatency and maxDBLatency).

      ### Master ###-
        This process acts as a master process. As instructed in project.txt, this process upon coming up, starts the processes- application, sub_co, res_co and worker. When all the requests are handled, this process shuts down all the other process.

      ### Application ###-
        This is the entry level process for all the requests. This process upon starting, forms a request object (with appropriate values) and sends it to the matching subject co-ordinator (calculated using the hash function).

      ### Subject Coordinator ###-
        This process runs as a subject Coordinator. Upon receiving a request from application, it forwards it to the relevant Resource Coordinator (calculated from the hash Table). After that, It waits for the worker to send the policy decision. Then it asks the Resource Coordinator to check for conflicts. If everything was successful, it updates the cache (cached replica of DB).

      ### Resource Coordinator ###-
        This is the resource Coordinator process. Upon receipt of policy evaluation request from Subject Coordinator, it forwards the request to one of the workers. Again, after receiving the rewuest from Subject Coordinator for conflict detection, it checks for conflicts and sends the appropriate response.

      ### Worker ###-
        This is the worker process. This process evaluates the policy and sends the subject and resource obligations to the subject Coordinators.


     Note- The code is designed in an object oriented fashion, it is very easy to add/remove features and extend the support for other features



* Version
* 1.0

### Running Instructions ###

* Summary of set up
    The setup is simple to run. To run the policy evaluation-
        $ dar policy.da <Test Case Config File> <DB Config File>

    Both the arguments are optional. If not provided, the program defaults to the basic config.
        e.g.-
            $ dar policy.da basic.config dbconfig.config



### Tests Cases ###

* Apart from the main file (policy.da) , the submission also contains the test cases to replicate various        scenarios. The test are written in config files and are named in an intuitive way. Following are the names of the test case config files and their details-

    * basic.config -> This config file tests the basic functionality (1 Subject, 1 Resource).

    * multiple_subjects.config -> This config file tests the condition when there are more than one subjects involved. It sends the update to appropriate Subject coordinator.

    * conflict.config -> This config file tests the conflict condition. It restarts the appropriate process on detecting a conflict.

    * stress.config -> This config file lists the stress testing test cases. It lists 6 requests, 5 workers, 5 subject coordinators, 5 resource coordinators. The implementation behaves perfectly fine on the stress test cases, restarting any requests if it detects a conflict.


### Contributors ###

* Arunesh Pandey (110945824)
* Arun Rajan (110921170)
