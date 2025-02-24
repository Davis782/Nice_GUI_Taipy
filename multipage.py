from taipy.gui import Gui


def submit_form(state):
    print(f"Name: {state.name}, Email: {state.email}")


def on_page_change(state, action, page):
    state.navigate(page)


# Initialize state variables
name = ""
email = ""
pages_list = ["page1", "page2"]
current_page = "page1"

# Create page content using Taipy's markdown syntax
form_template = """
# Enter your details below

<|{name}|input|label=Name|>
<|{email}|input|label=Email|>
<|Submit|button|on_click=submit_form|>
"""

# Add dropdown navigation
nav_template = """
<|{current_page}|selector|values={pages_list}|on_change=on_page_change|>
"""

# Define multiple pages
page1 = """
# Page 1
""" + nav_template + form_template

page2 = """
# Page 2
""" + nav_template + form_template

# Create pages dictionary
pages = {
    "/": page1,
    "page1": page1,
    "page2": page2
}

# Create and run the GUI
gui = Gui(pages=pages)

if __name__ == "__main__":
    gui.run(title="Multi-Page App", port=8088)
