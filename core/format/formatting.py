class coloration:

    def __init__(self):

        self.red = "\033[31;1m"
        # green
        self.green = "\033[32;1m"
        # cyan
        self.cyan = "\033[36;1m"
        # purple
        self.purple = "\033[95;1m"
        # end color
        self.end = "\033[0m"

class notifications:

    def __init__(self):

        colors = coloration()

        self.notify = f'{colors.cyan}[*]{colors.end}'

        self.warning = f'{colors.red}[!]{colors.end}'
