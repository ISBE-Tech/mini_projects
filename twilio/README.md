## APIs
An API is an initialization for "Application Program Interface" and describes the way a given piece of software works.

A lot of APIs now are hosted for public usage but many require **tokens**.

**Tokens** are essentially a key that grants you access to the API. Owners of the application can restrict who uses their API by giving out keys and can monitor usage through it.

## Secrets (shh)

When you're using a token for API access you need to make sure it's hidden from your code. Pushing code up to GitHub that contains your API key is dangerous.

The way we'll get around this is by using environmental variables and sourcing.

### Environment Variables and Sourcing

To keep certain variables (like tokens) out of code, they can be set to environment variables.

Environment variables are variables local to the terminal.

They're set using `$ export MY_NAME='andy'`

Then, `$ echo $MY_NAME` should print out my name.

We can write a file that contains all of the variables we need, called `.secret`, that will set all the enviromental variables for us when we run `$ source .secret`.

Run the command `$ cp .secret.example .secret` to create a copy of .secret.example called .secret.

This is where we'll put our auth token and identifier once we get them.

## Using the Twilio API

The first thing to do is to [Sign up for Twilio](https://www.twilio.com/try-twilio).

Confirm your account then click `Get your number` from the dashboard, save it somewhere.

In the top right of the dashboard is `Show API Credentials`—this is your token and an identifier for your account.

Copy these into the .secret file by opening it with Sublime or another text editor, then use `$ source .secret` to export them to the environment.

### The Python Wrapper

Twilio (and other companies with popular APIs) make their own wrappers for their APIs. Twilio has one that can be installed using:

```
$ pip install twilio
```

If you run into a `Permssion denied:` error, run `$ sudo pip install twilio`.

### Sending an SMS

Twilio's API can be used to send and receive SMS messages (and other cool stuff).

Any project we're going to create using the Python Twilio wrapper will need to first import it, using

```
from twilio.rest import TwilioRestClient
```

This imports the relevant code from our `$ pip install twilio` so we can use it in a our project.

Next, a **client** needs to be initialized.

A **client** is a class that handles authentification with your token and account id then performs the interaction with the API.

A Twilio client is initialized as `client = TwilioRestClient(account_sid, auth_token)`.

The two arguments are an `account_sid` and an `auth_token`, the two things we put into our `.secret` file.

For Python to be able to access the environmental variables, we need to use a function built into Python.

The `example.py` shows how this is done, using `import os` then `os.getenv('VARIABLE NAME')`.

Fill in the information in the message-sending function, then execute the file to send yourself a text.

## Challenge

Using the Twilio documentation, learn how to check received SMS messages.

Create a program that can execute two different commands based on the message it receives.