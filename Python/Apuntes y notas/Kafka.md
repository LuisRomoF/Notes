## **Apache Kafka**
In the context of event streaming, an event is a type of data which describes the entity’s observable state updates over time.  
Most common formats:
* Primitive (text,number,date,etc)
* Key value pair (list, tuple, json,etc)
* Key value with timestamp

Event Stream Platform (ESP)
Used to overcome the challenge of handling different event sources and destinations. An ESP acts as a middle layer among various event sources and destinations and provides a unified interface for handling event-based ETL.
Apache Kafka is an ESP.

A Kafka cluster contains one or many brokers. 

* **Brokers:** The dedicated server to receive, store, process, and distribute events.Brokers are synchronized and managed by another dedicated server called ZooKeeper. Each broker contains one or many topics. You can think of a topic as a database to store specific types of events, such as logs, transactions, and metrics, for example.
* **Topics:** The containers or databases of events.
* **Partitions:** Divide topics into different brokers. 
* **Replications:** Duplicate partitions into different brokers.
* **Producers:** Kafka client applications to publish events into topics.
* **consumers:** Kafka client applications subscribed to topics and read events from them.

**Kafka Streams API** is a simple client library aiming to facilitate data processing in event-streaming pipelines. It processes and analyzes data stored in Kafka topics, thus both the input and output of the Streams API are Kafka topics.
![Stream topology](/Python//Imagenes/Stream_process_topology.png "Topology")