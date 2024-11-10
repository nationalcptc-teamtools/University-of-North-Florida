import json

from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion, CompleteEvent
from prompt_toolkit.document import Document
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.progress import Progress, BarColumn, TransferSpeedColumn, DownloadColumn
from rich.prompt import Prompt
from main import File

# https://github.com/carlospolop/PEASS-ng/blob/master/linPEAS/builder/linpeas_parts/linpeas_base.sh
# ╠ ╣ ═ ╔ ╗ ╚ ╝ ║

console = Console()
style = Style.from_dict({
            'border': 'ansicyan'
        })
BLACKLISTED_EXTENSIONS = [
    "ram", "3gp", "3gpp", "3g2", "3gpp2", "aac", "adts", "loas", "ass", "au",
    "snd", "mp3", "mp2", "opus", "aif", "aifc", "aiff", "ra", "wav", "avif",
    "bmp", "gif", "ief", "jpg", "jpe", "jpeg", "heic", "heif", "png", "svg",
    "tiff", "tif", "ico", "ras", "pnm", "pbm", "pgm", "ppm", "rgb", "xbm",
    "xpm", "xwd", "mp4", "mpeg", "m1v", "mpa", "mpe", "mpg", "mov", "qt",
    "webm", "avi", "movie", "mkv", "exe", "dll",
]


class MyCompleter(Completer):
    def __init__(self, completions: list[str]):
        """
        Initialize the MyCompleter instance.

        :param completions: List of strings to prompt user
        """
        self.completions = completions

    def get_completions(self, document: Document, complete_event: CompleteEvent):
        """
        Generate completion suggestions based on the input document and complete event.

        :param document: Document object
        :param complete_event: Complete object
        """
        word_before_cursor = document.get_word_before_cursor()
        word_before_cursor_lower = word_before_cursor.lower()
        matches = [c for c in self.completions if c.lower().startswith(word_before_cursor_lower)]
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))


def download_prompt(readable_file_names: list[str]) -> list[str] | None:
    """
    Prompts a user asking if they would like to download any readable files in an S3 bucket.
    If the answer is "y", a prompt with auto-completion will appear.

    :param readable_file_names: List of file/folder names to prompt for auto-completion.
    :return: List of user's arguments if any, None otherwise
    """
    download_input = Prompt.ask("[cyan]║\n║[/cyan] Would you like to download any of the readable files?", choices=["y", "n"],
                                default="n", console=console)

    if download_input == 'y':
        files = prompt([('class:border', '║'), ('', ' File(s): ')], completer=MyCompleter(readable_file_names), style=style)
        console.print(f'[cyan]║')
        return files.split()
    else:
        return


def get_progress_bar() -> Progress:
    """
    Creates and returns a stylized progress bar to be used for a file download.

    :return: Stylized progress bar
    """
    progress = Progress(
        "[cyan]║[/cyan] [progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "•",
        DownloadColumn(),
        console=console
    )

    return progress


class Format:
    BORDER_FORMAT = "[cyan]║[/cyan] {}"

    def __init__(self, border: bool):
        self.__ls_string = self.BORDER_FORMAT.format(
            "{:<11} {:<15} {:<6} {:<4}  {}") if border else "{:<11} {:<15} {:<6} {:<4}  {}"
        self.border = border

    @staticmethod
    def print_title(text: str) -> None:
        length = 130
        top = f'[cyan]╔{"═" * (len(text) + 2)}╗'
        middle = f'[cyan]╣ [bold green]{text} [cyan]╠'
        bottom = f'[cyan]╚{"═" * (len(text) + 2)}╝'
        console.print(f'\n{top: ^{length - 18}}\n{middle:═^{length}}\n{bottom: ^{length - 18}}')

    @staticmethod
    def print_title1(text: str) -> None:
        console.print(f'\n[cyan]╔══════════╣ [bold magenta]{text}', highlight=False)

    def print_title2(self, text: str) -> None:
        if self.border:
            console.print(f'[cyan]║\n╠═════╣ [yellow]{text}', highlight=False)
        else:
            console.print(f'\n[cyan]═════╣ [yellow]{text}', highlight=False)

    def print_title3(self, text: str) -> None:
        if self.border:
            console.print(f'[cyan]║\n╠══╣ [grey62]{text}', highlight=False)
        else:
            console.print(f'[cyan]══╣ [grey62]{text}', highlight=False)

    def print_info(self, text: str) -> None:
        if self.border:
            console.print(f'[cyan]║\n║ [yellow][+] [green]{text}\n[cyan]║[/cyan]')
        else:
            console.print(f'\n[yellow][+] [green]{text}\n')

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
            formatted_error = self.BORDER_FORMAT.format(f'[red]{error}')
            console.print(formatted_error)
        else:
            console.print(f'[red]{error}')

    def print_file_headers(self) -> None:
        console.print(self.__ls_string.format("Size", "Last Modified", "Type", "Read", "File Name"))

    def print_file(self, file: File) -> None:
        console.print(
            self.__ls_string.format(file.size, file.last_modified, file.type, file.is_readable, file.name),
            highlight=False
        )


if __name__ == '__main__':
    pass
