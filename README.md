# Elf TAS (Title - Alias - Strings)

# Motivation
<p>Consider the following situation: you have a big set of documents to read, each of which are labeled with the area of knowledge they cover (psychology, mathematics etc). Also, each document has it's ID number.</p>
<p>The Elf TAS program will try to build a generic command-line manager for such situations, where the following are TRUE:</p>
<ul>
<li>There exists a big set of objects (documents in this case), and we want to record which of these objects have been processed (in this case, read).</li>
<li>There exists a reduced number of titles (labels, in this case), where each title characterizes a set of objects.</li>
<li>Each object is characterized by only 1 Title.</li>
<li>Each object can be described by a string (the ID in this case)</li>
</ul>

# Specs

## 1) Overview
<ul>
<li>We want to be able to add multiple Titles.</li>
<li>We want to be able to add Aliases to Titles, which are short synonyms by which we can refer to that Title.</li>
<li>We want to be able to add a comment to each Title. The comment should be a single string. It should be possible to change the comment.</li>
<li>We want to be able to add Strings to Titles. We also want to be able to do this using their Aliases.</li>
<li>We want to be able to find which Title contains a certain String.</li>
</ul>

## 2) Functionalities
<ul>
<li>(Add/Remove) Title</li>
<li>(Add/Remove) Alias</li>
<li>(Add/Remove/Change) Comment</li>
<li>(Add/Remove/Find) String</li>
<li>List all Titles</li>
<li>List strings from a given Title</li>
</ul>

## 3) CSV format
<p>[Title],[alias1],[alias2],[alias3],[alias4],[...]</p>
<p>[Comment]</p>
<p>[String1],[String2],[String3],[...]</p>
