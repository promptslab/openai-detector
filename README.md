<h2 align="center">Openai Detector</h2>
<p align="center">
  <p align="center">Open AI classifier for indicating AI-written text
</p>

## Usage



```python

from detector import OpenaiDetector

sentence     = """All children, except one, grow up. They soon know that they will grow up, and the way Wendy knew was this. One day when she was two years old she was playing in a garden, and she plucked another flower and ran with it to her mother. I suppose she must have looked rather delightful, for Mrs. Darling put her hand to her heart and cried, “Oh, why can’t you remain like this for ever!” This was all that passed between them on the subject, but henceforth Wendy knew that she must grow up. You always know after you are two. Two is the beginning of the end. Of course they lived at 14, and until Wendy came her mother was the chief one. She was a lovely lady, with a romantic mind and such a sweet mocking mouth. Her romantic mind was like the tiny boxes, one within the other, that come from the puzzling East, however many you discover there is always one more; and her sweet mocking mouth had one kiss on it that Wendy could never get, though there it was, perfectly conspicuous in the right-hand corner. The way Mr. Darling won her was this: the many gentlemen who had been boys when she was a girl discovered simultaneously that they loved her, and they all ran to her house to propose to her except Mr. Darling, who took a cab and nipped in first, and so he got her. He got all of her, except the innermost box and the kiss. He never knew about the box, and in time he gave up trying for the kiss. Wendy thought Napoleon could have got it, but I can picture him trying, and then going off in a passion, slamming the door. Mr. Darling used to boast to Wendy that her mother not only loved him but respected him. He was one of those deep ones who know about stocks and shares. Of course no one really knows, but he quite seemed to know, and he often said stocks were up and shares were down in a way that would have made any woman respect him."""
bearer_token = 'Bearer sess-abcd1234..'

od = OpenaiDetector(bearer_token)
od.detect(sentence)
                          
                          
### Output

{'unlikely': 96.15870427207666}

```



## TO-DO

- Add all classes labels (total 5 classes from openai)
- add verifier to check if the sentence is 1000 characters long
- automatically detect token from user_name, password


## Web Version

https://openai.com/blog/new-ai-classifier-for-indicating-ai-written-text/
