import flet as ft

# Mapping of letters to digits
LETTER_TO_DIGIT = {
    **dict.fromkeys("OUY", "3"),
    **dict.fromkeys("FGHJ", "4"),
    **dict.fromkeys("AI", "2"),
    **dict.fromkeys("KLMNPQR", "7"),
    **dict.fromkeys("E", "1"),
    **dict.fromkeys("BCDSTVWXZ", "9"),
}


def transcribe(word):
    word = word.upper()  # Ensure uppercase
    return "".join(
        LETTER_TO_DIGIT.get(char, "0") for char in word
    )  # Default to "0" if no match


def main(page: ft.Page):
    page.title = "Word to Number Transcriber"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_field = ft.TextField(label="Enter a 4-letter word", width=200, max_length=4)
    result_text = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    def on_submit(e):
        word = input_field.value.strip()
        if len(word) == 4 and word.isalpha():
            result_text.value = transcribe(word)
        else:
            result_text.value = "Invalid input"
        page.update()

    submit_button = ft.ElevatedButton(text="Convert", on_click=on_submit)

    page.add(
        ft.Column(
            [input_field, submit_button, result_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
