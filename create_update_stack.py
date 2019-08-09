import subprocess
import argparse
import os.path

#--stack-name 
#--template-body file://
#--parameters    file://
#--region  

arg = argparse.ArgumentParser(description='check_update_stack.py')
#Command Line Arguments

arg.add_argument('--action', action="store", type = str, default="create-stack")
arg.add_argument('--stackname', action="store", type = str)
arg.add_argument('--template', action="store",type = str)
arg.add_argument('--parameters', action="store", type=str)
arg.add_argument('--region', action="store", type=str,default="us-west-2")



arg_value = arg.parse_args()
action = arg_value.action
stackname = arg_value.stackname
template = arg_value.template
parameters = arg_value.parameters
region = arg_value.region





template_url = "file://" + os.path.abspath(template)
parameters_url = "file://" + os.path.abspath(parameters)

print(template_url)

 #'--template-body',templatebody

cmd = 'aws cloudformation ' + action + ' --stack-name ' + stackname + ' --template-body ' + template_url + ' --parameters ' + parameters_url + ' --region ' + region

print(cmd)

subprocess.call(cmd)

#output, errors = p.communicate()

#if not output:
    #print("empty")
#else:
    #print(output)

#if not errors:
   # print("No Errors")
#else:
   # print(errors)

