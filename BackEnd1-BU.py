from taipy.gui import Gui, State, notify
from taipy import Core

# Initialize data and state


class AppState:
    def __init__(self):
        self.counter = 0
        self.message = "Hello from Taipy Backend!"

# Create callback functions


def increment_counter(state: State):
    state.counter += 1
    notify(state, 'success', f'Counter incremented to {state.counter}')


# Define the page content
page = """
<|layout|columns=1 gap=30px|
<|part|class_name=text-center|
# {message}

Current Count: {counter}

<|button|on_action=increment_counter|text="Increment Counter"|>
|>
|>
"""

# Initialize the state and GUI
state = AppState()
gui = Gui(page)

if __name__ == '__main__':
    Core().run()
    gui.run(port=8086, title="Taipy Backend")
