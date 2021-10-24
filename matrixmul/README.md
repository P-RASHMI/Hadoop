hadoop version  -----> Hadoop 3.3.1
Python version -------> Python 3.8.10

Execute pgm on hdfs:
Servers to start:
$start-all.sh
$jps

->Create text input file ,mapper.py,reducer.py : in home folder of matrixmul
mkdir matrixmul
Create input text file ,mapper,reducer file:
nano mapper.py
nano reducer.py
nano matrixinput.txt
Executing command locally : of mapper ----->mapper.py
~/hadooppractice/matrixmul$ cat matrixinput.txt |python3 mapper.py
Op: 
A    ,0,0,1
A    ,0,1,2
A    ,0,2,3
A    ,1,0,4
A    ,1,1,5
A    ,1,2,6
A    ,2,0,7
A    ,2,1,8
A    ,2,2,9
B    ,0,0,1
B    ,0,1,1
B    ,0,2,1
B    ,1,0,1
B    ,1,1,2
B    ,1,2,3
B    ,2,0,1
B    ,2,1,1
B    ,2,2,1

Executing command locally : of reducer ----->reducer.py
$ cat matrixinput.txt |python3 mapper.py |sort |python3 reducer.py
Op:
(0,0)    6
(0,1)    8
(0,2)    10
(1,0)    15
(1,1)    20
(1,2)    25
(2,0)    24
(2,1)    32
(2,2)    40

Place files in hadoop:
~/hadooppractice/matrixmul$  hadoop  jar  /home/lenovo/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -file /home/lenovo/hadooppractice/matrixmul/mapper.py  -mapper   'python3 mapper.py' -file /home/lenovo/hadooppractice/matrixmul/reducer.py -reducer  'python3 reducer.py' -input /matrix/matrixinput.txt -output /matrix/outputmatrixmul

To lists the files in output:
$ hadoop fs -ls /matrix/outputmatrixmul
-rw-r--r--   1 lenovo supergroup          0 2021-10-25 00:30 /matrix/outputmatrixmul/_SUCCESS
-rw-r--r--   1 lenovo supergroup         79 2021-10-25 00:30 /matrix/outputmatrixmul/part-00000

To get the output into local:
hadoop fs -get /matrix/outputmatrixmul /home/lenovo/hadooppractice/matrixmul


