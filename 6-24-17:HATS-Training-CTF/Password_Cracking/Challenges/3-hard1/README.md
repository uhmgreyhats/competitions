# hard1
HPD obtained password dumps storing the criminal's passwords. It appears that they have an interest in Grey's Anatomy episodes followed by 3 digits.

## Questions
1. **7878719df2d7aae0294bc31e5e52e4a0**
2. **9982fda6ddefe68ecd0f246826848ab2**
3. **c2775ebdb0aec52243f70666bfa2696e**
4. **20e6dc9a8d3d6c7e5b148c95253f3673**
5. **608c0d8288afcc6b3e9d7982ffe23437**

## Steps
1. Create a word list of Grey's Anatomy episodes. This can be done by parsing through https://en.wikipedia.org/wiki/List_of_Grey%27s_Anatomy_episodes
2. With the word list, hash each episode followed by 000-999
3. If the hashes were not found, try variations of the episode names including lowercase, no spaces, or a combination of both
