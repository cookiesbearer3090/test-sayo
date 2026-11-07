init 4 python:
    _ru_poem_reg_original = reg_poem_trans
    _ru_poem_reg_code = getattr(_ru_poem_reg_original, "__code__", None)

    if _ru_poem_reg_code is not None and _ru_poem_reg_code.co_argcount == 2:
        def _ru_poem_reg_compat(original_poem_name, translated_poem, lang=None):
            previous_language = persistent.language
            if lang is not None:
                persistent.language = lang
            try:
                return _ru_poem_reg_original(original_poem_name, translated_poem)
            finally:
                persistent.language = previous_language

        reg_poem_trans = _ru_poem_reg_compat