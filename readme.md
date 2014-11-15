
# PyJenkinsCli

Python API to Jenkins CLI

This API makes system calls to run the Jenkins CLI .jar with the appropriate commands.


# Usage

```
from jenkinscli import JenkinsCli


# URL to the Jenkins instance
JENKINS_HOST = "http://localhost:8080/"

# path to the Jenkins CLI .jar file
JENKINS_CLI_JAR = "/path/to/jenkins-cli.jar"

# path to the SSH key file (openssh format) or None if not necessary
JENKINS_SSH_PRIV_KEY = "/path/to/id_rsa_private_key_file"


jenkins = JenkinsCli(JENKINS_HOST, JENKINS_CLI_JAR, key_file=JENKINS_SSH_PRIV_KEY)

# Get list of job names
job_list = jenkins.get_joblist()

# create job with name and config as string
jenkins.create_job("Job name", config_xml_string)

# disable job by name
jenkins.disable_job("Job name")

# enable job by name
jenkins.enable_job("Job name")

# delete job by name
jenkins.delete_job("Job name")

# get config xml as string by job name
config_xml = jenkins.get_job("Job name")
```

A failing command will raise an exception passing the `stderr` value as message.

# How to install

The `.py` file might just be dropped into the systems `site-packages` folder or the environment variable `PYTHONPATH` could be defined or extended with or by the path to the folder containing the `.py` file.


# Status

- API not complete (not all Jenkins CLI are implemented)
- API not stable (method names and signatures might change)
- Implemented calls are functional and stable


# Requirements / Tested on

- Python 2.6
- Tested on Debian 7 and RedHat 6.x (64 Bit)


# License

This project is licensed for you under the MIT license.

