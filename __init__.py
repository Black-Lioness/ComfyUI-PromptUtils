from .filename_generator import FilenameGenerator
from .keyword_generator import KeywordGenerator

NODE_CLASS_MAPPINGS = {
    "FilenameGenerator": FilenameGenerator, 
    "KeywordGenerator": KeywordGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FilenameGenerator": "Filename Generator 📁", 
    "KeywordGenerator": "Keyword Generator 🔑", 
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
