# BFPI
BFPI: Exactly what it sounds like

---

#What is bf? 

https://en.wikipedia.org/wiki/Brainfuck

(tl,dr;)

You can run bf in this bf+ interpreter because we can translate bf to bf+. 

---

#What is bf+? 
Differences: infinite cells, lists in cells, negative cells, more loops, etc. 

There are 37 key phrases in bf+. Because bf+ can do everything bf can, it is turing-complete: 

(There are also 37 key words, not including 21 cap letters except 'P', 'F', 'O', 'Q', and 'I'). 

37+21=58

bf | bf+
---|---
\+ | +
\- | -
\, | iscwv (only case where bf+ is more complex)
\. | o
\> | d
\< | a
[CODE] | [CODEl]

Like bf, bf+ ignores non-keyword phrases. 

NOTE: All cap letters after 'p', 'P', 'f', or 'F' are also keywords. 

Character, Meaning, Type, And If they have been changed dramatically from bf

\+                       :      add current cell by 1 if current cell is not a list, else raise an error|Modify|No

\-                       :      subtract current cell by 1 if current cell is not a list, else raise an error|Modify| No

0                       :      makes current cell value 0|Modify|Sort of, same as [-] in bf but original ver won't work with neg values

a                       :      move 1 cell to the left; if already at position 0 raise an error|Move|Not really, same as < in bf

d                       :      move 1 cell to the right|Move|Not really, same as > in bf

s                       :      if current cell is list, go into list at index 0; else make it a list and go into list at index 0. Technically if it is near 100th recursion will raise recursion error in python|Move|Yes

w                       :      if current cell is in list, go to cell that contain the list; else raise an error|Move|Yes

i                       :      input the input as their ord() values in a list, stores the list to current cell|I/O|Sort of, similar to , in bf but support more chars; bf , is equivalent to bf+ iscwv, only the later being more general

I                       :      input a number and store it to cell|I/O|Sort of, but accessible in bf using long programs, not including neg ints. 

o                       :      output the char of ASCII value of cell if the cell is of type value (neg or bad values raise errors), else output the string containing all chars of ASCII values in the string (for simplification doesn't include '0' values)|I/O|Sort of, first usage equivalent to . in bf but second impossible (I think)

O                       :      output the value of the cell directly if it is of type value, else raise an error|I/O|Sort of, but accessible in bf using long programs, not including neg ints. 

c                       :      copy the value of cell (int or list)|Copy Paste|Yes, as one of the strongest features in bf+ (although pos int or 0 copy and paste is possible in bf, neg int is not do-able and thus lists with them not do-able too)

v                       :      paste the value of cell (int or list)|Copy Paste|Yes, as one of the strongest features in bf+ (although pos int or 0 copy and paste is possible in bf, neg int is not do-able and thus lists with them not do-able too)

p                       :      make a portal. pH make a portal named H, etc. Technically should only have 1-char caps except 'P' as portal name|Portal|Yes, as one of the strongest features in bf+

P                       :      go to a portal. PH go to the portal named H, etc.; if portal undefined raise an error|Portal|Yes, as one of the strongest features in bf+

fNCODEf                 :      make function named 'N' with definition CODE; there is no reason to stack this and such stacking will cause errors|Function|Yes, as one of the strongest features in bf+

FN                      :      call function named 'N'; if function undefined raise an error|Function|Yes, as one of the strongest features in bf+

\(CODE\)                :      execute code inside if current cell is 0|Loop|Yes, as goes all the loop features except \[CODEl\]

\[CODE\]                :      execute code inside if current cell is not 0|Loop|Yes, as goes all the loop features except \[CODEl\]

\{CODE\}                :      execute code inside if current cell is > 0|Loop|Yes, as goes all the loop features except \[CODEl\]

\<CODE\>                :      execute code inside if current cell is < 0|Loop|Yes, as goes all the loop features except \[CODEl\]

\,CODE\;                :      execute code inside if current cell is >= 0|Loop|Yes, as goes all the loop features except \[CODEl\]

\.CODE\:                :      execute code inside if current cell is <=0|Loop|Yes, as goes all the loop features except \[CODEl\]

\/CODE\\                :      execute code inside|Loop|Yes, as goes all the loop features except \[CODEl\]

\(CODEl\)               :      repeatly execute code inside as long as current cell remains 0 (position of 'current cell' aforementioned might change due to CODE inside) (code doesn't include character 'l', the letter in jk'l'mn)|Loop|Yes, as goes all the loop features except \[CODEl\]

\[CODEl\]               :      repeatly execute code inside as long as current cell remains not 0 (position of 'current cell' aforementioned might change due to CODE inside) (code doesn't include character 'l', the letter in jk'l'mn)|Loop|No, it is the only loop in bf: the [] loop

\{CODEl\}               :      repeatly execute code inside as long as current cell remains > 0 (position of 'current cell' aforementioned might change due to CODE inside) (code doesn't include character 'l', the letter in jk'l'mn)|Loop|Yes, as goes all the loop features except \[CODEl\]

\<CODEl\>               :      repeatly execute code inside as long as current cell remains < 0 (position of 'current cell' aforementioned might change due to CODE inside) (code doesn't include character 'l', the letter in jk'l'mn)|Loop|Yes, as goes all the loop features except \[CODEl\]

\,CODEl\;               :      repeatly execute code inside as long as current cell remains >= 0 (position of 'current cell' aforementioned might change due to CODE inside) (code doesn't include character 'l', the letter in jk'l'mn)|Loop|Yes, as goes all the loop features except \[CODEl\]

\.CODEl\:               :      repeatly execute code inside as long as current cell remains <=0 (position of 'current cell' aforementioned might change due to CODE inside) (code doesn't include character 'l', the letter in jk'l'mn)|Loop|Yes, as goes all the loop features except \[CODEl\]

\/CODEl\\               :      repeatly execute code inside (code doesn't include character 'l', the letter in jk'l'mn)|Loop|Yes, as goes all the loop features except \[CODEl\]

\#CODE\#                :      ignore code inside, used for commenting. make sure pairing symbols pair. DO NOT STACK THIS|Comment|Yes, as it is not needed in bf

initial loop comment.   :      supported: [], {}, <>, [l], {l}, \<l\>, but make sure pairing symbols pair|Comment|Sort of, as only [l] is supported in bf

q                       :      quit function

Q                       :      quit entire program

'                       :      print character \t

"                       :      print character \n

|                       :      break 2 loops

_                       :      restart 2nd loop (but still checks condition before execution)

# 119 lines!!! GOD!!! 

















































