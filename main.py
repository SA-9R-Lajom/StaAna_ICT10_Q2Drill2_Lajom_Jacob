from pyscript import document

grade7 = {"Ava Santos", "Liam Reyes", "Mia Cruz"}
grade8 = {"Noah Garcia", "Emma Torres", "Lucas Flores"}
grade9 = {"Sophia Ramos", "Ethan Mendoza", "Isabella Diaz"}
grade10 = {"Daniel Castillo", "Olivia Navarro", "Gabriel Lim"}

master_set = grade7 | grade8 | grade9 | grade10


def update_results():
    """Display all members in alphabetical order and update the count."""
    sorted_members = sorted(master_set, key=str.casefold)

    member_html = "".join(
        f'<li class="member-item">'
        f'<span class="member-icon">{name[0]}</span>'
        f'<span class="member-name">{name}</span>'
        f'</li>'
        for name in sorted_members
    )

    document.getElementById("member-output").innerHTML = (
        f'<ul class="member-list">{member_html}</ul>'
    )

    document.getElementById("total-count").innerText = str(
        len(master_set)
    )


def add_member(event):
    """Validate input and add a new member if they do not already exist."""
    first_name = (
        document.getElementById("first-name").value.strip().title()
    )
    last_name = (
        document.getElementById("last-name").value.strip().title()
    )

    message_element = document.getElementById("message")

    if not first_name or not last_name:
        message_element.innerHTML = (
            '<span class="text-danger fw-semibold">'
            'Please enter both a first name and a last name.'
            '</span>'
        )
        return

    full_name = f"{first_name} {last_name}"

    if full_name in master_set:
        message_element.innerHTML = (
            '<span class="text-warning fw-semibold">'
            f'{full_name} is already a member.'
            '</span>'
        )
        return

    master_set.add(full_name)

    message_element.innerHTML = (
        '<span class="text-success fw-semibold">'
        f'✓ {full_name} has been added successfully!'
        '</span>'
    )

    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""

    update_results()

update_results()

