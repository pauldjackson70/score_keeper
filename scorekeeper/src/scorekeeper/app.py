"""
A program to keep track of score during game play
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ScoreKeeper(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.
        """
        main_box = toga.Box()

        btn_add_players=toga.Button(
            '+Add Players',
            on_press=self.add_players,
            style=Pack(padding=5)
        )

        main_box.add(btn_add_players)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    
    def add_players(self, widget):
        self.player_count =0
        self.add_players_mainbox =toga.Box(
            style=Pack(direction=COLUMN)
        )
        self.add_players_box =toga.Box(
            style=Pack(
                flex=1,
                direction=ROW,
                padding=10,
            )
        )
        self.player_list_box =toga.Box(
            style=Pack(
                flex=1,
                direction=COLUMN,
                padding=3,
            )
        )
        self.number_players = toga.Label(self.player_count)
        self.btn_new_player = toga.Button(
            '+',
            on_press=self.action_new_players,
            # style=Pack(padding=5)
        )
        self.add_players_box.add(
            self.number_players,
            self.btn_new_player,
        )
        self.add_players_mainbox.add(
            self.add_players_box,
            self.player_list_box,
        )
        self.action_new_players(widget)
        add_players_window = toga.Window(title='Add Players',)
        self.windows += add_players_window
        add_players_window.content = self.add_players_mainbox
        add_players_window.show()
    
    def action_new_players(self, widget):
        self.player_count += 1
        self.player_list_box.add(
            toga.TextInput(
                id='player'+str(self.player_count),
                placeholder='player'+str(self.player_count),
                style=Pack(padding=3)
            )
        )
        self.number_players.text = self.player_count
def main():
    return ScoreKeeper()
