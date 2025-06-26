#!/usr/bin/env python3

import re  # We'll use this for sentence counting

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Uses the setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # This regex splits based on punctuation that typically ends a sentence.
        # Handles cases like "!!" or "...", and filters out empty results.
        sentences = re.split(r'[.!?]+', self._value)
        non_empty_sentences = [s for s in sentences if s.strip()]
        return len(non_empty_sentences)
