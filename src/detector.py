import requests
import numpy as np


class OpenaiDetector:

    def __init__(self, token):

        self.header = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
            'Authorization': token,
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://platform.openai.com',
            'Referer': 'https://platform.openai.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        self.possible_classes = ['very unlikely', 'unlikely', 'unclear if it is', 'possibly', 'likely']
        self.class_max = [10, 45, 90, 98, 99]

    def detect(self, text, all_probs=False):
        data = {
            'prompt': text + "».\n<|disc_score|>",
            'max_tokens': 1,
            'temperature': 1,
            'top_p': 1,
            'n': 1,
            'logprobs': 5,
            'stop': '\n',
            'stream': False,
            'model': 'model-detect-v2',
        }

        response = requests.post('https://api.openai.com/v1/completions', headers=self.header, json=data)
        if response.status_code == 200:
            choices = response.json()['choices'][0]
            logprobs = choices['logprobs']['top_logprobs'][0]
            probs = {key: 100 * np.e ** value for key, value in logprobs.items()}
            key_prob = probs['"']
            if self.class_max[0] < key_prob < self.class_max[len(self.class_max) - 1]:
                val = max(i for i in self.class_max if i < key_prob)
                class_label = self.possible_classes[self.class_max.index(val)]
            elif self.class_max[0] > key_prob:
                class_label = self.possible_classes[0]
            else:
                class_label = self.possible_classes[len(self.possible_classes) - 1]
            top_prob = {'Class': class_label, 'AI-Generated Probability': key_prob}
            if all_probs:
                return probs, top_prob
            return top_prob
        return "Check prompt, Length of sentence it should be more than 1,000 characters"
