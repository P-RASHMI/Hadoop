     Word count :
hadoop version  -----> Hadoop 3.3.1
Python version -------> Python 3.8.10

 Create text input file ,mapper.py,reducer.py : in home folder ,word_count folder
~/word_count$ nano input1.txt
~/word_count$ nano map1.py
~/word_count$ nano reducer1.py
To change the mode for all files :
~/word_count$ chmod a+x input1.txt
~/word_count$ chmod a+x map1.py
~/word_count$ chmod a+x reducer1.py

Executing command locally : of mapper--->map1.py
~/word_count$ cat input1.txt |python3 map1.py
Op:
Hi    1
this    1
is    1
sample    1
program    1
for    1
wordcount    1
Hi    1
this    1
is    1
to    1
execute    1
wordcount    1
of    1
the    1
we    1
get    1
count    1
of    1
words    1
Hi    1
this    1
is    1
sample    1
program    1
for    1
wordcount    1
Hi    1
this    1
is    1
to    1
execute    1
wordcount    1
of    1
the    1
input    1
data    1
the    1
words    1
are    1
incremented    1
we    1
get    1
count    1
of    1
words    1


Executing the command of reducer :

:~/word_count$ cat input1.txt |python3 map1.py|sort |python3 reducer1.py
Op:
are    1
count    2
data    1
execute    2
for    2
get    2
Hi    4
incremented    1
input    1
is    4
of    4
program    2
sample    2
the    3
this    4
to    2
we    2
wordcount    4
words    3

Execute pgm on hdfs:
Servers to start:
~/word_count$ start-all.sh
~/word_count$  jps

Create folder on hadoop :word-count-2:
/word_count$ hadoop fs -mkdir /word-count-2
To put the input file into directory:
~/word_count$ hadoop fs -put input1.txt /word-count-2
~/word_count$ hadoop fs -ls /word-count-2

To get the hadoop jar the command is :
~/word_count$ find /home/lenovo  -name  ‘hadoop-streaming*.jar’

Placing file files into hadoop:
~$ hadoop  jar  /home/lenovo/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar  -file  /home/lenovo/word_count/map1.py  -mapper   'python3 map1.py'   -file /home/lenovo/word_count/reducer1.py   -reducer  'python3 reducer1.py'   -input /word-count-2/input1.txt       -output    /word-count-2/outputfile

Output:  Output directory: /word-count-2/outputfile

To check the contents of outputfile:
~$ hadoop fs -ls /word-count-2/outputfile
Output:
     -rw-r--r--   1 lenovo supergroup          0 2021-10-22 16:30 /word-count-2/outputfile/_SUCCESS
-rw-r--r--   1 lenovo supergroup        142 2021-10-22 16:30 /word-count-2/outputfile/part-00000

To get the  output:
  ~$ hadoop fs -cat /word-count-2/outputfile/part-00000
To download the output to local system (get):
$ hadoop fs -get /word-count-2/outputfile/part-00000  /home/lenovo/word_count/out
