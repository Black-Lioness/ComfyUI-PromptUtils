#https://github.com/Black-Lioness/ComfyUI-PromptUtils
import random
import json
import os
from typing import Dict, Tuple

_CACHE = {}

def load_json_file(file_name):
    if file_name not in _CACHE:
        file_path = os.path.join(os.path.dirname(__file__), "data", file_name)
        with open(file_path, "r") as file:
            _CACHE[file_name] = json.load(file)
    return _CACHE[file_name]

class KeywordGenerator:
    def __init__(self, seed: int = None):
        self.rng = random.Random(seed)
        
    @classmethod
    def INPUT_TYPES(cls) -> Dict:
        return {
            "optional": {
                "prompt": ("STRING", {"multiline": True, "forceInput": True}),
                "keywords_count": ("INT", {"default": 1, "min": 1, "max": 50, "step": 1}),
                "seed": ("INT", {"default": random.randint(0, 30000), "min": 0, "max": 30000, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Keyword(s)",)
    FUNCTION = "generate_keyword"
    CATEGORY = "Prompt"
        
    def generate_keyword(self, keywords_count: int, prompt: str = "",  seed: int = None) -> str:
        if seed is not None:
            self.rng.seed(seed)
        return ((prompt+" " if prompt != "" else prompt)+", ".join(self.rng.sample(load_json_file("keywords.json"), keywords_count)).lower(),)