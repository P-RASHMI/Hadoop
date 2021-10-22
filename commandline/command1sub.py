'''
@Author: Rashmi
@Date: 2021-10-22 19:31
@Last Modified by: Rashmi
@Last Modified time: 2021-10-23  00:11
@Title :Write a Python program for executing hadoop hdfs using subprocess 
'''
import subprocess

def run_commands(args_list):
    '''
    Description : To execute the hadoop hdfs commands using subprocess libraries
    '''
    print(f'Running system command: {args_list}')
    processed_inp = subprocess.Popen(args_list,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = processed_inp.communicate()
    s_return = processed_inp.returncode
    return s_return,s_output, s_err

if __name__ == '__main__':
     
    #create directory 
    dir_to_created= run_commands(['hadoop', 'fs', '-mkdir', '/Hadoopcommandlinepgm1'])
    print(dir_to_created)
    #upload files from local system to hdfs using put
    put_file= run_commands(['hadoop', 'fs', '-put', '/home/lenovo/Desktop/Python_work/hadoop/file1.txt', '/Hadoopcommandlinepgm1'])
    print(put_file)
    list_all= run_commands(['hadoop', 'fs', '-ls', '/Hadoopcommandlinepgm1'])
    print(list_all)
    # #download files from hadoop to local using get
    get_file= run_commands(['hadoop', 'fs', '-get', '/Hadoopcommandlinepgm1/file1.txt', '/home/lenovo/Desktop/Python_work/hadoop/file1out.txt'])
    print(get_file)
    # #to list all files and directories present in root 
    list_all= run_commands(['hadoop', 'fs', '-ls', '/'])
    print(list_all)
    # #to execute the contents of file
    file_contents_cat= run_commands(['hadoop', 'fs', '-cat', '/Hadoopcommandlinepgm1/file1.txt'])
    print(file_contents_cat)
    # #to copy the file from local system to hdfs using copyFromLocal
    copy_from_local_syst= run_commands(['hadoop', 'fs', '-copyFromLocal', '/home/lenovo/Desktop/Python_work/hadoop/file2.txt', '/Hadoopcommandlinepgm1'])
    print(copy_from_local_syst)
    # #to copy the file from hdfs to local system using copyToLocal
    copy_to_local_syst= run_commands(['hadoop', 'fs', '-copyToLocal', '/Hadoopcommandlinepgm1/file2.txt', '/home/lenovo/Desktop/Python_work/hadoop/file2out.txt'])
    print(copy_to_local_syst)
    # #to create another directory and remove it
    another_direct = run_commands(['hadoop','fs','-mkdir','/hadoop2dir'])
    print(another_direct)
    remove_directry= run_commands(['hadoop', 'fs', '-rm', '-r', '/hadoop2dir'])
    print(remove_directry)