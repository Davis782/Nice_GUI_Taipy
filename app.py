# from nicegui import ui


# def main():
#     ui.label('Welcome to my NiceGUI application').classes(
#         'text-h3 text-center')

#     with ui.row().classes('w-full justify-center'):
#         ui.button('Click me!', on_click=lambda: ui.notify('Button clicked!'))


# if __name__ in {"__main__", "__mp_main__"}:
#     main()
#     ui.run(title='My Application', port=8082)
from taipy.gui import Gui


def submit_form(state):
    print(f"Name: {state.name}, Email: {state.email}")


# Initialize state variables
name = ""
email = ""

# Create page content using Taipy's markdown syntax
page = """
# Enter your details below

<|{name}|input|label=Name|>
<|{email}|input|label=Email|>
<|Submit|button|on_click=submit_form|>
"""

# Create and run the GUI
gui = Gui(page)

if __name__ == "__main__":
    gui.run(title='Simple Form', port=8086)
