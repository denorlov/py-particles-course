# Do not change the class name.
class Metadata:
    # Your discord name and tag, so that we can award you the points
    # in the leaderboards.
    discord_tag = "MyUsename#0000"

    # The name that should be diplayed below your entry in the menu.
    display_name = "Base setup"

    # All the challenges that you think you have acheived.
    # Uncomment each one that you have done and not only the highest.
    achievements = [
        # "Casual",
        # "Ambitious",
        # "Adventurous",
    ]

    # The lowest python version on which your code can run.
    # It is specified as a tuple, so (3, 7) mean python 3.7
    # If you don't know how retro-compatible your code is,
    # set this to your python version.
    # In order to have the most people to run your entry, try to
    # keep the minimum version as low as possible (ie. don't use
    # match, := etc...
    min_python_version = (3, 6)

    # A list of all the modules that one should install
    # to run your entry. Each string is what you would pass to
    # import.
    # Each line will be passed to pip install if needed, but you cannot
    # (yet?) specify version constraints. Modules that have a different name
    # on install and import are also not supported. If you need it,
    # please open an issue on the GitHub.
    dependencies = [
        # "numpy",
    ]
