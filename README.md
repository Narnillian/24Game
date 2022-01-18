# 24Game
24 Game solution finder

Made with GitHub and Replit

It is not my fault Replit uses Poetry and not Pip

## About the game
24 game is a mathimatical game where you try to use 4 integers to get to 24. You start with a set such as `[2,4,6,7]`. You use each number exactly once and can use any of the four arithmetical operators (`+`,`-`,`*`,`/`) as many times as you wish to get to 24. In this example, one solution would be `(2 * 7) + (6 + 4)`.  Each number is used once, but `+` is used twice. `-` and `/


## This is not finished!
It will probably be changed pretty drastically.


## About the code
Imported packages: `random`, `time`, `replit` (if available - mostly just for me working in Replit)
This script currently uses a randomizer to get every possible list with the four numbers. You end up with 24  lists inside of a larger list. 24 here has nothing to do with the game. That's the amount of different lists you can have of 4 elements without repeating numbers.

After getting all permutations of the list, the script finds 64 lists of the operators and adds them to a similar list.   64 is the maximum number of different combinations of 3  elements you can have. These lists can use each element more than once.

Once the script has both lists, we end the program. Like I said, this is unfinished.

## About Replit
Replit is an online IDE where you can code in many *many* languages. I have integrated it with GitHub so that I can commit directly from Replit. 

## What I could do instead of the current implementation
- Subtract/Divide/etc. 24 by each number then see if that works.
  - Probably also a bad implementation