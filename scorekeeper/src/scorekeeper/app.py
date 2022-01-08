"""
A program to keep track of score during game play
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, TEXT_ALIGN_CHOICES
# from travertino.constants import CENTER


class ScoreKeeper(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.
        """
        self.main_box = toga.Box()

        self.dict_players = {}

        btn_add_players=toga.Button(
            '+Add Players',
            on_press=self.add_players,
            style=Pack(padding=5)
        )
        self.btn_record_score = toga.Button(
            'Record Score',
            on_press=self.record_score,
            style=Pack(padding=5)
        )

        self.main_box.add(
            btn_add_players,
            self.btn_record_score,
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
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
            style=Pack(flex = 1)
        )
        self.btn_save_players = toga.Button(
            'Save',
            on_press=self.save_players,
            style=Pack(flex = 1)
        )
        self.add_players_box.add(
            self.number_players,
            self.btn_new_player,
            self.btn_save_players,
        )
        self.add_players_mainbox.add(
            self.add_players_box,
            self.player_list_box,
        )
        self.action_new_players(widget)
        self.add_players_window = toga.Window(title='Add Players',)
        self.windows += self.add_players_window
        self.add_players_window.content = self.add_players_mainbox
        self.add_players_window.show()
    
    def action_new_players(self, widget):
        self.player_count += 1
        self.player_list_box.add(
            toga.TextInput(
                id='input_player'+str(self.player_count),
                placeholder='player'+str(self.player_count),
                style=Pack(padding=3)
            )
        )
        self.player_list_box.children[self.player_count-1].focus()
        self.number_players.text = self.player_count
    def record_score(self, widget):
        print('record')
        print(self.main_box._children)
        for i in self.main_box._children:
            if len(i.children)>0: print(f'{i.children[0].text}: {i.children[-1].value}')

    def save_players(self, widget):
        for a in range(0, self.player_count):
            self.dict_players[f'{self.player_list_box.children[a].value}'] = ()
            self.main_box.add(
            toga.Box(
                children=[
                    toga.Label(f'{self.player_list_box.children[a].value}'),
                    toga.Label('0',style=Pack(alignment='center')),
                    toga.Label('______'),
                    toga.NumberInput(f'input_{self.player_list_box.children[a].value}')
                ],
                style=Pack(
                    flex=1,
                    direction=COLUMN,
                    alignment='center',
                )
            )
        )
        print(self.dict_players)
        self.add_players_window.close()

def main():
    return ScoreKeeper()
