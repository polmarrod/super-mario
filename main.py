@namespace
class SpriteKind:
    images = SpriteKind.create()
    game_option = SpriteKind.create()
    coinOne = SpriteKind.create()
    coinTwo = SpriteKind.create()
    Shroom = SpriteKind.create()
    Turtle = SpriteKind.create()
    Shell = SpriteKind.create()
    Coin = SpriteKind.create()
    Prize = SpriteKind.create()

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, marioLevel)
    if tall:
        marioLevel.set_image(assets.image("""
            tall_mario_right0
        """))
    else:
        marioLevel.set_image(assets.image("""
            mario_right
        """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, marioLevel)
    if tall:
        marioLevel.set_image(assets.image("""
            tall_mario_left
        """))
    else:
        marioLevel.set_image(assets.image("""
            mario_left
        """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_on_destroyed(sprite2):
    global listCoinIndex
    listCoinIndex = 0
sprites.on_destroyed(SpriteKind.coinTwo, on_on_destroyed)

def jumpAnimation():
    animation.stop_animation(animation.AnimationTypes.ALL, marioLevel)
    if tall:
        if facingRight:
            marioLevel.set_image(assets.image("""
                tall_mario_jump_right
            """))
        else:
            marioLevel.set_image(assets.image("""
                tall_mario_jump_left
            """))
    else:
        if facingRight:
            marioLevel.set_image(assets.image("""
                jump_right
            """))
        else:
            marioLevel.set_image(assets.image("""
                jump_left
            """))
def initializeMenu():
    global backgroundmenu, mario, title_onep, title_twop, selector_ig, selector, spriteCoinBrillante, spriteCoinOscura, listCoins, list2
    backgroundmenu = sprites.create(assets.image("""
        background-menu
    """), SpriteKind.images)
    mario = sprites.create(assets.image("""
        mario_stan_def
    """), SpriteKind.images)
    title_onep = sprites.create(assets.image("""
            title-1-player
        """),
        SpriteKind.game_option)
    title_twop = sprites.create(assets.image("""
            title-2-player
        """),
        SpriteKind.game_option)
    selector_ig = sprites.create(assets.image("""
        selector
    """), SpriteKind.game_option)
    selector = 0
    spriteCoinBrillante = sprites.create(assets.image("""
        coin one
    """), SpriteKind.coinOne)
    spriteCoinOscura = sprites.create(assets.image("""
        coin two
    """), SpriteKind.coinTwo)
    listCoins = [spriteCoinBrillante, spriteCoinOscura]
    mario.set_position(40, 99)
    title_onep.set_position(80, 70)
    title_twop.set_position(80, 85)
    title_onep.set_scale(0.9, ScaleAnchor.MIDDLE)
    title_twop.set_scale(0.9, ScaleAnchor.MIDDLE)
    selector_ig.set_scale(0.5, ScaleAnchor.MIDDLE)
    list2 = [title_onep, title_twop]
    changePostionSelector(selector)
    buildCabecera()

def on_on_destroyed2(sprite):
    global listCoinIndex
    listCoinIndex = 1
sprites.on_destroyed(SpriteKind.coinOne, on_on_destroyed2)

def on_on_overlap(sprite3, otherSprite2):
    if sprite3.y < otherSprite2.top:
        otherSprite2.vx = 0
        animation.stop_animation(animation.AnimationTypes.ALL, otherSprite2)
        jump()
        otherSprite2.set_image(assets.image("""
            shroom_death
        """))
        pause(450)
        sprites.destroy(otherSprite2)
        info.change_score_by(100)
    else:
        deathMario()
sprites.on_overlap(SpriteKind.player, SpriteKind.Shroom, on_on_overlap)

def on_down_pressed():
    global selector
    if selector == 0:
        selector = 1
        changePostionSelector(selector)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def buildCabecera():
    global scr, x, strTemp, y, strCoins, textScore, titleScore, titleCoins, listCoinIndex, titleTime, spriteCoinOscura, spriteCoinBrillante
    scr = convert_to_text(score)
    x = len(scr)
    while x < 7:
        strTemp = "" + strTemp + "0"
        x += 1
    y = len(convert_to_text(coins))
    while y < 2:
        strCoins = "" + strCoins + "0"
        y += 1
    strCoins = "" + strCoins + convert_to_text(coins)
    strTemp = "" + strTemp + scr
    textScore = textsprite.create(strTemp)
    titleScore = textsprite.create("SCORE")
    titleCoins = textsprite.create("X" + strCoins)
    listCoinIndex = 1
    titleTime = textsprite.create("TIME")
    titleScore.set_max_font_height(1)
    titleTime.set_max_font_height(1)
    textScore.set_max_font_height(1)
    titleScore.set_position(30, 3)
    titleTime.set_position(123, 3)
    textScore.set_position(30, 10)
    titleCoins.set_position(79, 9)
    colocateCoin(spriteCoinBrillante)
    colocateCoin(spriteCoinOscura)
    while True:
        pause(500)
        if listCoinIndex == 0:
            sprites.destroy(spriteCoinBrillante)
            spriteCoinOscura = sprites.create(assets.image("""
                coin two
            """), SpriteKind.coinTwo)
            colocateCoin(spriteCoinOscura)
        else:
            sprites.destroy(spriteCoinOscura)
            spriteCoinBrillante = sprites.create(assets.image("""
                coin one
            """), SpriteKind.coinOne)
            colocateCoin(spriteCoinBrillante)
scene.on_hit_wall(SpriteKind.player, on_hit_wall)
def on_hit_wall(sprite6: Sprite, location2: tiles.Location):
    if sprite6.is_hitting_tile(CollisionDirection.RIGHT):
        sprite6.vx = -50
    elif sprite6.is_hitting_tile(CollisionDirection.LEFT):
        sprite6.vx = 50
scene.on_hit_wall(SpriteKind.food, on_hit_wall)
def startGame():
    global marioLevel

    scene.set_background_image(img("""
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    """))
    tiles.set_current_tilemap(tilemap("""
        level_1_0
    """))
    if tall:
        marioLevel = sprites.create(assets.image("""
                tall_mario_right0
            """),
            SpriteKind.player)
    else:
        marioLevel = sprites.create(assets.image("""
            mario_right
        """), SpriteKind.player)
    createPlayer(marioLevel)
    marioLevel.ay = 350
    info.set_life(3)
    info.set_score(0)
    info.start_countdown(400)

def on_hit_wall2(sprite5, location):
    if sprite5.is_hitting_tile(CollisionDirection.RIGHT):
        sprite5.vx = -50
    elif sprite5.is_hitting_tile(CollisionDirection.LEFT):
        sprite5.vx = 50
scene.on_hit_wall(SpriteKind.Shroom, on_hit_wall2)

def on_right_pressed():
    global facingRight
    facingRight = 1
    if marioLevel.vy == 0:
        if tall:
            animation.run_image_animation(marioLevel,
                            assets.animation("""
                                tall_mario_walk_right
                            """),
                            150,
                            True)
        else:
            animation.run_image_animation(marioLevel,
                assets.animation("""
                    mario_walk_right
                """),
                150,
                True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def deathMario():
    info.stop_countdown()
    info.change_life_by(-1)
    info.set_score(0)
    info.change_countdown_by(400 - info.countdown())
    tiles.set_current_tilemap(tilemap("""level_1_0"""))
    sprites.destroy_all_sprites_of_kind(SpriteKind.Shroom)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Turtle)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Shell)
    tiles.place_on_tile(marioLevel, tiles.get_tile_location(0, 13))
    spawnEnemies()

def on_left_pressed():
    global facingRight
    facingRight = 0
    if marioLevel.vy == 0:
        if tall:
            animation.run_image_animation(marioLevel,
                assets.animation("""
                    tall_mario_walk_left
                """),
                150,
                True)
        else:
            animation.run_image_animation(marioLevel,
                assets.animation("""
                    mario_walk_left
                """),
                150,
                True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def changePostionSelector(selection: number):
    selector_ig.set_position(list2[selection].x - 38, list2[selection].y + 1)
def initializeGame():
    global tall, score, level, coins
    tall = 0
    score = 0
    level = 0
    coins = 0

def on_on_overlap2(sprite22, otherSprite22):
    global shell
    if sprite22.y < otherSprite22.top:
        otherSprite22.vx = 0
        animation.stop_animation(animation.AnimationTypes.ALL, otherSprite22)
        jump()
        sprites.destroy(otherSprite22)
        info.change_score_by(100)
        shell = sprites.create(assets.image("""
            shell_sprite
        """), SpriteKind.Shell)
        tiles.place_on_tile(shell, otherSprite22.tilemap_location())
        shell.ay = 350
    else:
        deathMario()
sprites.on_overlap(SpriteKind.player, SpriteKind.Turtle, on_on_overlap2)

def on_a_pressed():
    global level
    if level == 0 and selector == 0:
        level = 1
        startGame()
        destroyMenu()
    elif level != 0:
        if marioLevel.vy == 0:
            jump()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def spawnEnemies():
    global shroom, turtle
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile2
    """)):
        if marioLevel.tilemap_location().column + scene.screen_width() > value.column:
            shroom = sprites.create(assets.image("""
                shroom_sprite0
            """), SpriteKind.Shroom)
            tiles.place_on_tile(shroom, value)
            tiles.set_tile_at(value, assets.tile("""
                transparency16
            """))
            shroom.vx = -20
            animation.run_image_animation(shroom,
                [img("""
                        . . . . . . e e e e . . . . . . 
                                        . . . . . e e e e e e . . . . . 
                                        . . . . e e e e e e e e . . . . 
                                        . . . e e e e e e e e e e . . . 
                                        . . e f f e e e e e e f f e . . 
                                        . e e e d f e e e e f d e e e . 
                                        . e e e d f f f f f f d e e e . 
                                        e e e e d f d e e d f d e e e e 
                                        e e e e d d d e e d d d e e e e 
                                        e e e e e e e e e e e e e e e e 
                                        . e e e e d d d d d d e e e e . 
                                        . . . . d d d d d d d d . . . . 
                                        . . f f d d d d d d d d . . . . 
                                        . f f f f d d d d d d f f . . . 
                                        . f f f f f d d d d f f f . . . 
                                        . . f f f f f . . f f f . . . .
                    """),
                    img("""
                        . . . . . . e e e e . . . . . . 
                                        . . . . . e e e e e e . . . . . 
                                        . . . . e e e e e e e e . . . . 
                                        . . . e e e e e e e e e e . . . 
                                        . . e f f e e e e e e f f e . . 
                                        . e e e d f e e e e f d e e e . 
                                        . e e e d f f f f f f d e e e . 
                                        e e e e d f d e e d f d e e e e 
                                        e e e e d d d e e d d d e e e e 
                                        e e e e e e e e e e e e e e e e 
                                        . e e e e d d d d d d e e e e . 
                                        . . . . d d d d d d d d . . . . 
                                        . . . . d d d d d d d d f f . . 
                                        . . . f f d d d d d d f f f f . 
                                        . . . f f f d d d d f f f f f . 
                                        . . . . f f f . . f f f f f . .
                    """)],
                500,
                True)
            shroom.ay = 160
            shroom.set_bounce_on_wall(False)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile
    """)):
        if marioLevel.tilemap_location().column + scene.screen_width() > value2.column:
            turtle = sprites.create(assets.image("""
                turtle_sprite
            """), SpriteKind.Turtle)
            tiles.place_on_tile(turtle, value2)
            tiles.set_tile_at(value2, assets.tile("""
                transparency16
            """))
            turtle.vx = -20

def on_up_pressed():
    global selector
    if selector == 1:
        selector = 0
        changePostionSelector(selector)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def jump():
    jumpAnimation()
    marioLevel.vy = -220
def createPlayer(player2: Sprite):
    scene.camera_follow_sprite(player2)
    tiles.place_on_tile(player2, tiles.get_tile_location(0, 13))
    controller.move_sprite(player2, 100, 0)
def destroyMenu():
    sprites.destroy_all_sprites_of_kind(SpriteKind.images)
    sprites.destroy_all_sprites_of_kind(SpriteKind.game_option)
    sprites.destroy_all_sprites_of_kind(SpriteKind.coinTwo)
    sprites.destroy_all_sprites_of_kind(SpriteKind.coinOne)

def on_on_overlap3(sprite32, otherSprite3):
    otherSprite3.vx = sprite32.x * 2
    otherSprite3.set_bounce_on_wall(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.Shell, on_on_overlap3)

def colocateCoin(mySprite: Sprite):
    mySprite.set_position(65, 9)

def on_on_overlap4(sprite4, otherSprite):
    global tall
    sprites.destroy(otherSprite)
    tall = 1
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap4)
def on_on_update():
    global boost
    if level != 0:
        spawnEnemies()
        for value22 in tiles.get_tiles_by_type(assets.tile("""
            prize_block
        """)):
            
            if marioLevel.tilemap_location().column == value22.column and marioLevel.tilemap_location().row == value22.row + 1:
                coin = sprites.create(assets.image("""
                        coin_sprite
                    """), SpriteKind.Coin)
                tiles.place_on_tile(coin, value22)
                coin.vy = -200
                coin.ay = 400
                info.change_score_by(10)
                
                tiles.set_tile_at(value22, assets.tile("""
                    myTile1
                """))
        for value222 in tiles.get_tiles_by_type(assets.tile("""
            prize_block_boost
        """)):
            if marioLevel.tilemap_location().column == value222.column and marioLevel.tilemap_location().row == value222.row + 1:
                boost = sprites.create(assets.image("""
                    boost_sprite
                """), SpriteKind.food)
                tiles.place_on_tile(boost,
                    tiles.get_tile_location(value222.column, value222.row - 1))
                boost.vx = 50
                boost.ay = 160
                tiles.set_tile_at(value222, assets.tile("""
                    myTile1
                """))
game.on_update(on_on_update)
def on_on_update2():
    if level != 0:
        checkFall()
        if marioLevel.vx == 0 and marioLevel.vy == 0:
            if tall:
                if facingRight:
                    marioLevel.set_image(assets.image("""
                        tall_mario_right0
                    """))
                else:
                    marioLevel.set_image(assets.image("""
                        tall_mario_left
                    """))
            elif facingRight:
                marioLevel.set_image(assets.image("""
                    mario_right
                """))
            else:
                marioLevel.set_image(assets.image("""
                    mario_left
                """))
game.on_update(on_on_update2)
def checkFall():
    if marioLevel.tilemap_location().row == 15:
        deathMario()
    for value in sprites.all_of_kind(SpriteKind.Shroom):
        if value.tilemap_location().row == 15:
            sprites.destroy(value)
    for value2 in sprites.all_of_kind(SpriteKind.Turtle):
        if value2.tilemap_location().row == 15:
            sprites.destroy(value2)
    for value3 in sprites.all_of_kind(SpriteKind.Food):
        if value3.tilemap_location().row == 15:
            sprites.destroy(value3)
    for value4 in sprites.all_of_kind(SpriteKind.Shell):
        if value4.tilemap_location().row == 15:
            sprites.destroy(value4)
def on_hit_wall3(sprite, location):
    if sprite.tile_kind_at(TileDirection.BOTTOM, assets.tile("""
        myTile1
    """)):
        sprites.destroy(sprite)
scene.on_hit_wall(SpriteKind.Coin, on_hit_wall3)
    
boost: Sprite = None
turtle: Sprite = None
shroom: Sprite = None
shell: Sprite = None
level = 0
titleTime: TextSprite = None
titleCoins: TextSprite = None
titleScore: TextSprite = None
textScore: TextSprite = None
strCoins = ""
coins = 0
y = 0
strTemp = ""
x = 0
score = 0
scr = ""
list2: List[Sprite] = []
listCoins: List[Sprite] = []
spriteCoinOscura: Sprite = None
spriteCoinBrillante: Sprite = None
selector = 0
selector_ig: Sprite = None
title_twop: Sprite = None
title_onep: Sprite = None
mario: Sprite = None
backgroundmenu: Sprite = None
listCoinIndex = 0
tall = 0
facingRight = 1
marioLevel: Sprite = None
initializeGame()
initializeMenu()