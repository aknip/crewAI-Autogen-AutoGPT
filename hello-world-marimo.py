import marimo

__generated_with = "0.6.13"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        """
        # Hello World

        - Some snippets for marimo
        - Copy and paste...
        """
    )
    return


@app.cell
def __(mo):
    openaikey = mo.ui.text(label="OpenAI Key", kind="password")
    mo.accordion({"Enter your OpenAI key (click to expand)": openaikey})
    return openaikey,


@app.cell
def __(mo):
    mo.md("The cell below is dependent on the input field above. It is executed only, if the value of the input field changes.")
    return


@app.cell
def __(mo, openaikey, os):
    os.environ["OPENAI_API_KEY"] = openaikey.value
    #print(os.environ["OPENAI_API_KEY"])
    mo.md(f"Key: {openaikey.value}") if openaikey.value else None
    return


@app.cell
def __(mo):
    mo.md("The following button appears if the API key input field has been changed.")
    return


@app.cell
def __(mo, openaikey):
    start_button = mo.ui.button(
        label="Caluculate date and time",
        value=0, 
        on_click=lambda count: count + 1
    )

    start_button if openaikey.value else None
    return start_button,


@app.cell
def __(mo, openaikey):
    mo.md("""The following cell is **not** exectued on start. It is executed each time if "Start next cell" is clicked
    """) if openaikey.value else None
    return


@app.cell
def __(datetime, mo, start_button):
    mo.stop(start_button.value == 0, mo.md("-Click button to start...-"))

    my_date_time2 = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    mo.md(
        f"""
        The Time is ** {my_date_time2} **!
        """
    )
    return my_date_time2,


@app.cell
def __(mo, start_button):
    mo.md("""The following cell is **not** exectued on start. It is executed each time if "Start next cell" is clicked
    """) if start_button.value != 0 else None
    return


@app.cell
def __(mo, start_button):
    #form = mo.ui.text(label="Your name").form()

    form = (
        mo.md('''
        **Your form.**

        {name1}

        {date1}
    ''')
        .batch(
            name1=mo.ui.text(label="Name"),
            date1=mo.ui.date(label="Date"),
        )
        .form(show_clear_button=True, bordered=False)
    )
    form if start_button.value != 0 else None
    return form,


@app.cell
def __(form, mo):
    mo.stop(form.value is None, mo.md("Submit the form to continue"))

    mo.md(f"Hello, {form.value['name1']}!")
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import json
    import os
    from getpass import getpass
    import psutil
    import time
    import textwrap

    from datetime import datetime
    return datetime, getpass, json, os, psutil, textwrap, time


@app.cell
def __(mo):
    get_index, set_index = mo.state(0)

    def increment_index():
        set_index(lambda v: v+1)
    return get_index, increment_index, set_index


if __name__ == "__main__":
    app.run()
