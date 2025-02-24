from nicegui import ui


def main():
    ui.label('Welcome to my NiceGUI application').classes(
        'text-h3 text-center')

    with ui.row().classes('w-full justify-center'):
        ui.button('Click me!', on_click=lambda: ui.notify('Button clicked!'))


if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(title='My Application', port=8080)
