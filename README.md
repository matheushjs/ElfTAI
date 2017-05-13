# Elf TAI (Title - Alias - Items)

# Environment
<ul>
<li>Python 3</li>
<li>Python packages: termcolor, argparse</li>
<li>Linux Mint 18 (Should work on all Ubuntu Linux'es, though)</li>
</ul>

# Usage
[Example image of basic usage](example.png)
<ul>
<li>git clone https://github.com/matheushjs/ElfTAI</li>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
</ul>

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
