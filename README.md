# cwf
## Synopsis
Cheating With Friends

This is a python script that uses a word list to figure out the best scoring
word opportunities based on the letters and patterns you provide

## Basic Usage

You get a '?' prompt.

To assign (or reset) the letters you currently have, enter them beginning with an '=' sign like so:
```
? =DQUEZIZ
Letters set to 'dqueziz'

8-letter words:
7-letter words:
   35    quizzed
?
```
The output will give you the best 7 and 8 letter words available with that set, along with the point value for the word.

If you want to add a blank tile to your set, use the '+' by itself:
```
? +   
Letters set to 'dqueziz '

8-letter words:
   33   quizzeRS
7-letter words:
   33    quizzeR
   33    quizzeS
   35    quizzed
?
```
Note the capital letters now in the output.  A capital letter in the word means that the indicated letter must be available for use on the board already, or you must use a blank tile to cover it.

Even if you don't actually have a blank tile to use, adding one to your set may give you better ideas on what you should be looking for re: opportunities on the board.

Like the plus sign, use '-' by itself to remove a blank from your set:
```
? -
Letters set to 'dqueziz'

8-letter words:
7-letter words:
   35    quizzed
?
```
Now that you have the basics, here comes the fun part

## Pattern Matching

You can search for words using patterns based on what is available on the board using a regular expression style query syntax.

In its most simple form, you can look to see if your letters complement another placement on the board.  For example, using the same letter set from above, let's suppose our opponent played the word 'aid'.  You can just type that in at the prompt to find words you can build off of that base word:
```
? aid
    4        aid
    5       aide
    7      aided
   14       qaid
?
```
You can use the '.' as a wildcard to indicate a specific pattern also.  If you have two words in parallel on the board and you know you have an 'a', followed by a space, and then a 'd', you can use 'a.d' as the input pattern:
```
? a.d
    4        aid
    5       aide
    5        add
    7      aided
   14       qaid
? 
```
The characters '^' and '$' can be used to indicate start and end boundaries for the patterns.  Consider these examples:
```
? ^a.d
    4        aid
    5        add
    5       aide
    7      aided
? a.d$
    4        aid
    5        add
   14       qaid
? ^a.d$
    4        aid
    5        add
? 
```
More advanced regular expression patterns are supported as well, but this should get you going.

Sorry, there is no supported way to indicate that particular character slots in pattern descriptions map to bonus multipliers on the board.
