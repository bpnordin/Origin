import os.path
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(here))
var_path = os.path.join(root,"var")
print var_path

# This file is not for committing. Don't commit it 'cause it has
# passwords in it
configTest={
  "origin_server"               : "127.0.0.1",
  "origin_register_port"        : "5556",
  "origin_measure_port"         : "5557", 
  "origin_alert_port"           : "5558",
  "origin_read_port"            : "5559",
  "origin_json_register_port"   : "5566",
  "origin_json_measure_port"    : "5567", 
  "alert_check_period"          : "30",
  "timestamp_type"              : "uint64",
  "origin_destination"          : "hdf5",

  # MYSQL
  "mysql_local_server"          : "127.0.0.1",
  "mysql_local_db"              : "origintest",
  "mysql_local_user"            : "test",
  "mysql_local_password"        : "test",
  #"mysql_remote_server":"",
  #"mysql_remote_db":"",
  #"mysql_remote_user":"",
  #"mysql_remote_password":"",

  # HDF5
  "hdf5_data_path"    : os.path.join(var_path,"data"),
  "hdf5_data_file"    : os.path.join(var_path,"data","origintest.hdf5"),
  "hdf5_chunksize"    : 2**10, # for testing (make 1kB to 1MB)
  "hdf5_compression"  : 'gzip', # False for no compression

  # Filesystem
  "fs_data_path"      : os.path.join(var_path,"data","origintest"),
  "fs_info_file"      : os.path.join(var_path,"data","origintest","knownStreams.json"),
}

configSite={
  "origin_server"             : "xxx.xxx.xxx.xxx",
  "origin_register_port"      : "5556",
  "origin_measure_port"       : "5557", 
  "origin_alert_port"         : "5558",
  "origin_read_port"          : "5559",
  "origin_json_register_port" : "5566",
  "origin_json_measure_port"  : "5567", 
  "alert_check_period"        : "30",
  "timestamp_type"            : "uint64",
  "origin_destination"        : "hdf5",

  # MYSQL
  "mysql_local_server"        : "127.0.0.1",
  "mysql_local_db"            : "origin",
  "mysql_local_user"          : "_user_",
  "mysql_local_password"      : "_password_",
  #"mysql_remote_server":"",
  #"mysql_remote_db":"",
  #"mysql_remote_user":"",
  #"mysql_remote_password":"",

  # HDF5
  "hdf5_data_path"    : os.path.join(var_path,"data"),
  "hdf5_data_file"    : os.path.join(var_path,"data","origin.hdf5"),
  "hdf5_chunksize"    : 2**10,
  "hdf5_compression"  : 'gzip', # False for no compression

  # Filesystem
  "fs_data_path"      : os.path.join(var_path,"data","origin"),
  "fs_info_file"      : os.path.join(var_path,"data","origin","knownStreams.json"),
}
