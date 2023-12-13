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
        print('Did I get to startup?')
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
        print('before add players')
        self.add_players(self)
        print('AFTER FUNTION CALL ADD PLAYERS')
        self.main_box.add(
            # btn_add_players,
            self.add_players_mainbox,
            self.btn_record_score,
        )
        print('how a bout just before the window')
        self.main_window = toga.MainWindow(title=self.formal_name)
        print('how a bout just or after the window')
        self.main_window.content = self.main_box
        print('after setting the content')
        self.main_window.show()
        print('after show')
    
    def add_players(self, widget):
        # self.player_count = 0
        # self.add_players_mainbox = toga.Box(
        #     style=Pack(direction=COLUMN)
        # )
        print('in add players')
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
        print('before creating number players label')
        self.number_players = toga.Label(f'{self.player_count}')
        print('after creating number players label')
        self.btn_new_player = toga.Button(
            'Add Player',
            on_press=self.action_new_players,
            style=Pack(flex = 1)
        )
        print('between btn_newplay and btn_saveplayers')
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
        print('before action new players')
        self.action_new_players(widget)
        # self.add_players_window = toga.Window(title='Add Players',)
        # self.windows += self.add_players_window
        # self.add_players_window.content = self.add_players_mainbox
        # self.add_players_window.show()
        # self.main_window.content = self.add_players_mainbox
    
    def action_new_players(self, widget):
        print('in action new players')
        self.player_count += 1
        box_player = toga.Box(
            children=[
                toga.TextInput(placeholder=f'Player{self.player_count}'),
                toga.Label('------'),
                toga.Label('______'),
                toga.Label('0'),
                toga.NumberInput() #default=0)
            ],
            style=Pack(
                flex=1,
                direction=COLUMN,
                alignment='center',
            )
        )
        print('afer creating box_player')
        self.number_players.text = f'{self.player_count}'
        print('after updating number players')
        self.player_list_box.add(box_player)
        # box_player.children[0].focus()
        print('END OF ACTION NEW PLAYERS')


    def record_score(self, widget):
        print('record')
        print(self.player_list_box._children)
        for i in self.player_list_box._children:
            self.dict_players[i.children[0].text].append(int(i.children[-1].value))
            print(self.dict_players)
            temp_name = i.children[0].text
            for x in reversed(i.children): #range(len(i.children)-1,0):
                print(x)
                i.remove(x) #i.children[x])
            i.add(toga.Label(temp_name))
            i.add(toga.Label('------'))
            print(len(self.dict_players[i.children[0].text]))
            for round in range(0, len(self.dict_players[i.children[0].text])):
                print(round)
                i.add(toga.Label(f'{self.dict_players[i.children[0].text][round]}'))
            i.add(toga.Label('______'))
            i.add(toga.Label(f'{sum(self.dict_players[i.children[0].text])}'))
            i.add(toga.NumberInput())
        print(self.dict_players)
        print(len(self.dict_players[i.children[0].text]))

    def save_players(self, widget):
        # self.main_window.content = self.main_box
        for i in self.player_list_box._children:
            if len(i.children)>0:
                self.dict_players[f'{i.children[0].value}'] = [0]
                temp_name = i.children[0].value
                for x in reversed(i.children): 
                    print(x)
                    i.remove(x) #i.children[x])
                i.add(toga.Label(temp_name))
                i.add(toga.Label('------'))
                print(len(self.dict_players[i.children[0].text]))
                for round in self.dict_players[i.children[0].text]:
                    i.add(toga.Label(f'{self.dict_players[i.children[0].text][round]}'))
                i.add(toga.Label('______'))
                i.add(toga.NumberInput())
                
        self.btn_record_score.enabled = True
        self.btn_save_players.enabled = False
    

def main():
    return ScoreKeeper()
