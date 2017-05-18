# Elf TAI (Title - Alias - Items)

# Environment
<ul>
<li>Python 3</li>
<li>Python packages: termcolor, argparse</li>
<li>Linux Mint 18 (Should work on every Ubuntu, if not on every Linux)</li>
</ul>

# Initial Setup
* Everything should be fine if the commands below work without throwing any exception.
```
git clone https://github.com/matheushjs/ElfTAI
chmod +x ElfTAI/elftai
./ElfTAI/elftai list
./ElfTAI/elftai add -t "Hello World!" -a hw
./ElfTAI/elftai rm -t hw
```
* After cloning, you can use the following commands to bring 'elftai' program to current directory:
```
cp ./ElfTAI/elftai -r ./ElfTAI/modules_elf ./
./elftai list
rm -rf ./ElfTAI
```

# Usage
[Example image of basic usage](example.png)

## Keep in Mind
* This program can't manage multiple instances of CSV files, so make a clone of elftai for each directory where you'd like to manage something.
* Feel free to change the name of the program ("elftai") to suit the context of what you're managing.
* You can edit the CSV file 'database_elftai.csv' in ElfTAI directory by hand, as long as you acknowledge the format of the CSV file, which is explained below.

## Commands
The program contains 4 subparsers: 'list', 'add', 'rm' and 'comment', each of which can be called like './elftai list', for example.

### list
```
./elftai list
```
Prints a list of all Titles currently in the file.
```
./elftai list [alias/title]
```
Prints information about the Title given as argument. Only the 5 latest items added to each Title are displayed.
```
./elftai list [alias/title] -e 10
```
Same as above, but prints latest 10 items.

### add
```
./elftai add -t [name of new title]
```
Creates a new Title with the name given.
```
./elftai add -t [alias/title] -a [new alias]
```
Adds [new alias] as an alias to the given Title. Title is created if doesn't exist.
```
./elftai add -t [alias/title] -i [new item]
```
Adds the item [new item] to the given Title.

### rm
```
./elftai rm -t [name of title]
```
Removes a Title from the file. This is a destructive command, so the user is prompted for confirmation before execution.
```
./elftai rm -a [alias]
```
Removes the alias [alias] from whatever Title it belongs to.
```
./elftai rm -t [alias/title] -i [item]
```
Removes [item] from the given Title.

### comment
Comment also has its subparsers: 'rm' and 'add'.

```
./elftai comment -t [alias/title] add [comment]
```
Adds [comment] to the list of comments of the given Title.
```
./elftai comment -t [alias/title] rm [index]
```
Removes the comment of index [index] from the given Title.

# Motivation
<p>Consider the following situation: you have a big set of documents to read, each of which are labeled with the area of knowledge they cover (psychology, mathematics etc). Also, each document has it's ID number.</p>
<p>The Elf TAI program will try to build a generic command-line manager for such situations, where the following are TRUE:</p>
<ul>
<li>There exists a big set of items; we'd like to keep track of which items have been processed.</li>
<li>There exists a set of Titles, smaller than the set of items; and each Title characterize a subset of items.</li>
</ul>
<p>Elf TAI allows you to manipulate these Titles and items.</p>
<p>As a bonus, it also allows you to add comments to Titles, which can be any string; useful for adding reminders like "We stopped on page 117", for example.</p>

# CSV format
<p>[Title],[alias1],[alias2],[alias3],[alias4],[...]</p>
<p>[Comment1],[Comment2],[...]</p>
<p>[Item1],[Item2],[Item3],[...]</p>
