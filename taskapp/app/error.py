import os, sys


def build_error_references(): 
    logs = [(logger,open(logger,"a")) 
            for logger in os.listdir("../docs") 
           if logger.endswith(".log")]

    error_logs = {k:v for k,v in logs}

    #print error_logs   #Shows docs contents


    return error_logs
   


def write_to_log(log_dict = build_error_references(),
                 log_ref = "post_errors.log",
                 error = "\nUNKNOWN ERROR"
                ):
    log_dict[log_ref].write(error)


write_to_log()

'''
for x in error_logs:
    print x, " written"
    error_logs[x].write("\nTEST")
    error_logs[x].close()
    

sys.exit(0)

'''
