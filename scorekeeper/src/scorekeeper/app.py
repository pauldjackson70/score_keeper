"""
A program to keep track of score during game play
"""
import toga
from toga import style
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, TEXT_ALIGN_CHOICES
# from travertino.constants import CENTER


class ScoreKeeper(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.
        """
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        self.dict_players = {}
        self.player_count = 0
        # btn_add_players=toga.Button(
        #     '+Add Players',
        #     on_press=self.add_players,
        #     style=Pack(padding=5)
        # )
        self.btn_record_score = toga.Button(
            'Record Score',
            on_press=self.record_score,
            enabled=False,
            style=Pack(padding=5)
        )
        self.add_players_mainbox = toga.Box(
            style=Pack(direction=COLUMN)
        )
        self.add_players(self)
        self.main_box.add(
            # btn_add_players,
            self.add_players_mainbox,
            self.btn_record_score,
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
    
    def add_players(self, widget):
        # self.player_count = 0
        # self.add_players_mainbox = toga.Box(
        #     style=Pack(direction=COLUMN)
        # )
        self.add_players_box = toga.Box(
            style=Pack(
                flex=1,
                direction=ROW,
                padding=10,
            )
        )
        self.player_list_box =toga.Box(
            style=Pack(
                flex=1,
                direction=ROW,
                padding=3,
            )
        )
        self.number_players = toga.Label(self.player_count)
        self.btn_new_player = toga.Button(
            'Add Player',
            on_press=self.action_new_players,
            style=Pack(flex = 1)
        )
        self.btn_save_players = toga.Button(
            'Save Player Names',
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
        # self.add_players_window = toga.Window(title='Add Players',)
        # self.windows += self.add_players_window
        # self.add_players_window.content = self.add_players_mainbox
        # self.add_players_window.show()
        # self.main_window.content = self.add_players_mainbox
    
    def action_new_players(self, widget):
        self.player_count += 1
        # self.player_list_box.add(
        #     toga.TextInput(
        #         id='input_player'+str(self.player_count),
        #         placeholder='player'+str(self.player_count),
        #         style=Pack(padding=3)
        #     )
        # )
        box_player = toga.Box(
            children=[
                toga.TextInput(placeholder=f'Player{self.player_count}'),
                toga.Label('------'),
                toga.Label('______'),
                toga.Label('0'),
                toga.NumberInput(default=0)
            ],
            style=Pack(
                flex=1,
                direction=COLUMN,
                alignment='center',
            )
        )
        self.number_players.text = self.player_count
        self.player_list_box.add(box_player)
        box_player.children[0].focus()


    def record_score(self, widget):
        print('record')
        print(self.player_list_box._children)
        for i in self.player_list_box._children:
            if len(i.children)>0: 
                print(i.children)
                print(f'{i.children[0].text}: {i.children[-1].value}')
                self.dict_players[i.children[0].text].append(i.children[-1].value)
                i.insert(len(i.children)-3,toga.Label(i.children[-1].value))
                i.children[-1].value = 0
                i.children[-2].text = sum(self.dict_players[i.children[0].text])
        print(self.dict_players)

    def save_players(self, widget):
        # self.main_window.content = self.main_box
        for i in self.player_list_box._children:
            if len(i.children)>0:
                self.dict_players[f'{i.children[0].value}'] = []
                i.insert(1,toga.Label(i.children[0].value))
                i.remove(i.children[0])
        self.btn_record_score.enabled = True
        # for a in range(0, self.player_count):
        #     self.dict_players[f'{self.player_list_box.children[a].value}'] = []
            
        #     box_player = toga.Box(
        #         children=[
        #             toga.Label(f'{self.player_list_box.children[a].value}'),
        #             toga.Label('------'),
        #             toga.Label('______'),
        #             toga.Label('0'),
        #             toga.NumberInput(f'input_{self.player_list_box.children[a].value}',default=0)
        #         ],
        #         style=Pack(
        #             flex=1,
        #             direction=COLUMN,
        #             alignment='center',
        #         )
        #     )
        #     self.player_list_box.add(box_player)
        #     self.player_list_box.style=Pack(direction=ROW)
        # print(self.dict_players)
        # self.add_players_window.close()

def main():
    return ScoreKeeper()
