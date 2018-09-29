from multiprocessing import Pool
from EzFTP.ftp_resourse import *

# ***************MAIN()*******************
base_dir_name = '/Swapan'


def download_file_list(file_list):
    with ftplib.FTP(host="ftp-emea.teoco.com", user="Airtel3G", passwd="PocAg3") as ftp_con:
        for R_filename in file_list:
            print("Transferring {} ".format(R_filename))
            # TODO: Local directory is hard coded here, need to be dynamic based on input param, for a particular base_dir all the files recursively, will be downloaded at the directory provided as argument
            ftp_con.retrbinary('RETR ' + R_filename, open("C:\\Users\\Swapan\\Downloads\\FTP\\{}".format(R_filename.split('/')[-1]), 'wb').write)

if __name__ == '__main__':
    print(get_dir_list_ftp_server(base_dir_name))

    base_dir_name, Dir_list = get_dir_list_ftp_server(base_dir_name)
    # print(Dir_list)

    full_list = []
    oldest_time_under_retention = (datetime.datetime.now() - datetime.timedelta(minutes=360))
    for each_dir_attribute_list in Dir_list:
        # The next line is working correctly, but it shouldn't, need to check later
        full_list = dir_checker(base_dir_name, each_dir_attribute_list, oldest_time_under_retention=oldest_time_under_retention)
    # pool_object = Pool()
    # pool_object.map(download_file_list, full_list)
    download_file_list(full_list)

