#!/usr/bin/python

# https://github.com/tholewebgods/py-jenkins-cli
#
# Copyright (c) 2014 Thomas Lehmann
#
# Licensed under MIT
#
# See LISENCE.MIT in the project root directory for full license text

import re
import subprocess

class JenkinsCli(object):
	"""Jenkins CLI API"""

	def __init__(self, host, cli_jar, key_file=None):
		self._host = host
		self._jar = cli_jar
		self._key_file = key_file

		self._base_args = ["java",
			"-jar", self._jar,
			"-s", self._host]

		if key_file != None:
			self._base_args = self._base_args + ["-i", self._key_file]

	def _run_command(self, command_name, args):
		_args = self._base_args + [command_name] + args

		print "Running '%s'" % (" ".join(_args))

		p = subprocess.Popen(_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		# read from stderr and out
		out = p.stdout.read()
		err = p.stderr.read()

		# blocking wait for process to finish
		ret = p.wait()

		return (ret, out, err)

	def get_joblist(self):
		"""Get a list of jobs as list"""

		(ret, out, err) = self._run_command("list-jobs", [])

		if ret != 0:
			raise Exception("Cannot get list of jobs (%d): %s" % (ret, err))
		else:
			list = out.split("\n")
			# remove empty line
			list.pop()
			return list

	def get_job(self, name):
		"""Get the job configuration XML as string for the passed job name"""

		(ret, out, err) = self._run_command("get-job", [name])

		if ret != 0:
			raise Exception("Cannot get job config (%d): %s" % (ret, err))
		else:
			return out

	def create_job(self, name, config):
		"""Create a job with name passing a configuration XML string"""

		args = self._base_args + ["create-job", name]

		print "Running '%s'" % (" ".join(args))

		p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		# stdout/stderr string
		(out, err) = p.communicate(config)

		# blocking wait for process to finish
		ret = p.wait()

		if ret != 0:
			raise Exception("Cannot create job (%d): %s" % (ret, err))

	def _run_writeonly_command(self, command_name, args):
		_args = self._base_args + [command_name] + args

		print "Running '%s'" % (" ".join(args))

		p = subprocess.Popen(_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		# read from stderr and out
		out = p.stdout.read()
		err = p.stderr.read()

		# blocking wait for process to finish
		ret = p.wait()

		return (ret, out, err)

	def delete_job(self, name):
		"""Delete a job by name"""

		(ret, out, err) = self._run_writeonly_command("delete-job", [name])

		if ret != 0:
			raise Exception("Cannot delete job (%d): %s" % (ret, err))

	def enable_job(self, name):
		"""Enable a job by name"""

		(ret, out, err) = self._run_writeonly_command("enable-job", [name])

		if ret != 0:
			raise Exception("Cannot enable job (%d): %s" % (ret, err))

	def disable_job(self, name):
		"""Disable a job by name"""

		(ret, out, err) = self._run_writeonly_command("disable-job", [name])

		if ret != 0:
			raise Exception("Cannot disable job (%d): %s" % (ret, err))

