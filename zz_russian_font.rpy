# Use the Cyrillic-capable font bundled with Just Sayori.
# Applying it unconditionally also covers translated text that is shown
# before the mod's persistent language flag has been initialized.
init 100 python:
    _ru_font = "mod_assets/fonts/NotoSansSC-Regular.ttf"
    _ru_font_bold = "mod_assets/fonts/NotoSansSC-Bold.ttf"

    gui.default_font = _ru_font
    gui.name_font = _ru_font_bold
    gui.interface_font = _ru_font
    gui.button_text_font = _ru_font
    gui.choice_button_text_font = _ru_font

    def _ru_set_style_font(style_name, font_name):
        try:
            getattr(style, style_name).font = font_name
        except Exception:
            # Style names differ between Just Sayori builds. A missing
            # optional style must not stop the rest of the font fixes.
            pass

    for _ru_style_name in (
        "default", "edited", "poemgame_text", "button_text", "label_text",
        "choice_button_text", "talk_choice_button_text", "say_dialogue",
        "input_prompt", "input", "radio_button_text", "check_button_text",
        "slider_button_text", "main_menu_text", "quick_button_text",
        "page_label_text", "slot_button_text", "about_text", "history_text",
        "confirm_prompt_text", "confirm_button_text", "skip_text",
        "notify_text", "nvl_dialogue", "nvl_thought", "nvl_button_text",
        "scrollable_menu_button_text",
    ):
        _ru_set_style_font(_ru_style_name, _ru_font)

    for _ru_style_name in (
        "say_label", "navigation_button_text", "game_menu_label_text",
        "pref_label_text", "history_name_text",
    ):
        _ru_set_style_font(_ru_style_name, _ru_font_bold)

    try:
        style.say_dialogue.size = 30
    except Exception:
        pass