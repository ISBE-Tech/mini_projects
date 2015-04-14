# Using the Command Line

Command line navigation is an important skill to have for all projects, whether it's working in git, hosting a web server, or managing your computer.

### Navigation

The main commends for navigating via command line are `cd`, `ls`

`ls` is used to list the contents of the current directory.
For example:
```
$ ls
cloud  config public
```

`cd` means 'current directory' and can be used to navigate to another directory.
```sh
$ cd cloud 
```
will move us into the `cloud` directory.

If we type `ls` again it should list the contents of this directory, in my case, it looks like this:
```sh
$ ls
main.js
```

To return to the upper folder, type `cd ..`

To make a new directory, type `mkdir <directory name>`

To create a new file, just type `touch <filename>.<file extension>`

### Working with Files

The first part of this project will be creating a text file.

A simple command line function for creating a text file is `cat`

To create a simple text file, use the command
```sh
$ cat > test.txt
```

You should now have a blank line in your terminal: Anything you type will end up in the text file.
For now, type several lines with foods on them or something.

```sh
$ cat > test.txt
bread
milk
flour
```

To stop creating the file and save its changes, hit ^D (control+d).

If you type `ls` now you should see `test.txt`. You can view its contents with
```sh
$ head test.txt
```

`head` is a function which returns the first n lines of a file. Without specifying any argument, it returns the entire file.

By introducing an `argument` to the function call we're able to change how many lines it returns.

Try running `$ head -2 test.txt` and see what it outputs.

Now let's add another few lines to it.
To do this, use `cat >> test.txt` — note the *>>*

```sh
$ cat >> test.txt
carrots
lemons
```

Again, ^D closes the file.


### Searching 

A useful command is `egrep`, which can be used to search within files.

Given the list of foods we generated, we can search for items in the list that contain certain characters.

```sh
$ egrep 'a' test.txt
```

will return a list of all the entires in the list that contain the letter 'a'.
This is a trivial example of something that can be really useful on large files.

### Redirection and Piping 
There are useful ways we can manipulate the outputs of command line functions.
*Redirection* is the first and involves the `>` and `<` characters.

Using `>` after a function call will cause the output of that function to be saved to whatever file we specify after the `>`.

For example,

```
$ ls > output 
```

will redirect the output of ls into a file called `output`.
If you perform `ls` now you should see a file called `output`. 
`cat output` will show you the contents of this file—the names everything that's in this directory.

*Piping* is a way to pass the outputs of functions as the inputs to other functions.

In some languages we might do something like
```
function1(function2(x))
```
which would call `function1` with the result of calling `function2` on x as its argument.

In the command line this is mostly done with the `|` operator (shift+\).

First look at what happens when we run `ls /etc`—it returns a list of the contents of the /etc directory in your computer.
Say we only want the first 3 lines of this output.
The function we'd use for this is `head` with the optional argument `-3`.
Without piping, we would have to do something like:

```
$ ls /etc > myoutput
$ head -3 myoutput
```

With piping we can save a line and don't need to create a file for no reason.
Execute `$ ls /etc | head -3` and you'll see the first 3 entries in the /etc directory.

### Grepping

`grep` is a function similar to egrep that can be used to search pretty much anything.

We can pipe the result of a function into a grep search and find any occurences.

For example, using the example file, do:

```
$ cat example.txt | grep "a"

bananas
peaches
bread
ice cream
```

We get all the elements from `cat example.txt` that contain an 'a'.


### Processes

Everything that happens on your computer is a process—it has an ID to refer to it, a runtime associated with it, etc.

If you know the ID of a process—called its PID (process ID)–you can end it through the terminal.

This is done with `kill <process id>`.

### FUN PART

Something useful that can be done in command line is searching for a process running on your computer—then killing it.

Processes can be listed with `ps`.
You'll only see results that have to do with terminal—to expand to all processes, include the option flag `-x`.

It'll look like:
```
$ ps -ax
...
lots of stuff
```

Using piping and the functions we've learned so far, try to kill a process running on your computer.

We'll kill TextEdit because that's something that's pretty safe to kill.
Make sure you have everything saved first so you don't lose any progress.

Open TextEdit (or another application you want to kill) then using the functions we've discussed find it's pid.

Then use kill to end it.

Note: go ahead and send me your suggested solution if you feel unsure about killing a process.




























