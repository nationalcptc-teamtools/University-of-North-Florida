import json
from rich.console import Console

# ╠ ╣ ═ ╔ ╗ ╚ ╝ ║

console = Console()

def header() -> None:
    console.print(
        """
      [red]░▒▒▒▒                   
     ░▒▒▒▒░ ░░░               
      ▒▒▒▒▒▒▒[/red][white]▓[red]▒               
        ▒▒[/red]▓██▓▒▓▒▒▒           
     [yellow1]░ [white]▒▒▒▓█▓▓████░           
[yellow1]▒▒▒▓▒▓  [white]▒▒▒▓███▓▒        [yellow1]▒    
    [yellow1]▒▓▒   [white]▒ ▓█▓        [yellow1]░▓▒░░  
     [yellow1]▒▓▒    ░▒▒▒▒      ░▓▒▓▒░▓
       [yellow1]▒▓▓▒▓████▓▓▓▒▒░▒▓░▒     
            [yellow1]▒████▓░▒▒                                    
            [yellow1]▒▓██▓█▓▒                              [green]██████   ████   ████    ████
             [yellow1]▒▓█▓▓█░     [white] ████   ███    ███ ███     [green]██    ██  ██  ██ ██  ██ ██
           [yellow1]▒▒███▓▓▓▓▒    [white]██     ██ ██  ██ ███ ██    [green]██    ██  ██  ██  ████  ██
           [yellow1]▒▓██▓▓▓██░    [white] ███   █████  ██  █  ██    [green]██    ██████  ██   ██   ██
         [yellow1]▓▓▒▓▓▓▓▒▓▓░     [white]   ██  ██ ██  ██     ██    [green]██    ██  ██  ██        ██
          [white]▒▓▒  ▓░▒  [white]     ████   ██ ██  ██     ██    [green]██    ██  ██  ██        ██
       [white]▒▓█▓█    ▓▓▒                               [green]██████  ██  ██  ██        ██
                  [white]▒▒▓▓
        """,
        highlight=False
    )



class Format:
    BORDER_FORMAT = "[cyan]║[/cyan] {}"

    def __init__(self, border: bool):
        self.__ls_string = self.BORDER_FORMAT.format(
            "{:<11} {:<15} {:<6} {:<4}  {}") if border else "{:<11} {:<15} {:<6} {:<4}  {}"
        self.border = border

    @staticmethod
    def print_title(text: str) -> None:
        length = 130
        top = f"[cyan]╔{'═' * (len(text) + 2)}╗"
        middle = f"[cyan]╣ [bold green]{text} [cyan]╠"
        bottom = f"[cyan]╚{'═' * (len(text) + 2)}╝"
        console.print(f"\n{top: ^{length - 18}}\n{middle:═^{length}}\n{bottom: ^{length - 18}}")

    @staticmethod
    def print_title1(text: str) -> None:
        console.print(f"\n[cyan]╔══════════╣ [bold magenta]{text}", highlight=False)

    def print_title2(self, text: str) -> None:
        if self.border:
            console.print(f"[cyan]║\n╠═════╣ [yellow]{text}", highlight=False)
        else:
            console.print(f"\n[cyan]═════╣ [yellow]{text}", highlight=False)

    def print_title3(self, text: str) -> None:
        if self.border:
            console.print(f"[cyan]║\n╠══╣ [grey62]{text}", highlight=False)
        else:
            console.print(f"[cyan]══╣ [grey62]{text}", highlight=False)

    def print_info(self, text: str) -> None:
        if self.border:
            console.print(f"[cyan]║\n║ [yellow][+] [green]{text}\n[cyan]║[/cyan]")
        else:
            console.print(f"\n[yellow][+] [green]{text}\n")

    def print_data(self, data: str | dict) -> None:
        if isinstance(data, dict):
            data = json.dumps(data, indent=4, default=str)
        if self.border:
            formatted_data = "\n".join([self.BORDER_FORMAT.format(line) for line in data.split("\n")])
            console.print(formatted_data, highlight=False)
        else:
            console.print(data, highlight=False)

    def print_error(self, error: str, border: bool = False) -> None:
        if self.border and border:
            formatted_error = self.BORDER_FORMAT.format(f"[red]{error}")
            console.print(formatted_error)
        else:
            console.print(f"[red]{error}")


if __name__ == '__main__':
    pass
