## Status of Submission
The Java and Python code works perfectly fine. The C code compiles and runs perfectly, but the size it prints is incorrect. It appears the struct property I am using as the size isn't actually the size. I tried manually going over every character in a file to count its size byte by byte, but my the resulting executable didn't appear to do much. Perhaps it was just taking too long to count as there were a lot of characters to count. Either way, I removed that code and I decided to use the struct value instead as I ran out of time to find the correct solution.

---

## Question 1  
#### Java
I found Java to be the easiest to work with because i have been familiar with the language from previous classes and I knew to look in the documentation for an object that allowed me to get a list of the entries in a directory. After finding the object, it was just a matter of going through the documentation to get the right methods. I had some trouble debugging why the program wasn't working for the second level of test subdirectories I made; but I was able to figure out that it was because the program couldn't figure out their path with just a name, so I added the absolute path whenever calling my function to solve the problem.

#### Python
Python was surprisingly easy to figure out considering my only meaningful exposure to the language was the workshop I attended over the weekend. The syntax was much more compact than Java's syntax since it doesn't force writing the program in OOP. I had to keep looking over the correct syntax from the notes I took during the workshop, but it was mostly easy I would say. Like Java, I did have some difficulties figuring out why I couldn't correctly identify the subdirectories, but I came to the same conclusion of including the absolute path.

#### C
C was by far the hardest to  implement despite me knowing this language for the longest out of the other two. Compared the other two, there are very few high level function that allowed me to just get the answer. All of the functions available were very primitive and required me to build on top of them to get to where I wanted to go. For example, in Java and Python, I could simply concatenate the two strings to get the absolute path for a subdirectory. In C I had to manually allocate memory for a string, copy the path into it, concatenate the "/", concatenate the subdirectory name, and finally free the allocated memory once I'm done. What was just simply adding two strings with a + sign turned into 5 lines of code. This is what makes C difficult to use, but it is also what makes it appealing as it doesn't come with all the abstracted functions that will only take space if you don't need them. C shines in cases where resources are very limited and every byte, and microsecond counts. 

---

## Question 2
Recursion was a very useful tool during this lab, but it isn't strictly necessary to completing it. One could have used a loop to effectively  achieve the same result, though with admittedly more lines of code to setup the loop and make sure the logic is sound. If we detect a directory, we would need to manually keep track of returning to the parent directory rather than just relying on the call stack to do it for us. Another, even less efficient method in my opinion, is making a function for the sole purpose of summing the size of files. We manually keep track of the directories in the main function (or an equivalent) and call the file sum function on the files of each of those directories.