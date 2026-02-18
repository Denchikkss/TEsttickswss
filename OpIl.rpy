init:

    $ mods["Nu_da_prolog"]=u"Ну, да."

    $ girl = Character (u'Девушка', color="F0F8FF", what_color="E2C778")
    $ vr = Character (u'Валера', color="1C09ED", what_color="E2C778")

    image bg_space = "mods/test/bg_space.jpg"
    image bg_street = "mods/test/bg_street.jpg"

label Nu_da_prolog:
    play music music_list['a_promise_from_distant_days'] fadein 3
    $ renpy. notify ("A promise from distant day")
    $ renpy.pause(2, hard=True)
    scene bg_space with dissolve2
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Каждую ночь я вижу этот сон."
    "Каждую ночь одно и тоже..."
    "Словно по повторяющемуся сценарию."
    "Я уже знаю, что произойдет со мной через несколько минут."
    "Это как среди бела дня видеть дежавю, и ловить ощущение того, что это точно со мной уже происходило, просто я не могу этого доказать."
    "Однако, когда я проснусь, снова всё забудется."
    window hide dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Словно каждый раз, выходя из сна мне стирают память, не давая запомнить не то что его содержимое, а даже его концовку."
    "В моей памяти останутся лишь обрывки воспоминаний, затуманенные облики, голоса и лица."
    th "Может быть, оно и к лучшему..."
    "Нет сомнений, что мои сновидения - осознанные."
    "Ведь каждый раз я могу лицезреть мириады звёзд, улетающих куда-то в небытие."
    "Улетающих вместе со мной..."
    "Могу прикоснуться рукой к планетам, астероидам."
    "Понаблюдать за их флорой и фауной."
    "Если присмотреться, можно увидеть рукав Ориона, или к примеру созвездие рыб."
    "Или даже Бетельгейзе, как в южном полушарии."
    "И каждая из этих миллиардов звезд - особенная."
    "У каждой есть свой цвет, характер, возраст, уровень теплоты или же наличие жизни."
    window hide dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    "А ещё…"
    "В моих снах присутствует одна странная девочка."
    "Я не вижу её облика, лишь слышу ее приятный голос."
    "И каждый раз она спрашивает у меня одно и тоже."
    girl "Ты пойдёшь со мной?"
    window hide dissolve
    menu:
        "Да, я пойду.":
            jump Nu_da_prolog_4
        "Пожалуй, я останусь здесь.":
            jump Nu_da_prolog_3
label Nu_da_prolog_3:
    window hide dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    th "Пойти за ней?"
    "А ведь и вправду, кто она? Откуда взялась? И стоит ли мне вообще к ней прислушиваться?"
    "Я никогда ранее не задавался этим вопросом…"
    "А ведь я разговаривал с ней уже столько тысяч раз…"
    jump Nu_da_prolog_2
label Nu_da_prolog_4:
    window hide dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Мне уже было всё равно куда идти, и чем заниматся. Ведь этот всего-лишь сон. Не думаю, что может случится что-то плохое..."
    jump Nu_da_prolog_2
label Nu_da_prolog_2: 
    window hide dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Каждый раз так сложно выбрать, что ей ответить."
    "Ведь если не отвечать - сон не закончится, а значит - я не проснусь."
    "Если бы все эти действия происходили со мной впервые, я бы непременно испугался."
    "От понимания того, что ты витаешь по бескрайним просторам космоса, так ещё и с весьма странной девочкой - я был бы уверен, что я покинул привычный мир."
    "И что теперь я навеки обречен проводить своё время тут…"
    "Но эти события повторяются уже десятки тысяч раз."
    "Каждую ночь…"
    stop music fadeout 3
    window hide dissolve
    $ renpy.pause(2, hard=True)
    scene semen_room with dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    th "А? Что?"
    play music music_list['just_think'] fadein 3
    "Из сна меня вывел телефонный звонок, доносящийся с дальней стороны комнаты."
    "Я не люблю разговаривать по телефону. Да и вообще, с людьми коммуницировать у меня получается с очень явной натяжкой."
    vr "БЛЯХА МУХА, ДА НЕ ХОЧУ Я НЕ С КЕМ РАЗГОВАРИВАТЬ."
    th "Не думал, что один лишь звонок сможет так сильно, и причем, так быстро вывести меня из себя."
    window hide dissolve
    play sound sfx_bed_squeak1 fadein 1
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Я резко встал с кровати, рывком направился к столу, где лежал телефон, и сбросил звонок."
    show blink
    "В глазах помутнело…"
    "Качнувшись в сторону стены, падая, я успел вытянуть руки."
    window hide dissolve
    play sound sfx_body_bump
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Я остался на ногах, но немного ударился плечом о стену."
    window hide dissolve
    scene black with dissolve
    scene semen_room with dissolve2
    $ renpy.pause(2, hard=True)
    window show dissolve
    vr "Ой бляха муха."
    stop music fadeout 3
    th "Пожалуй, выйду на улицу, подышу свежим воздухом."
    "Это было одним из лучших решений, поскольку комнату я всегда забывал проветривать."
    "В последствии в ней скапливалось такое количество углекислого газа, что в соотношении к кислороду оно приравнивалось как 9:1."
    th "Не удивительно, что я постоянно теряю сознание, пусть даже и на пару секунд."
    window hide dissolve
    scene black with dissolve
    $ renpy.pause(2, hard=True)
    scene bg_street with dissolve2
    play music music_list['raindrops'] fadein 3
    $ renpy.pause(2, hard=True)
    window show dissolve
    "В последнее время я стал крайне редко выходить на свежий воздух."
    "Проще сказать, я предпочел затхлую и темную комнату с компьютером, играть в игры ночами, и выходить на улицу исключительно по нужде."
    th "Сегодня, как ни странно, я своим принципам не изменил."
    window hide dissolve
    $ renpy.pause(2, hard=True)
    scene bus_stop with dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Уж не знаю как, но дорога вывела меня к автобусной остановке маршрута номер 410."
    th "Я частенько приезжал с колледжа именно сюда, после чего спешно направился в сторону дома, за любимый компьютер."
    th "Пожалуй, постою немного."
    window hide dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    th "Странно, сегодня тут безлюдно."
    "Обычно именно это место является примером большого столпотворения людей в час пик, да и не только."
    "А сегодня…"
    vr "Ничего не понимаю, бляха муха."
    play sound sfx_ikarus_arrive
    "Из потока моих раздумий меня вывел приближающейся гул мотора."
    th "Это что еще за чертовщина?"
    "Такого автобуса я раньше не наблюдал…"
    "И я имел ввиду не в плане его маршрутного номера, а непосредственно его модели."
    "Уж не знаю, что это была за модель, я в автобусах не разбираюсь."
    "Я ими просто пользуюсь, как средством передвижения, и наверное, не было бы их, я бы и не смог никуда добраться, ведь машины у меня нету."
    window hide dissolve
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Не могу этого объяснить, но неизвестная мне сила буквально заставила меня в него зайти."
    "Стоило мне только запрыгнуть в его салон, как тут двери захлопнулись, и автобус дал по газам."
    window hide dissolve
    play sound sfx_bus_out
    $ renpy.pause(2, hard=True)
    window show dissolve
    th "Честно говоря я еле удержал равновесие, после чего приземлился на свободное сидение."
    window hide dissolve
    $ renpy.pause(2, hard=True)
    scene intro_xx with dissolve2
    $ renpy.pause(2, hard=True)
    window show dissolve
    "Я не знал, куда я еду."
    "Вернее маршрут автобуса я то знал, а вот где я выйду, да и смысл моей поездки к сожалению остался для меня тайной…"
    th "Что-то плохое у меня предчувствие."
    "Раньше я никогда не замечал за собой никаких экстрасенсорных способностей, да и вообщем то не полагался на чувства."
    "В окне мигали сотни фонарей, которые вместе озаряли огромный город."
    "Различные яркие вывески, рекламные баннеры…"
    th "Всего этого я раньше не замечал, поскольку мне было не до этого."
    "Но усталость вносила свои коррективы, и постепенно клонило меня в сон."
    show blink
    "Повиновавшись, я закрыл глаза."
    th "Камон, ничего же не случится, если я ненадолго вздремну, все равно я знаю этот маршрут наизусть."
	    window hide dissolve
    $ renpy.pause(1, hard=True)
    scene bg int_house_of_mt_day with dissolve2
    window show dissolve
    show mt normal panama pioneer far dissolve2:
        xcenter 0.50 ycenter 0.51
    show sl smile pioneer far dissolve:
        xcenter 0.72 ycenter 0.51

    sl "Ольга Дмитриевна, мы пришли."
    vr "Здравствуйте."
    mt "Здравствуйте, здравствуйте!"
    "Она направила свой взгляд на меня."
    mt "Здравствуй, Валерий."
    $ renpy.pause(1, hard=True)
    th "Так, стоп."
    th "Откуда она знает мое имя? Я ведь ей даже не представлялся…"
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Я принял решение, ее об этом спросить, поскольку пока еще за простой вопрос по самовару не получил. {/font}{/color}{/size}"
    th "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Да и вообще, будут ли меня бить за подобные вопросы?{/font}{/color}{/size}"
    vr "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Откуда вы знаете мое имя? {/font}{/color}{/size}"
    show mt surprise pioneer var with dissolve
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} В моей голове спросить это выглядело самым правильным решением. {/font}{/color}{/size}"
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Но в тот же момент, я боялся не спиздануть чего-нибудь лишнего… {/font}{/color}{/size}"
    show mt grin pioneer far with dissolve
    mt "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} А я всех в этом лагере по имени знаю {/font}{/color}{/size}"
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} И скорчила такую улыбку, как будто ей за это лауреат Нобелевской премии дадут. {/font}{/color}{/size}"
    vr "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} А…Понятно… {/font}{/color}{/size}"
    show mt smile pioneer far with dissolve
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Это было все, что я был способен выдавить из себя, попутно переваривая услышанное. {/font}{/color}{/size}"
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} В этот момент Славя себе решила, что неплохо бы нас оставить наедине. Мол, свой комсомольский долг она вполне себе выполнила. {/font}{/color}{/size}"
    sl "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Мне пора, дела. До свидания.{/font}{/color}{/size}"
    hide sl smile pioneer far with dissolve2
    th "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Комсомольский долг? А такой вообще существует? {/font}{/color}{/size}"
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Естественно, я не знал, поскольку во первых жил в совершенно другое время, так еще и в Германии.{/font}{/color}{/size}"
    mt "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Валерий {/font}{/color}{/size}"
    vr "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} А? {/font}{/color}{/size}"
    th "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Черт, снова задумался {/font}{/color}{/size}"
    vr "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Ой, простите, задумался. {/font}{/color}{/size}"
    show mt grin pioneer far with dissolve
    mt "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} О комсомольском долге? {/font}{/color}{/size}"
    th "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} ЧТО? КАК? {/font}{/color}{/size}"
    vr "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Вы не поверите… {/font}{/color}{/size}"
    "{font=mods/test/fonts/Baskerville Bold Italic.ttf}{color=#FFFFFF}{size=35} Сказал я с вырвавшимся смешком. {/font}{/color}{/size}"