# Welcome to CDK Python Challenge Solution

This is a project for CDK development with Python.

Prerequisite: https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file - if it doesn't exist please create the file and rerun the `pip install -r requirements.txt`
command.

Next you would deploy it to the AWS account - please update the follwoing line of code in app.py 

```
env=cdk.Environment(account='<account_numeber>', region='<region>')
```

When the deployment of the stack is completed. In the terminal the API GW url is provided.

The url has the following:

```
<url>/users - PUT
<url>/users/{email_address} - GET
<url>/users/{email_address} - DELETE
<url>/users/login - POST
```

Example json for PUT event:
```
{
  "email_address": "example@gmail.com",
  "password": "example",
  "name": "Example Name"
}
```

Example json for POST:
```
{
  "email_address": "example@gmail.com",
  "password": "example"
}
```

If you have any issues with running the code please let me know.

