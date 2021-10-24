create another folder : WordLength

hadoop version -----> Hadoop 3.3.1 
Python version -------> Python 3.8.10

Execute pgm on hdfs: 
Servers to start: 
$start-all.sh 
$jps

->Create text input file ,mapper.py,reducer.py : in home folder of WordLength
 mkdir WordLength
-> Create input text file ,mapper,reducer file: 
nano mapper.py 
nano reducer.py 
nano inputword.txt
Executing command locally : of mapper ----->mapper.py 
$ cat inputword.txt |python3 mapper.py

Executing command locally : of reducer ----->reducer.py 
$ cat inputword.txt |python3 mapper.py |sort |python3 reducer.py 

Place files in hadoop:
create folder in hadoop:
hadoop fs -mkdir /wordlength
put file in hadoop:
hadoop fs -put /home/lenovo/hadooppractice/WordLength/inputword.txt /wordlength

placing in hadoop:

hadoop jar /home/lenovo/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  
-file  /home/lenovo/hadooppractice/WordLength/mapper.py  -mapper   'python3 mapper.py' 
-file  /home/lenovo/hadooppractice/WordLength/reducer.py  -reducer   'python3 reducer.py' 
-input /wordlength/inputword.txt -output /wordlength/outputwordlen 

to get the file:
hadoop fs -ls /wordlength/outputwordlen
hadoop fs -cat /wordlength/outputwordlen/part-00000
hadoop fs -get /wordlength/outputwordlen /home/lenovo/hadooppractice/WordLength

