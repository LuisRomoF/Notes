# **ETL & Data Pipelines with shell, airflow & kafka**

## **Types of pipelines**
+ Dynamic / nonlinear
+ Static / linear 

An **I/O buffer** (input/output) is a holding area for data, placed between processing stages having different or varying delays. Buffers can also be used to regulate the output of stages having variable processing rates, and thus may be used to improve throughput.

## **Stages of pipelines**
* Data extraction
* Data ingestion (into the pipeline)
* Transformation
* Loading data
* Scheduling
* Monitoring 
* Maintenance and optimization


## **Key performance indicators of pipelines**
+ **Latency**: total time it takes for a packet of data to pass through the pipeline. You can break it down to each stage of the process.

+ **Throughput**: how much data can be fed through the pipeline per unit of time. Processing larger packets per unit of time increases throughput.

## **Pipeline monitoring**

--------------------------------------------------------------------

## **Linux Commands and Shell Scripting**
A shell is a powerful user interface for Unix-like operating systems.

```shell
#Create a shell file 
touch file_name.sh

#Open the file on a text editor and type:
#The following command turns your file into a bash shell script
'#!/bin/bash' #this includes the # 

#Call the api to read data and append to a log file
get_data_api >> data.log

#Call python file to read data and write results to csv
python3 main.py data.log res_data.csv

#Load results to front end using api
load_api res_data.csv

#Set permissions to make shell script executable
chmod +x file_name.sh

#then you have to schedule the shell file on Cron
````
-----------------------------------------------------------------------

## **Apache Airflow**
Open source workflow orchestration tool to programmatically author, schedule, and monitor workflows. Monitor, schedule and manage workflows with the webapp.

![Airflow architecture](/Python/Imagenes/workflow_arch.png "Airflow architecture")

A workflow is represented as a **DAG** (a Directed Acyclic Graph), and contains individual pieces of work called tasks, arranged with dependencies.

DAG definition components:
* Library imports
* DAG arguments
* DAG definition
* Task definition
* Task pipeline

**DAG definition example:**
![dag def example](/Python//Imagenes/dag_example.png "DAG definition example")
![dag task](/Python//Imagenes/dag_tasks.png "DAG tasks")

**Main principles**
* Scalable: it uses a modular architecture and can orchestrate an aribtraty number of workers
* Dynamic: pipelines are defined in python allowing dynamic pipeline generation
* Extensible: define your operators and extend libraries to suit your environment
* Lean

Usecases
- define and organiza Machine Learning pipeline dependencies
- increase visibility of processes 
- orchestration
- scheduling 

# Installation
On CMD run:
Make sure you type the correct python version on the constraint files.

    pip install "apache-airflow[celery]==2.3.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.3/constraints-3.7.txt"