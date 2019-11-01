player_name = "唐僧"
boss_name = "白骨精"
print("=" * 20, "欢迎来到游戏《%s大战%s》" % (player_name, boss_name), "=" * 20)
print("请选择您的游戏身份：\r\n"
      "\t1、唐僧\r\n"
      "\t2、白骨精")
player_choose = int(input("请选择："))
if player_choose == 1:
    print("您选择的身份是唐僧")
elif player_choose == 2:
    print("您竟然选择了白骨精，太不要脸了，系统将自动分配身份，您将以唐僧的身份进行游戏!")
else:
    print("您的输入有误，系统将自动分配身份，您将以唐僧的身份进行游戏!")

# 玩家初始生命值和攻击力
player_life = 2     # 生命值
player_attack = 2   # 攻击力

# BOOS生命值和攻击力
boss_life = 10
boss_attack = 10

print("您的生命值是%s，攻击力是%s" % (player_life, player_attack))

# 显示游戏选项，游戏正式开始
while True:
    print("请选择您要执行的操作：")
    print("\t1、练级")
    print("\t2、打BOSS")
    print("\t3、逃跑")
    game_choose = int(input("请选择您要执行的操作:"))

    # 处理用户的选择
    if game_choose == 1:
        player_life += 1
        player_attack += 1
        print(f"唐僧恭喜您升级了，生命值是{player_life}，攻击力是{player_attack}")
    elif game_choose == 2:
        print("开始攻击BOSS,BOSS受到%s点伤害，生命值-%s" % (player_attack, player_attack))
        boss_life -= player_attack
        # 检查boss是否死亡
        if boss_life <= 0:
            # boss死亡
            print("BOSS已死亡，游戏结束!")
            break

        # boss反击玩家
        # 减去玩家的生命值
        player_life -= boss_attack
        print("玩家受到BOSS%s点伤害，生命值减去%s" % (boss_attack, boss_attack))
        if player_life <= 0:
            print("您受到致命伤害，生命值为0，游戏结束")
            break
    elif game_choose == 3:
        print("您逃跑了，游戏结束")
        break
    else:
        continue
