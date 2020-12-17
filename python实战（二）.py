class TongLao():
    def __init__(self,hp=None,power=None):
        self.my_hp=hp
        self.my_power=power


    def see_people(self,name):
        name=name
        if name=='WYZ':
            print("师弟！！！！")
        elif name=='LQS':
            print("李秋水")
        elif name=='DCQ':
            print("叛徒！我杀了你")

    def fight_zms(self,enemy_hp,enemy_power):
        my_hp=self.my_hp/2
        my_power=self.my_power*10
        # print(my_hp)
        # print(my_power)
        while True:
            my_hp = my_hp - enemy_hp
            enemy_hp = enemy_hp - my_power
            if my_hp <= 0:
                print(f"我输了,my_hp={my_hp},enemy_hp={enemy_hp}")
                break
            elif enemy_hp <= 0:
                print(f"你输了,my_hp={my_hp},enemy_hp={enemy_hp}")
                break

class XuZhu(TongLao):
    def read(self):
        print('罪过罪过')

if __name__ == '__main__':
    a=TongLao(1001,500)
    a.fight_zms(500,300)
    # a=XuZhu()
    # a.read()
