import ftplib
import os
"""
Assumption all the files matching the downloading pattern are not older than 1 year 
"""
def get_dir_list_ftp_server(base_dir):
    Dir_list = []
    with ftplib.FTP(host="ftp-emea.teoco.com", user="Airtel3G", passwd="PocAg3") as ftp_con:
        ftp_con.cwd(base_dir)
        #Swapan: In the line below split was not working correctly with maxsplit, later I explicitly mark the x as string then it work correct
        ftp_con.retrlines('LIST', lambda x='': Dir_list.append(x.split(maxsplit=8)))
        ftp_con.close()
    return base_dir, Dir_list


# We will run the following method for each dir or file obtained from ftp server
def dir_checker(base_dir, each_dir_attrbt_list = [], file_list_to_downloaed =[]):
    if each_dir_attrbt_list[0].startswith('d'):
        # TODO: base_dir_name has become hard-coded by initial base-dir name, need to improve, done
        base_dir_name, sub_dir_list_with_attributes = get_dir_list_ftp_server(base_dir + '/' + each_dir_attrbt_list[-1])
        # print(base_dir_name, end = "\t")
        # print(sub_dir_list_with_attributes)
        for sub_dir_attribute in sub_dir_list_with_attributes:
            dir_checker(base_dir_name, sub_dir_attribute, file_list_to_downloaed)
    else:
#         TODO: In case of file we need to do multiple tasks till ftp download
#         TODO: Here we will check if the file matching pattern then only be appended to list
#         TODO: Here we will check time stamp of the file before appending into download list
        each_dir_attrbt_list[-1] = base_dir + "/" + each_dir_attrbt_list[-1]
        file_list_to_downloaed.extend(each_dir_attrbt_list[-1:])

    return file_list_to_downloaed


