# Shell
A shell is a special user program that provides an interface to the user to use operating system services. 
<br>Shell accepts human-readable commands from the user and converts them into something which the kernel can understand. 
<br>It is a command language interpreter that executes commands read from input devices such as keyboards or from files.

You can run Shell scripts by using bash
```sh
# This is a comment
bash my_script.sh
```

## Shell Variables
Shell variables are like local variables in other programming languages. They are assigned with and = sign without spaces.
<br>To access the content of the variable you can use the echo command and the $ sign to specify the contents of the variable.
```sh
variable=variable_content

echo $variable
```
## Parameters
Special expression $@ (dollar sign immediately followed by at-sign) to mean "all of the command-line parameters given to the script".

For example, if unique-lines.sh contains sort $@ | uniq, when you run:
```sh
bash unique-lines.sh seasonal/summer.csv 
```
Shell replaces $@ with seasonal/summer.csv and processes one file.

## Loops
Structure:
```sh
for variable in list; do body; done

# Examples:
for filetype in gif jpg png; do echo $filetype; done
for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
```

## Concepts
* **Absolute path:** is like latitude and longitude, it has the same value no matter where you are. 
* **Relative path:** specifies a location starting from where you are (pwd).
    The shell decides if a path is absolute or relative by looking at its first character: If it begins with /, it is absolute. If it does not begin with /, it is relative.
* .. (two dots with no spaces) means "the directory above the one I'm currently in".

* ~  (the tilde character) means "your home directory" No matter where you are, ls ~ will always list the contents of your home directory, and cd ~ will always take you home.
## Commands
* control + c quits a running shell command
* pwd (print working directory): tells you where you are
```sh
pwd
```
* ls (listing): prints the contents of the pwd
Flags: 
- -R: Recursive, prints everything underneath a directory, no matter how deeply nested it is.
```sh
ls
```
* cd (change directory):
```sh
cd
```
* cp copy files, rename and move them
```sh
cp original.txt duplicate.txt /new_path
```
* mv move files from one location/folder to another. You can also rename them in the new given path.
```sh
mv current/path/file.txt new/path/file.txt
```
* rm remove

```sh
rm thesis.txt backup/thesis-2017-08.txt
```
removes both thesis.txt and backup/thesis-2017-08.txt
* rmdir remove a folder, it will only work with empty folders
* mkdir creates a new folder on the specified path
* cat (concatenate) prints the contents of files on the screen.
* less prints the contents one page at a time.
* head works like pandas.df.head(). By default it will show 10 lines. You can change this by using the -n flag to specify the number of lines to print.
* man (manual) show a description and options of the command
```sh
man tail 
```
* grep grep can search for patterns as well; we will explore those in the next course. What's more important right now is some of grep's more common flags:

    - -c: print a count of matching lines rather than the lines themselves
    - -h: do not print the names of files when searching multiple files
    - -i: ignore case (e.g., treat "Regression" and "regression" as matches)
    - -l: print the names of files that contain matches, not the matches
    - -n: print line numbers for matching lines
    - -v: invert the match, i.e., only show lines that don't match
    ```sh
    grep incisor -c path/file1.csv path/file2.csv
    ```
    this counts the number of lines in each file that contain the word incisor

* The command wc (short for "word count") prints the number of characters, words, and lines in a file. You can make it print only one of these using -c, -w, or -l respectively.

* sort puts data in order. By default it does this in ascending alphabetical order, but the flags -n and -r can be used to sort numerically and reverse the order of its output, while -b tells it to ignore leading blanks and -f tells it to fold case (i.e., be case-insensitive). Pipelines often use grep to get rid of unwanted records and then sort to put the remaining records in order.

* uniq, whose job is to remove duplicated lines. More specifically, it removes adjacent duplicated lines.
-c shows a count
* echo To get the variable's value, you must put a dollar sign $ in front of it.
```sh
echo $USER
```

## Pipelines
The pipe symbol (|) tells the shell to use the output of the command on the left as the input to the command on the right.

## Wildcards
- \* : means "match zero or more characters".

- ? : matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
- [...] : matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
- {...} : matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.