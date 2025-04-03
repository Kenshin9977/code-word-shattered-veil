import flet as ft

# Predefined mappings identified by a key letter
ARRANGEMENTS = {
    "E": {"E": 1, "AI": 2, "OUY": 3, "FGHJ": 4, "KLMNPQR": 7, "BCDSTVWXZ": 9},
    "S": {"S": 1, "QX": 2, "JKZ": 3, "AIOUY": 5, "BCDEFGH": 7, "LMNPRTVW": 8},
    "NI": {"M": 1, "NI": 2, "ECVB": 4, "XYZWK": 5, "QPGAFR": 6, "OSTUHJLD": 7},
    "XYZ": {"M": 1, "XYZ": 3, "JKQU": 4, "BCDEF": 5, "GHILNO": 6, "APRSTVW": 7},
}


def generate_mapping(arrangement_key):
    """Retrieve the correct mapping based on user-selected arrangement key."""
    if arrangement_key not in ARRANGEMENTS:
        return None

    mapping = {}
    for group, digit in ARRANGEMENTS[arrangement_key].items():
        for char in group:
            mapping[char] = str(digit)

    return mapping


def transcribe(word, arrangement_key):
    """Convert word to digits using the selected arrangement mapping."""
    letter_map = generate_mapping(arrangement_key)
    if not letter_map:
        return "Invalid key"

    return "".join(letter_map.get(char, "0") for char in word.upper())  # Default to "0"


def on_input_change(e, input_field, arrangement_field, result_text, page):
    """Handle dynamic update when input field or arrangement is changed."""
    word = input_field.value.strip().upper()
    arrangement_key = arrangement_field.value

    # If no arrangement is selected (empty), show all codes
    if not arrangement_key:
        all_codes = []
        if len(word) == 4 and word.isalpha():
            for k in ARRANGEMENTS.keys():
                all_codes.append(transcribe(word, k))
            result_text.value = "\n".join(all_codes)
        else:
            result_text.value = "Invalid input"
    else:
        # If arrangement is selected, use it to transcribe the word
        arrangement_key = arrangement_key.strip().upper()
        if len(word) == 4 and word.isalpha():
            result_text.value = transcribe(word, arrangement_key)
        else:
            result_text.value = "Invalid input"

    page.update()


def main(page: ft.Page):
    page.title = "Word to Number Transcriber"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_field = ft.Dropdown(
        label="Word",
        options=[ft.DropdownOption(text=w) for w in ["CRAB", "MOTH", "WORM", "YETI"]],
        width=200,
    )

    # Add the empty option for the arrangement key dropdown
    arrangement_field = ft.Dropdown(
        label="Letter group",
        options=[ft.DropdownOption(text="None")]
        + [ft.DropdownOption(text=key) for key in ARRANGEMENTS.keys()],
        width=200,
    )

    result_text = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    # Trigger the conversion or display all codes dynamically
    input_field.on_change = lambda e: on_input_change(
        e, input_field, arrangement_field, result_text, page
    )
    arrangement_field.on_change = lambda e: on_input_change(
        e, input_field, arrangement_field, result_text, page
    )

    page.add(
        ft.Column(
            [input_field, arrangement_field, result_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)
