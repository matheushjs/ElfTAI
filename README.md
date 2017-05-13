# Elf TAI (Title - Alias - Items)

# Environment
<ul>
<li>Python 3</li>
<li>Python packages: termcolor, argparse</li>
<li>Linux Mint 18 (Should work on every Ubuntu, if not on every Linux)</li>
</ul>

# Usage
[Example image of basic usage](example.png)
```
git clone https://github.com/matheushjs/ElfTAI
chmod +x ElfTAI/elftai
./ElfTAI/elftai list
./ElfTAI/elftai add -t "Hello World!" -a hw
./ElfTAI/elftai rm -t hw
```
* If the commands above work, everything should be fine.
* Make a clone for each directory where you'd like to manage something. In other words, this program can't manage multiple instances of CSV files.
* You can edit the CSV file 'database.csv' in ElfTAI directory by hand, as long as you acknowledge the format of the CSV file, which is explained below.
* After executing the commands above, you can use the following ones to bring 'elftai' program to root directory:
```
cp ./ElfTAI/elftai -r ./ElfTAI/modules_elf ./
./elftai list
rm -rf ./ElfTAI
```

## Commands
The program contains 4 subparsers: 'list', 'add', 'rm' and 'comment', each of which can be called like './elftai list', for example.
### list
```
./elftai list
```
Prints a list of all Titles currently in the file.
```
./elftai list [alias/title] [alias/title]
```
Prints information about each Title given as argument. Only the 5 latest items added to each Title are displayed.
```
./elftai list [alias/title] [alias/title] -e 10
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
Adds [new alias] as an alias to the given Title.
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
```
./elftai comment -t [alias/title] "[comment]"
```
Sets [comment] as the comment on the given title.

# Motivation
<p>Consider the following situation: you have a big set of documents to read, each of which are labeled with the area of knowledge they cover (psychology, mathematics etc). Also, each document has it's ID number.</p>
<p>The Elf TAI program will try to build a generic command-line manager for such situations, where the following are TRUE:</p>
<ul>
<li>There exists a big set of items (documents in this case), and we want to record which of these items have been processed (in this case, read).</li>
<li>There exists a reduced number of titles (labels, in this case), where each title characterizes a set of items.</li>
<li>Each item is characterized by only 1 Title.</li>
<li>Each item can be described by a string (the ID in this case)</li>
</ul>

# Specs

## 1) Overview
<ul>
<li>We want to be able to add multiple Titles.</li>
<li>We want to be able to add Aliases to Titles, which are short synonyms by which we can refer to that Title.</li>
<li>We want to be able to add a comment to each Title. The comment should be a single string. It should be possible to change the comment.</li>
<li>We want to be able to add Items to Titles. We also want to be able to do this using their Aliases.</li>
<li>We want to be able to find which Title contains a certain Item.</li>
</ul>

## 2) Functionalities
<ul>
<li>(Add/Remove) Title</li>
<li>(Add/Remove) Alias</li>
<li>(Add/Remove/Change) Comment</li>
<li>(Add/Remove/Find) Item</li>
<li>List all Titles</li>
<li>List items from a given Title</li>
</ul>

## 3) CSV format
<p>[Title],[alias1],[alias2],[alias3],[alias4],[...]</p>
<p>[Comment]</p>
<p>[Item1],[Item2],[Item3],[...]</p>
