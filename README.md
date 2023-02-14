<h2 align="center">Openai Detector</h2>
<p align="center">
  <p align="center">Open AI classifier for indicating AI-written text
</p>


 <h4 align="center">
  <a href="https://github.com/promptslab/openai-detector/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="openai-detector is released under the Apache 2.0 license." />
  </a>
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="http://makeapullrequest.com" />
  </a>
  <a href="https://discord.gg/m88xfYMbK6">
    <img src="https://img.shields.io/badge/Discord-Community-orange" alt="Community" />
  </a>
  <a href="https://colab.research.google.com/drive/1f4YG9stX9aHmsmh6ZhzjekJU4X4BIynO?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="colab" />
  </a>
</h4>

## Usage



```python

from detector import OpenaiDetector

sentence     = """All children, except one, grow up. They soon know that they will grow up, and the way Wendy knew was this. One day when she was two years old she was playing in a garden, and she plucked another flower and ran with it to her mother. I suppose she must have looked rather delightful, for Mrs. Darling put her hand to her heart and cried, “Oh, why can’t you remain like this for ever!” This was all that passed between them on the subject, but henceforth Wendy knew that she must grow up. You always know after you are two. Two is the beginning of the end. Of course they lived at 14, and until Wendy came her mother was the chief one. She was a lovely lady, with a romantic mind and such a sweet mocking mouth. Her romantic mind was like the tiny boxes, one within the other, that come from the puzzling East, however many you discover there is always one more; and her sweet mocking mouth had one kiss on it that Wendy could never get, though there it was, perfectly conspicuous in the right-hand corner. The way Mr. Darling won her was this: the many gentlemen who had been boys when she was a girl discovered simultaneously that they loved her, and they all ran to her house to propose to her except Mr. Darling, who took a cab and nipped in first, and so he got her. He got all of her, except the innermost box and the kiss. He never knew about the box, and in time he gave up trying for the kiss. Wendy thought Napoleon could have got it, but I can picture him trying, and then going off in a passion, slamming the door. Mr. Darling used to boast to Wendy that her mother not only loved him but respected him. He was one of those deep ones who know about stocks and shares. Of course no one really knows, but he quite seemed to know, and he often said stocks were up and shares were down in a way that would have made any woman respect him."""
bearer_token = 'Bearer sess-abcd1234..'

od = OpenaiDetector(bearer_token)
response = od.detect(sentence)
print(response)                          
                          
### Output

{"output"          : "The classifier considers the text to be very unlikely AI-generated.",
"Confidence score" : 96.15870427207666}

```

## Run on colab
  <a href="https://colab.research.google.com/drive/1f4YG9stX9aHmsmh6ZhzjekJU4X4BIynO?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="colab" />
  </a>

## Community

If you are interested in Prompt-Engineering, LLMs, ChatGPT and other latest research discussions, please consider joining PromptsLab

<a href="https://discord.gg/m88xfYMbK6">
<img alt="Join us on Discord" src="https://img.shields.io/discord/1069129502472556587?color=5865F2&logo=discord&logoColor=white"></a>

## Steps to get Bearer token from chrome


- Go to https://platform.openai.com/ai-text-classifier
- Hit F12 to access the Developer tools
- Select the Network Tab
- Select nearly any POST Operation (paste text into detection box and click on submit)
- Find your current Bearer token in the Request Headers

Here is an example

<div align="center">
<img width="600px" src="https://raw.githubusercontent.com/promptslab/openai-detector/main/extra/bearer_token.gif">
</div>


## TO-DO

- Add all classes labels (total 5 classes from openai) ✅
- add verifier to check if the sentence is 1000 characters long
- automatically detect token from user_name, password


## Web Version

https://openai.com/blog/new-ai-classifier-for-indicating-ai-written-text/
