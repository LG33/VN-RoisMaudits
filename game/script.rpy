﻿image decor noir = "#000"

image decor intro:
    "backgrounds/intro.png"
    zoom 0.5
    
image decor chambre:
    "backgrounds/bedroom.jpg"
    zoom 2
    
image decor grande_salle:
    "backgrounds/bigroom.jpg"
    zoom 2
    
image decor entree:
    "backgrounds/entry.png"
    zoom 0.5
    
image decor village:
    "backgrounds/village.jpg"
    zoom 0.2
    
image decor fontainebleau:
    "backgrounds/fontainebleau.png"
    zoom 0.5


image helene normal:
    "characters/helene/helene_normal.png"
    zoom 0.45
image helene masque:
    "characters/helene/helene_masque.png"
    zoom 5
image helene inquiete:
    "characters/helene/helene_panique.png"
    zoom 0.45
image helene serieuse:
    "characters/helene/helene_serieuse.png"
    zoom 0.45
image helene souriante:
    "characters/helene/helene_sourire.png"
    zoom 0.45

image helene_demon normal:
    "characters/helene_demon/helene_demon_normal.png"
    zoom 0.45
image helene_demon souriante:
    "characters/helene_demon/helene_demon_souriante.png"
    zoom 0.45

image gaston normal:
    "characters/gaston/gaston_normal.png"
    zoom 5
image gaston masque:
    "characters/gaston/gaston_masque.png"
    zoom 5
image gaston serieux:
    "characters/gaston/gaston_serieux.png"
    zoom 5
image gaston souriant:
    "characters/gaston/gaston_souriant.png"
    zoom 5
image gaston panique:
    "characters/gaston/gaston_panique.png"
    zoom 5

image anne normal:
    "characters/anne/anne_normal.png"
    zoom 5
image anne masque:
    "characters/anne/anne_masque.png"
    zoom 5
image anne choquee:
    "characters/anne/anne_choquee.png"
    zoom 5
image anne serieuse:
    "characters/anne/anne_serieuse.png"
    zoom 5
image anne souriante:
    "characters/anne/anne_souriante.png"
    zoom 5

image charles normal:
    "characters/charles/charles_normal.png"
    zoom 0.4
image charles masque:
    "characters/charles/charles_masque.png"
    zoom 5
image charles panique:
    "characters/charles/charles_panique.png"
    zoom 0.4
image charles serieux:
    "characters/charles/charles_serieux.png"
    zoom 0.4
image charles dague:
    "characters/charles/charles_dague.png"
    zoom 0.4

image arm_0:
    "backgrounds/bras/bras_0.png"
    zoom 0.5
image arm_1:
    "backgrounds/bras/bras_1.png"
    zoom 0.5
image arm_2:
    "backgrounds/bras/bras_2.png"
    zoom 0.5
image arm_3:
    "backgrounds/bras/bras_3.png"
    zoom 0.5

image bras_leon_flashback = im.MatrixColor("characters/bras_leon_fin.png",im.matrix.saturation(0.1))

define leon = Character('Léon', outlines=[(1, "#008800", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")
define helene = Character('Hélène', image="helene", outlines=[(1, "#ff00ff", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")
define gaston = Character('Gaston', image="gaston", color="#9999ff", window_top_padding=40, window_background="gui/dialogue_box.png")
define anne = Character('Anne', image="anne", color="#eeeeee", window_top_padding=40, window_background="gui/dialogue_box.png")
define charles = Character('Charles', image="charles", outlines=[(1, "#aa7700", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")
define inconnu = Character('???', window_top_padding=40, window_background="gui/dialogue_box.png")
define self = Character(None, color="#ffff99", what_italic=True, what_color="#ffdd55", window_top_padding=90, window_background="gui/narrative_box.png")
define jacques_inconnu = Character("???", what_color="#8888ff", what_italic=True, what_slow_cps=10, window_top_padding=40, window_background="gui/dialogue_box.png")
define jacques = Character("Jacques De Molay", what_color="#8888ff", what_italic=True, what_slow_cps=20, window_top_padding=40, window_background="gui/dialogue_box.png")
define t = Character(None, what_xalign=0.5, what_yalign=0.5, what_text_align=0.5, window_background="gui/dialogue_box.png")

transform left: 
    xalign 0.2 
    yalign 1.8
    
transform right: 
    xalign 0.8
    yalign 1.8
    
transform center: 
    xalign 0.5 
    yalign 1.8
    
transform enter_right:
    on show:
        xalign 3.0
        linear 0.5 xalign 1.5
    on hide:
        xalign 1.5
        linear 0.5 xalign 3.0
    
transform enter_left:
    on show:
        xalign -3.0
        linear 0.5 align -0.2
    on hide:
        xalign -0.2
        linear 0.5 xalign -3.0
    
transform bras_transform:
    xalign 0.25
    on show:
        yalign 2.0
        linear 0.5 yalign 1.2
    on hide:
        yalign 1.2
        linear 0.5 yalign 2.0

define ellipse = Fade(0.5, 1.0, 0.5)
define long_dissolve = Dissolve(1.0)

init python:
    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
        }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)
    
    shake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
    flash_rouge = Fade(.25, 0, .25, color="#ff0000")
    flash_blanc = Fade(.25, 0, .25, color="#ffffff")
    
    choix1 = 0
# commentaires généraux.
# ATTENTION : vrai guillemet-> "    (faux guillemets -> "")

# 01 - Fuite
label start:
    show screen menu_button
    scene decor noir with dissolve
    
    inconnu "Léon ! Léon !!"
    pause 1.0
    self "Que… qu’est-ce qu’il se passe ?"
    
    scene decor intro with long_dissolve
    
    pause 0.5
    
    inconnu "Tu t’es évanoui. Dépêche-toi, il faut fuir !"
    self "Je… je ne comprends rien…"

    menu:
        "\"Qui est-ce que je suis ?\"":
            leon "Qui est-ce que je suis ?"
            jump fuite_fin
        "\"Qui êtes-vous\"":
            leon "Qui êtes-vous ?"
            jump fuite_fin
    
label fuite_fin:
    inconnu "QU… {w=0.7}QUOI ?!"
    
    pause 2.0
    
    inconnu "On n’a pas le temps, suis-moi !"
    leon "Ah… {w=0.5}ma tête…"
    
    with shake

    scene decor noir with dissolve

    inconnu "LÉON !!!"

    pause 4.0

    jump reveil_start
# END FILE 01 - Fuite

# 02 - Réveil
label reveil_start:
    scene decor chambre
    show helene inquiete at left
    with dissolve

    inconnu "Ça y est, tu es réveillé ?"
    leon "..."    
    inconnu "J’étais vraiment inquiète, tu sais !"
    self "Cette voix… {w=0.5}c’est la fille au masque ?"

    show helene normal
    
    inconnu "L’attaque d’hier ne s’est pas tout à fait passée comme prévu et on t’a retrouvé évanoui après s’être séparés."
    inconnu "Mais ne t’inquiète pas, Gaston t’as porté et on s’en est tous sortis indemnes."
    leon "Une attaque ? Gaston ?"

    show helene inquiete
    pause 1.0

    inconnu "Je m’en doutais… {w=0.5}Tu ne te souviens vraiment plus de rien…"

    helene normal "Tu ne te souviens même plus de moi… {w=0.5}je m’appelle Hélène."

    menu:
        "\"Où est ce qu’on est ?\"":
            jump reveil_1_1
        "\"Qu’est-ce qui s’est passé ?\"":
            jump reveil_1_2

label reveil_1_1:
    leon "Où est ce qu’on est ?"
    helene "Nous sommes dans des souterrains. Tu peux voir ça comme la base secrète de l’Ordre du Lys."
    jump reveil_1_end

label reveil_1_2:
    leon "Qu’est-ce qui s’est passé ?"
    helene "Nous avons attaqué une église au nom de l’Ordre du Lys, mais ça ne s’est pas passé comme prévu..."
    jump reveil_1_end

label reveil_1_end:
    leon "L’Ordre du Lys ?"

    pause 0.3
    self "*bruit de porte qui s’ouvre*"
    pause 0.5
    show anne normal at right with dissolve

    inconnu "Hélène, Charles demande à nous voir."

    pause 1.0
    show anne souriante

    inconnu "Ah, Léon, tu es enfin réveillé !"
    inconnu "Tu as dormi comme un loir, tu sais. Ne nous fais plus de frayeurs comme ça !"

    show helene inquiete

    helene "Anne… {w=0.5}Il a perdu la mémoire…"

    show anne serieuse

    anne "Oh…"

    pause 2.0

    show anne souriante

    anne "Je suis Anne, nous sommes amis. "
    anne normal "Charles nous attend. Léon, tu devrais venir avec nous."
    
    jump reunion_start
# END FILE 02 - Réveil


# 03 - Réunion
label reunion_start:
    scene decor noir with dissolve
    pause 2.0

    self "Les couloirs sont étroits et humides... {w=0.5}ça ne me met pas vraiment à l'aise."

    pause 2.0
    
    scene decor grande_salle
    show charles normal at left
    show gaston normal at right
    with dissolve
    
    self "Ces personnes… {w=0.5}évidemment, leur visage ne me dit rien."

    hide charles
    hide gaston

    self "Au moins, cette salle est déjà un peu plus spacieuse."

    show charles normal at center with dissolve
    
    inconnu "Léon aurait donc perdu la mémoire..."
    charles "Je me présente. Tu peux m'appeler Charles. Je suis fondateur et dirigeant de l'Ordre du Lys."
    
    hide charles
    show gaston at center with dissolve
    with dissolve

    gaston souriant "Moi, c'est Gaston. T'as intérêt à vite retrouver la mémoire !"
    leon "L'Ordre du Lys... {w=0.5}qu’est-ce que c'est ?"

    hide gaston
    show charles normal at center

    charles "Te souviens-tu de la situation dans laquelle la France se trouve actuellement ?"
    leon "Absolument pas…"

    hide charles
    show helene inquiete at center
    with dissolve

    helene "Tu ne te souviens même pas de ça…"

    hide helene
    show charles normal at center
    with dissolve

    charles "Le royaume de France était encore paisible jusqu’à récemment."
    charles serieux "Cependant, il y a une dizaine d’années, celui-ci a été renversé par les Templiers."
    leon "Les Templiers ?"
    charles normal "C’est un groupe religieux maléfique qui a mis la main sur un artefact démoniaque lors de la dernière croisade."
    charles serieux "Ils s’en sont servis afin de pratiquer des rites occultes qui leur ont permis d’invoquer des démons."
    self "Des… {w=0.5}des démons ?! Vraiment ?!"

    hide charles
    show gaston serieux at center

    gaston "Ces salopards ont utilisé les pouvoirs des démons pour tuer un grand nombre d’innocents."

    hide gaston
    show charles serieux at center
    
    charles "Il ne leur a fallu qu’une nuit pour prendre d’assaut le château royal et assassiner la majorité des nobles qui s’y trouvaient."
    charles "En un clin d’oeil, ils ont terrassé tout le royaume et ont pris le pouvoir"
    charles "À présent, ils dirigent le pays dans une atmosphère de terreur."
    charles normal "L’Ordre du Lys est un groupe de résistants."
    charles "Il a été crée dans le but de lutter contre les Templiers."
    leon "L’Ordre du Lys doit être un très grand groupe pour pouvoir lutter contre eux…"
    charles serieux "..."
    charles "Tous les membres de l’Ordre sont présents dans cette pièce."
    leon "Que… quoi ?!"
    leon "Vous comptez les vaincre avec seulement 5 personnes ?!"
    self "Ils se moquent de moi ?!"

    hide charles
    show anne serieuse at center

    anne serieuse "Eh, nous ne sommes peut-être pas nombreux, mais le peuple est de notre côté."
    anne "Nous agissons au nom de tous ceux qui n’ont pas le courage de faire face aux Templier."
    anne "Nous avons de nombreux alliés qui nous aident financièrement ou qui nous fournissent des informations."
    anne "Avoir un prince parmi nous aide vraiment pour notre image."
    leon "Un… un prince ?!"
    anne normal "Ah, c’est vrai que tu ne t’en souviens plus."
    anne souriante "Charles était un prince de l’ancien royaume."

    hide anne
    show charles normal with dissolve

    charles "Je suis le dernier survivant de la famille royale."
    self "Un prince, vraiment ?!"

    menu:
        "\"Excusez mon impolitesse, votre Altesse. Je ne savais pas.\"":
           jump reunion_3_1
        "\"Un prince devrait vraiment se battre alors qu’il n’y a plus d’autre héritier ?\"":
           jump reunion_3_2

label reunion_3_1:
    leon "Excusez mon impolitesse, votre Altesse. Je ne savais pas."

    pause 2.0
    hide charles
    show gaston souriant at center

    gaston "Ha ha! Tu devrais voir ta tête !"

    hide gaston
    show anne normal at center
    with dissolve

    anne "Gaston, ne te moque pas! Tu avais réagi exactement de la même façon la première fois que tu as rencontré Charles toi aussi."
    self "Elle dit ça, mais elle se retient de rire elle aussi…"

    show anne souriante

    anne "Nous avons décidé que les statuts n’auraient pas d’importance au sein de l’ordre. D’ailleurs, j’étais moi même servante avant de rejoindre l’Ordre !"

    jump reunion_3_end

label reunion_3_2:

    leon "Un prince devrait vraiment se battre alors qu’il n’y a plus d’autre héritier ?"

    hide charles
    show anne normal at center

    anne "Si lui ne se bat pas, qui le fera? Son simple nom permet de nous rendre plus crédible auprès de nos alliés."
    anne souriante "Et, tu sais, nous avons décidé que les statuts n’auraient pas d’importance au sein de l’ordre. D’ailleurs, j’étais moi même servante avant de rejoindre l’Ordre !"

    jump reunion_3_end

label reunion_3_end:

    hide anne
    show gaston souriant at center

    gaston "Et moi, j’étais paysan. Dur à croire, hein !"

    hide gaston
    show helene normal at center

    helene "Quand à nous deux, nous étions nobles mais avons perdu le statut lors du coup d’état."

    hide helene
    show charles normal at center

    charles "Quoi qu’il en soit, nous avons beau n’être que 5 véritables exécutants, c’est largement suffisant."
    charles "Ce n’est pas comme si nous avions besoin d’une armée."
    charles "Le règne des Templiers est centré autour d’une seule et unique personne."
    charles serieux "Jacques de Molay."
    charles normal "Il est le grand maître des Templiers. C’est lui qui est à l’origine de toutes les atrocités commises par les Templiers."
    charles serieux "Si nous le tuons tout le reste s’écroulera."
    self "Ce raisonnement semble bien optimiste…"
    charles normal "Nous sommes un groupe d’élite spécialisé dans l’infiltration et l’assassinat. L’Ordre du Lys a été crée dans le but d’abattre cet homme."
    leon "Mais… l’Ordre doit se battre contre des démons, pas vrai ?"
    charles "À vrai dire, nous n’en avons que rarement croisé et nous avons réussi à nous enfuir à chaque fois."
    charles "Bien qu’on ne sache presque rien sur eux, ils ne sont pas si nombreux et la plupart restent dans les châteaux sans en sortir."
    leon "..."
    leon "Les Templiers sont-ils vraiment si mauvais pour justifier de renverser le pouvoir ?"
    self "Après tout, il ne font que me donner leur version des faits…"

    hide charles
    show anne serieuse at center

    anne "Léon."
    anne "Si quelqu’un renie leur façon de faire ou est soupçonné d’agir contre leur intérêt…"
    anne "Ils le punissent par une malédiction."

    hide anne
    show charles serieux at center

    charles "Cette malédiction est pire que la mort."
    charles normal "Une marque noire apparaît sur le corps de la personne maudite et s’étend peu à peu sur son corps."
    charles "Le corps est entièrement recouvert après quelques jours."
    charles serieux "La personne maudite perd alors la raison, se met à se déchaîner sans distinction sur les gens qui l’entourent et fini par mourir une fois épuisée mentalement."
    self "Ça semble vraiment tiré par les cheveux... {w=0.5}Un phénomène pareil existe réellement ?"
    leon "Pourquoi les Templiers ne tuent pas simplement la personne concernée plutôt que de lui infliger ça ?"
    charles normal "Leur objectif est de traumatiser le peuple pour le convaincre de ne pas s’opposer à eux."
    charles "Cette malédiction est contagieuse. Elle se transmet simplement par le toucher."
    charles serieux "Par conséquent, les personnes affectées finissent souvent exécutées par leur propre famille ou amis."
    charles "Malheureusement, il n’y a pas de remède une fois que quelqu’un a été affecté par la malédiction."

    hide charles
    show gaston serieux at center

    gaston "Eh, on s’était mis d’accord pour plus aborder ce sujet."

    hide gaston
    show helene serieuse "Gaston… Léon ne se souvient plus de rien, la situation est particulière."

    show gaston serieux at center

    gaston "Alors ce sera sans moi."

    hide gaston with dissolve
    pause 0.5
    show helene serieuse 

    helene "Eh !"

    hide helene
    show charles serieux at center

    charles "Laisse-le, Hélène."
    leon "Qu’est-ce qu’il lui arrive ?"

    hide charles
    show anne serieuse at center

    anne "Parler de ce sujet est un tabou pour lui."
    leon "Comment ça ?"
    anne "..."
    anne "C’est une histoire qui remonte à l’époque où Hélène et toi n’aviez pas encore rejoint l’Ordre. Celui-ci était composé de Charles, Gaston, moi-même et d’un dernier membre."
    anne normal "C’était une jeune femme radieuse. Elle s’appelait Charlotte."
    anne souriante "Dès la première fois qu’il l’a vue, Gaston est tout de suite tombé sous son charme."
    anne "Charlotte, quand à elle, était un peu plus réservée mais a fini par se laisser séduire"
    anne normal "..."
    anne serieuse "..."
    anne "Un jour, l’Ordre a mené un assaut dont le but était d’assassiner un dirigeant Templier."
    anne "L’attaque s’est mal déroulée et Charlotte a été atteinte par un artefact démoniaque."
    anne "Une marque noire est apparue sur son corps… Elle était touchée par la malédiction."
    anne "..."
    anne "Nous avons réussi à nous échapper, mais Charlotte était condamnée."

    hide anne
    show charles serieux at center

    charles "Je lui ai porté le coup de grâce lorsque la marque avait recouvert la moitié de son corps."
    charles "Nous n’avions pas d’autre choix."
    self "C’est horrible…"

    hide charles
    show anne serieuse at center

    anne "Tu comprendras qu’aborder le sujet est devenu difficile pour Gaston."

    hide anne
    show charles normal at center

    charles "Bref. Je sais que tout ne doit pas être encore très clair pour toi, mais le temps presse."
    charles "Je vous  ai tous demandé de venir pour une raison précise."
    self "Tout le monde semble si sérieux d’un coup…"
    charles "Le but de l’attaque d’hier était de soutirer des informations à un officier Templier proche de Jacques de Molay"

    show charles serieux

    charles "Malgré ce qui est arrivé à Léon, c’était un succès."

    show charles normal

    charles "Suite à ça, nous avons réussi à connaître l’emploi du temps de Jacques de Molay pour les jours à venir."
    leon "Ce Templier l’a simplement révélé ?!"

    hide charles
    show anne serieuse at center

    anne "Léon… {w=0.5}Nous l’avons torturé puis égorgé."
    self "...Quoi ?!"
    self "Mais c’est horrible !"
    self "Je fais vraiment parti d’un groupe qui suit ce genre de pratiques ?!"

    hide anne
    show charles normal at center

    charles "Quoi qu’il en soit, nous savons que Jacques de Molay se trouve actuellement au Château de Fontainebleau."
    charles "De plus, il quittera le château ce soir pour un déplacement vers Paris."
    charles "Le délai est trop court pour qu’il prenne connaissance de la mort de l’officier Templier. Autrement dit, il ne se doutera de rien et ne changera pas son emploi du temps."
    charles serieux "..."
    charles "Évidemment, nous ne pouvons pas laissez passer une occasion pareille."
    charles "Nous allons l’attendre à la sortie du château et l’assassiner."
    charles "Léon, repose-toi pendant que nous nous occupons des préparatifs. Il faut que tu sois en forme ce soir."
    self "...moi ?!"
    self "Ils comptent me faire combattre dans mon état ?!"

    hide charles
    show helene serieuse at center

    helene "Charles, tu n’es pas sérieux ?"
    helene "Il est hors de question que Léon participe à cet assaut dans son état."

    hide helene
    show charles serieux at center

    charles "Léon est le plus doué parmi nous cinq pour les attaques furtives et rapides. Il est parfaitement qualifié pour porter le coup de grâce"
    charles "C’est à Jacques de Molay que nous nous attaquons, Hélène. Nous ne pouvons pas nous permettre d’y aller à moitié."

    hide charles
    show helene serieuse at center

    helene "C’est ridicule, il a perdu la mémoire ! Il ne sait même plus se battre !"

    hide helene
    show anne serieuse at center

    anne "..."

    pause 1.0
    with flash_blanc

    self "*bruit d’attaque contrée*" 
    leon "Ah…!"
    anne souriante "Vu l’aisance avec laquelle il a bloqué mon attaque, je pense qu’il est évident qu’il a gardé tous ses réflexes."

    hide anne
    show helene serieuse at center

    helene "Ça ne veut pas dire qu’il saura se servir d’une arme ! Aller se battre dans son état est juste dangereux !"

    hide helene
    show charles serieux at center

    $ charles("Nous attendons ce jour depuis si longtemps, nous devons mettre toutes les chances de notre côté. Léon doit ven", interact=False)
    pause 3.6
    
    with flash_blanc
    
    hide charles
    show helene inquiete at center

    helene "Léon ! Tu vas bien ?!"
    leon "…Non… J’ai subitement un énorme mal de crâne…"
    leon "..."
    leon "Je peux me reposer dans ma chambre ?"

    hide helene
    show charles serieux at center

    charles "..."
    charles "Bien sûr. Repose-toi bien."

    jump retour_chambre
# END FILE 03 - Réunion

# 04 - Chambre
label retour_chambre:
    scene decor noir with dissolve
    pause 3.0
    scene chambre with dissolve

    self "J’ai la tête qui tourne… et mon bras…"

    scene arm_gant with dissolve

    self "Ca me brûle sous ce gant…!"

    scene arm_1 with dissolve

    self "Qu… Qu’est-ce que c’est que ça !"
    self "Ce ne serait quand même pas… non, ça ne peut pas être ça !"
    self "C’était déjà là quand je me suis réveillé ?"
    self "Qu’est ce qu’il va m’arriver si les autres le découvrent ?"
    self "Ah ! De l’eau !"
    self "Ça veut pas partir…"
    self "Oh !"

    scene decor water with dissolve
    pause 2.0

    self "Alors c’est à ça que je ressemble… Je tire une de ces têtes..."
    self "D’ailleurs, j’ai aucune idée de l’âge que j’ai…"
    self "J’ai l’air plus vieux que je ne l’aurais espéré…"

    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "Il y a plusieurs choses que tu dois savoir sur les démons."

    pause 1.0
    scene decor chambre with flash_blanc

    self "Que… quoi ?!"
    self "C’était quoi, ça ?!"
    self "Une hallucination ?! Un souvenir ?!"

    pause 0.5
    self "*bruit de porte qui s’ouvre.*"
    show gaston normal at center
    with dissolve

    gaston "Eh, ça va? On m’a dit que tu te sentais mal."
    self "C’était limite mais j’ai pu remettre mon gant à temps..."
    gaston "Eh, tu m’écoutes ?"
    leon "Ne… ne t’inquiète pas, c’est juste un coup de fatigue, rien de bien grave."
    gaston serieux "Je voulais m'excuser d’être parti comme ça tout à l’heure. C’était maladroit de ma part"
    gaston "T’as perdu la mémoire quand même, c’était logique d’aborder ce sujet..."

    menu:
        "\"Il fallait y penser avant d’agir comme ça.\"":
           jump chambre_1_1
        "\"Ne t’inquiète pas, je comprends.\"":
           jump chambre_1_2

label chambre_1_1:
    leon "Il fallait y penser avant d’agir comme ça."
    gaston normal "Eh ! J’ai j’ai l’effort de m’excuser, tu pourrais me pardonner, quand même !"
    jump chambre_1_end

label chambre_1_2:
    leon "Ne t’inquiète pas, je comprends."
    gaston souriant "Merci, t’es vraiment un pote !"
    jump chambre_1_end

label chambre_1_end:
    
    pause 0.5
    show gaston normal at center
    self "*bruit de porte qui s’ouvre"

    show gaston normal at left with move
    show anne normal at right
    with dissolve

    anne "Ah, Gaston, tu es là."
    anne serieuse "On avait dit qu’on laisserait Léon se reposer."
    gaston "Je voulais juste voir comment il allait."
    anne normal "Peu importe. Charles veut te parler à propos des préparatifs de l’attaque de demain."
    gaston normal "Ça marche. Je vous laisse."

    hide gaston
    show anne at center with move

    anne "..."
    anne "Tu as vraiment mauvaise mine."
    anne "Pas étonnant qu’Hélène se soit énervée tout à l’heure quand Charles parlait de te faire participer à l’attaque."
    leon "Elle était persistante."
    anne souriante "Eh, c’est normal, elle t’aime, quand même !"
    leon "...!"
    leon "Vraiment ?!"
    anne normal "Oh… elle ne t’en a pas parlé ?"
    anne serieuse "Je vois… ton amnésie doit être très dure à vivre pour elle aussi."
    anne souriante "Hélène et toi êtes en couple depuis bien avant que vous n'ayez intégré l’Ordre."
    leon "Elle ne m’en a pas dit un mot…"
    anne normal "..."
    anne "J’ai quelque chose à proposer. Allons voir Charles."
    
    jump grande_salle
# END FILE 04 - Chambre

# 05 - Dialogue Charles
label grande_salle:
    
    scene decor noir with dissolve
    pause 3.0
    scene decor grande_salle
    show anne normal at left
    show charles normal at right
    with dissolve
 
    charles "Au village ?"
    anne "Oui. Je pense que Léon devrait sortir acheter des herbes médicinales. Ça calmera ses douleurs si jamais il doit participer à l’assaut de ce soir."
    anne souriante "Ça ne peut que lui faire du bien de prendre l’air !"
    charles "Il ne se souvient plus du chemin."
    anne normal "Hélène peut l’accompagner, ils y allaient toujours ensemble pour faire des provisions."
    anne "Après tout, leurs visages ne sont pas connus des Templiers, contrairement à ceux du reste de l’Ordre"

    charles "Anne… tu es consciente de l’importance de l’attaque de demain...?"
    charles "Léon ne peux pas vraiment nous aider à préparer quoi que ce soit dans son état, mais Hélène n’a pas de temps à perdre à gambader au village."
    helene "Je veux y aller !"
    anne souriante "Ah, tu es là !"

    hide anne
    hide charles
    show helene souriante at center
    with dissolve

    helene "S’il ne manque que moi, vous devriez pouvoir vous débrouiller à tout préparer, pas vrai ?"

    hide helene
    show charles normal at center

    charles "Même toi tu t’y mets…"
    charles "..." 
    charles "Tâchez de revenir rapidement."
    self "Visiblement, mon avis n’intéresse personne…"
    self "De toutes façon, je ne me sens pas vraiment à l’aise dans ce trou à rat. Ça ne peut que me faire du bien de sortir un peu."

    leon "Agh..."

    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "Les démons peuvent prendre une forme humaine."

    pause 1.0
    scene decor grande_salle with flash_blanc

    self "Ah… encore ça ?!"

    show helene inquiete at center with dissolve

    helene "Léon ! Tu vas bien ?!"
    leon "Ce n’est rien, j’ai juste des vertiges."
    helene "..."

    hide helene
    show charles serieux at center
    with dissolve

    charles "..."
    charles "Anne, Hélène, laissez-nous seuls un instant."

    hide charles
    show anne serieuse at left
    show helene inquiete at right
    with dissolve

    anne "Très bien."

    hide anne with dissolve
    hide helene with dissolve
    show charles normal at center
    with dissolve

    charles "Léon… tu es sûr que tout va bien ? N’essaye pas de ma faire croire que tu as juste de simples vertiges."
    charles "Tu peux nous en parler, tu sais."
    self "Je ne peux pas le laisser savoir ce que j’ai au bras…"
    leon "Je t’assure. Je suis juste un peu fatigué mais je ne me sens pas particulièrement mal."
    charles serieux "..."
    charles normal "Peu importe."
    charles "Ah, j’allais oublier !"
    charles dague "Cette dague, tu t’en sers toujours pour le combat."
    charles "Tu avais l’habitude de ne jamais t’en séparer."
    charles "Je te la rends."
    leon "Ah, merci."

    show charles normal

    self "Effectivement, elle rentre parfaitement dans le fourreau que j’ai à la taille."
    charles "Bien. Je vais prévenir Hélène. Vous allez pouvoir y aller."
    leon "Ah! Je…"
    charles "Oui ?"

    menu:
        "\"Demander si les démons peuvent prendre une forme humaine\"":
           jump dialogue_charles_1_1
        "Ne rien demander":
           jump dialogue_charles_1_2

label dialogue_charles_1_1:

    leon "Est-ce que les démons peuvent prendre une forme humaine ?"
    charles serieux "Où a-tu entendu une chose pareille ?"
    leon "Nulle part… je me posais juste la question."
    charles normal "Ne te pose pas des questions aussi insensées. Évidemment qu’ils ne peuvent pas."
    charles "Bref. Je vais aller prévenir Hélène."

    jump dialogue_charles_1_end

label dialogue_charles_1_2:

    leon "Non… rien…"
    charles "..."
    charles "Bon, je vais aller prévenir Hélène."

    jump dialogue_charles_1_end
    
label dialogue_charles_1_end:

    hide charles

    self "Tout à l’heure… mon bras…"

    scene arm_gant with dissolve
    pause 0.5
    scene arm_2 with dissolve

    self "La marque… elle s’est propagée…"

    jump sortie_start
# END FILE 05 - Dialogue Charles

# 06 - Sortie
label sortie_start:
    scene decor noir with dissolve
    pause 3.0
    scene entree
    show helene normal at center
    with dissolve

    helene "Ah, te voila !"
    helene "On n’a pas beaucoup eu l’occasion de parler seul à seul jusqu’à maintenant. J’espère cette perte de mémoire n’est pas trop difficile à vivre."

    menu:
        "\"Tout va bien\"":
           jump sortie_1_1
        "\"L’objectif de l’Ordre… Il est vraiment réaliste ?\"":
           jump sortie_1_2

label sortie_1_1:

    leon "Tout va bien." 
    leon "Tout le monde m’aide comme il le peut."
    helene souriante "Si quelque chose ne va pas, n’hésite pas à m’en parler !"

    jump sortie_1_end

label sortie_1_2:

    leon "L’objectif de l’Ordre… Il est vraiment réaliste ?"
    helene normal "Qu’est ce que tu veux dire par là ?"
    leon "Les membres risquent leur vie et vont jusqu’à utiliser la torture, tout ça pour assassiner une personne…"
    leon "Je comprends que Jacques de Molay est une ordure, mais le tuer va vraiment changer quelque chose ?"
    leon "Les démons ne vont pas disparaître… N’est-ce pas ?"
    helene "..."
    leon "..."
    self "Elle n’a pas l’air de vouloir répondre quoi que ce soit…"
    leon "Oublie ce que j’ai dis, je réfléchis trop…"
    helene "..."

    jump sortie_1_end
    
label sortie_1_end:

    helene souriante "Bref, allons-y."

    jump village_start
# END FILE 06 - Sortie

# 07 - Village
label village_start:
    scene decor noir with dissolve
    pause 3.0
    scene village
    show helene normal at center
    with dissolve

    helene "... et c’est à cette étale qu’on achète habituellement nos légumes."
    helene souriante "Ils vendent les meilleurs choux du coin !"
    helene normal "Par contre, leurs navets sont écoeurants..."
    helene "Ne va pas le répéter au marchand, il est persuadé du contraire."
    helene souriante "Tu n’aimes déjà pas les navets, alors imagine quand ils sont mauvais."
    leon "Je n’aime pas les navets ?"
    helene normal "En général, tu n’es pas difficile avec la nourriture, mais alors pour les navets par contre… !"
    helene souriante "Une fois, Anne en avait mit dans une soupe de légumes et tu as agis comme un gamin ! Tu as finis par aller te coucher en boudant sans rien manger."
    leon "Vraiment ? C’est embarrassant…"
    helene "C’est ce qui fait ton charme !"
    leon "..."
    leon "On devrait rentrer maintenant qu’on a les herbes, non ? Ils doivent nous attendre."
    helene "On peut bien traîner un peu, ce sont pas 10 minutes que vont changer quoi que ce soit."
    helene "..."
    helene normal "..."
    helene serieuse "Léon…"
    leon "Oui ?"
    helene "Je n’ai pas vraiment trouvé le moment pour t’en parler plus tôt, mais…"
    helene "Toi et moi… nous formons un couple."

    menu:

        "\"Oui… Anne l’a déjà mentionné.\"":
           jump village_1_1
        "\"Vraiment ?! Je n’en avais aucune idée…\"":
           jump village_1_2

label village_1_1:

    leon "Oui… Anne l’a déjà mentionné."
    helene normal "Vraiment ? Décidément, elle ne sait pas tenir sa langue !"
    helene "J’aurais préféré te l’annoncer moi-même…"
    helene "C’est aussi de ma faute, je n’ai pas eu le courage de t’en parler avant..."
    helene "Quoi qu’il en soit..."

    jump village_1_end

label village_1_2:

    leon "Vraiment ?! Je n’en avais aucune idée…"
    helene normal "Oui. Nous étions déjà ensemble bien avant de rejoindre l’Ordre."
    helene "Désolé… Je n’ai pas trouvé le courage de t’en parler plus tôt."
    
    jump village_1_end
    
label village_1_end:

    helene souriante "Tu es très important pour moi."
    helene normal "Et tu sais, je te connais mieux que quiconque."
    helene souriante "Je peux comprendre ce que tu ressens juste en te regardant !"
    helene normal "..."
    helene serieuse "Léon."
    helene "Tu me caches quelque chose d’important, pas vrai ?"
    self "Que…"
    self "Elle est au courant pour mon bras ?!"
    self "Non… Ce n’est pas possible..."
    self "Elle se doute juste de quelque chose..."
    self "Qu’est-ce que je dois faire ? Je dois lui en parler ?"
    self "Nous étions en couple… C’est probablement la seule à qui je peux me confier…"
    self "Mais ce que Charles a dit au sujet de ceux qui ont cette marque…"
    self "Non. C’est probablement une mauvaise idée de lui en parler."
    self "Ça ne peut que mal finir."
    self "Mais… Elle m’aime, pas vrai ?"
    self "Mais même si je lui en parle... {w=0.5}elle ne pourrait surement rien faire pour m’aider..."

    menu:

        "Lui parler de la marque au bras":
           jump village_2_1
        "Ne pas lui en parler":
           jump village_2_2

label village_2_1:

    leon "Hélène… Mon bras…"
    helene normal "Oui ?"
    leon "Je m’en suis rendu compte un peu plus tôt…"
    leon "..."
    leon "...Regarde par toi-même."

    pause 2.0
    show helene serieuse
    pause 2.0

    helene "..."
    helene "..."
    helene "..."
    helene "Nous rentrons."

    $ leon("H… Hélène, je t’assu", interact=False)
    pause 0.6
    helene "Nous rentrons."
    leon "Je ne voulais pas."
    helene "Nous rentrons."
    leon "..."    
   
    self "COMMENTAIRE: Cet ending n’étant pas encore intégré, la structure retourne sur la route où Léon n’a pas montré son bras à Hélène."
    jump briefing_endingAB_start


label village_2_2:

    leon "Je ne comprends pas de quoi tu parles. Je ne te cache rien."
    helene inquiete "Je vois… tu ne me fais pas encore confiance, pas vrai ?"
    helene "Je ne peux pas t’en vouloir puisque tu as tout oublié."
    helene normal "Peu importe."
    helene souriante "Si un jour tu dois me parler de quelque chose, tu sais que je serai là pour t’écouter."
    helene normal "Il commence à être tard. Nous devrions rentrer."
     
    jump briefing_endingAB_start
# END FILE 07 - Village


# 08 - Ending A/B - Briefing
label briefing_endingAB_start:

    scene decor noir with dissolve
    pause 3.0
    scene grande_salle
    show anne normal at center
    with dissolve

    anne "Ah, vous êtes revenus !"

    hide anne
    show charles serieux at center with dissolve

    charles "Vous en avez mis, du temps."

    hide charles
    show helene souriante at center

    helene "Vraiment ? On s’est dépêchés, pourtant."

    hide helene
    show charles normal at center

    charles "..."
    charles "Peu importe."
    charles "Maintenant que tout le monde est là, je vais vous expliquer le plan d’attaque de ce soir. Écoutez attentivement."

    scene decor noir with dissolve
    pause 2.0
    scene grande_salle
    show charles normal at center
    with dissolve

    charles "Une fois notre cible éliminée, on fuira en repassant par le chemin de notre venue puisqu’il sera déjà nettoyé."
    self "En gros, on s’infiltre en tuant les gardes Templiers sur notre chemin et on se cache dans la forêt jusqu’au passage de Jacques de Molay…"
    self "Ça paraît un peu simpliste, mais je suppose que le manque de temps et d’informations que nous avons nous empêche d’être mieux préparés…"
    charles "Maintenant que c’est fait, il est temps d’aborder un autre sujet important."
    charles "Léon est-ce que tu te sens assez bien pour participer ?"

    hide charles
    show helene serieuse
    with dissolve

    helene "Il est hors de question qu’il y aille dans son état."

    hide helene
    show gaston souriant at center
    with dissolve

    gaston "Tu exagères, il est déjà en pleine forme !"
    gaston "Il n’y a aucune raison qu’il ne vienne pas !"

    hide gaston
    show charles serieux at center
    with dissolve

    charles "Silence !"
    charles "Vous êtes fatiguants !"
    charles normal "Léon, tu es le principal concerné. C’est à toi de décider."
    charles "Souhaite-tu venir avec nous lors de l’attaque de demain ou non ?"

    menu:
        "Accepter":
           jump briefing_endingAB_1_1
        "Refuser":
           jump briefing_endingAB_1_2

label briefing_endingAB_1_1:

    leon "Je veux venir avec vous."
    charles "Bien. Le problème est réglé."
    
    hide charles
    show helene serieuse at center
    with dissolve

    self "Elle n’a vraiment pas l’air d’apprécier ma décision…"
    self "Désolé, Hélène, mais j’ai vraiment envie d’y aller."

    hide helene
    show charles normal at center
    with dissolve

    charles "Nous en avons fini. Nous partons dans moins d’une heure. Léon, profites-en pour bien te reposer. Il faut que tu sois en forme."


    jump soir_endingA_start

label briefing_endingAB_1_2:

    leon "Je préfère ne pas y aller."
    charles "..."
    charles "Bien. Le problème est réglé."

    hide charles
    show gaston souriant at center
    with dissolve

    gaston "Alors Léon, t’as peur ?"
    gaston "Ça te ressemble pas !"

    hide gaston
    show helene souriante at center
    with dissolve

    self "Elle a l’air soulagée…"

    hide helene
    show charles normal at center
    with dissolve

    charles "Nous en avons fini. Nous partons dans moins d’une heure. Il faut finir les derniers préparatifs."
    charles "Quant à toi Léon, tu resteras ici en attendant notre retour. Profites-en pour bien te reposer. "

    hide charles
    show gaston souriant at center
    with dissolve

    gaston "T’inquiète pas, on fêtera notre victoire quand on sera revenu !"

    jump soir_endingB_start
# END FILE 08 - Ending A/B - Briefing
    
    
    
# 09 - Ending A - Soir
label soir_endingA_start:

    scene decor noir with dissolve
    pause 3.0
    scene chambre with dissolve

    self "La journée passe tellement rapidement..."

    scene arm_gant with dissolve
    pause 0.5
    scene arm_3 with dissolve

    self "..."
    self "Ça s’est encore propagé…"
    self "*bruit de porte qui s’ouvre*"

    scene chambre
    show helene normal at center
    with dissolve

    helene "Léon, je…"
    helene serieuse "..."
    self "...Merde !"
    self "Elle a eu le temps de le voir ?!"
    helene "À plus tard."

    hide helene

    leon "Hélène ! Je… Ah…!"

    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "On peut reconnaître ces démons sous forme humaine à leurs yeux."

    pause 1.0
    scene chambre with flash_blanc

    self "Encore ce truc…"
    self "Plus important… {w=0.5}Hélène !"
    self "Elle a manifestement vu mon bras…"
    self "Elle ne va pas en parler aux autres... {w=0.5}pas vrai ?"
    self "Nous sommes en couple… {w=0.5}Elle ne ferait pas ça !"
    self "..."
    self "Enfin, j’espère…"
    self "..."

    jump massacre_endingA_start
# END FILE 09 - Ending A - Soir

# 09 - Ending B - Soir
label soir_endingB_start:

    scene decor noir with dissolve
    pause 3.0
    scene chambre with dissolve

    self "La journée passe tellement rapidement..."

    scene arm_gant with dissolve
    pause 0.5
    scene arm_3 with dissolve

    self "..."
    self "Ça s’est encore propagé…"
    self "*bruit de porte qui s’ouvre*"

    scene chambre
    show helene normal at center
    with dissolve

    helene "Léon, je…"
    helene serieuse "..."
    self "...Merde !"
    self "Elle a eu le temps de le voir ?!"
    helene "À plus tard."

    hide helene

    leon "Hélène ! Je… Ah…!"

    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "On peut reconnaître ces démons sous forme humaine à leurs yeux."

    pause 1.0
    scene chambre with flash_blanc

    self "Encore ce truc…"
    self "Plus important… {w=0.5}Hélène !"
    self "Elle a manifestement vu mon bras…"
    self "Elle ne va pas en parler aux autres... {w=0.5}pas vrai ?"
    self "Nous sommes en couple… {w=0.5}Elle ne ferait pas ça !"
    self "..."
    self "Enfin, j’espère…"
    self "..."

    jump massacre_endingB_start
# END FILE 09 - Ending B - Soir

# 10 - Ending A - Massacre
label massacre_endingA_start:

    scene decor noir with dissolve
    pause 5.0
    scene chambre
    show anne serieuse at center
    with dissolve

    anne "Léon, il est l’heure. Je t’attends à l’entrée."

    self "Je suis stressé et excité à la fois."
    self "..."
    self "Hélène…"
    self "Elle m’évite depuis tout à l’heure…"
    self "Vu que les autres agissent normalement, je ne pense pas qu’elle leur ait parlé de mon bras."

    scene arm_gant with dissolve
    pause 0.5
    scene arm_4 with dissolve

    self "Ça s’est encore propagé…"
    self "..."
    self "Ce grand maître des Templiers…"
    self "Peut-être qu’il connaît un moyen de supprimer cette malédiction ?"
    self "Ce n’est pas grand chose, mais c’est ma seule piste."
    self "Je vais devoir miser dessus…"

    scene decor noir with dissolve
    pause 3.0

    with shake
    self "*bruit de coeur transpercé*"
    charles "Bien. Nous avons réussi à franchir les gardes en les éliminant avant qu’ils ne donnent l’alerte."
    charles "Tout se passe comme prévu."

    scene chateau
    show charles masque
    with dissolve

    charles "Nous n’avons plus qu’à attendre le passage de Jacques de Molay."

    hide charles
    show anne masque at left
    show gaston masque at right
    with dissolve

    gaston "On va lui faire sa fête !"
    anne "Il ne devrait plus tarder, n’est-ce pas ?"

    hide gaston
    hide anne
    show charles normal at center
    with dissolve

    charles "Ah, des chevaux, au loin !"
    charles serieux "Restez sur vos gardes, c’est peut-être lui."

    hide charles
    show helene masque at center
    with dissolve

    helene "..."
    helene "J’aurais préféré ne pas avoir à en arriver là aussi tôt."

    hide helene
    show anne masque at center
    with dissolve

    anne "Qu’est-ce que tu veux dire pa…"

    self "*bruit de coeur transpercé*"
    with flash_rouge
    hide anne
    pause 0.5
    with shake
    self "*bruit de corps qui tombe au sol*"
    pause 1.5
    show helene_demon normal at center
    with dissolve

    helene "Et de un."
    self "... !"
    self "Cette chose… {w=0.5}C’est Hélène ?!"

    show helene at left with move
    show charles panique at right
    with dissolve

    charles "Anne… non… ce n’est pas possible !"
    self "Qu… qu’est-ce qu’il se passe ?!"

    hide charles
    show gaston masque at right
    with dissolve

    gaston "Ah !"
    gaston "Espèce de monstre ! Meurs !"
    helene_demon souriante "Tu es ridicule."

    self "*bruit de coeur transpercé*"
    with flash_rouge
    hide gaston with dissolve
    pause 0.5
    with shake
    self "*bruit de corps qui tombe au sol*"
    pause 0.5

    self "C’est un cauchemar !"

    hide helene
    show charles panique at center
    with dissolve

    charles "Anne…! Par pitié, ouvre les yeux !"

    self "*bruit de coeur transpercé*"
    with flash_rouge
    hide charles
    pause 0.5
    with shake
    self "*bruit de corps qui tombe au sol*"
    pause 0.5

    self "Qu’est-ce que je dois faire ? Fuir ?"
    self "Elle me rattraperait probablement sans difficulté…"

    show helene_demon normal

    helene "J’aurais préféré garder ma couverture plus longtemps, mais l’attaque se déroulait trop bien et je ne pouvais pas risquer la vie du grand maître."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donné !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene "Je devais récolter autant d’informations que possible sur les alliés de la résistance… On dirait que ma mission se termine prématurément."
    self "Elle se rapproche de plus en plus… Je n’ai plus le choix !"
    helene "Je m’attendais à plus de résistance… C’en est presque décevant."

    jump mort_de_helene_start
# END FILE 10 - Ending A - Massacre

# 10 - Ending B - Massacre
label massacre_endingB_start:

    scene decor noir with dissolve
    pause 5.0
    scene chambre with dissolve

    self "Voila… ils sont partis."
    self "Anne et Gaston sont venus, probablement pour me prévenir de leur départ, mais j’ai fait semblant de dormir."
    self "Je n’ai pas vraiment envie de parler à qui que ce soit depuis qu’Hélène a vu mon bras…"
    self "Hélène… elle n’est pas venue me voir depuis tout à l’heure..."
    self "Au moins, les autres avaient l’air d’agir normalement. Je ne pense pas qu’elle leur en ait parlé."

    scene arm_gant with dissolve
    pause 0.5
    scene arm_4 with dissolve

    self "J’ai l’impression que ça se propage de plus en plus vite."
    self "Je devrais peut-être m’enfuir d’ici…? Au moins, je ne leur causerais plus de problèmes…"
    self "...!"

    scene chambre with dissolve

    self "J’ai entendu quelque chose !"
    inconnu "...Léon !"
    self "Ça vient de l’entrée !"

    scene entree
    show gaston panique
    with dissolve

    gaston "Ah, te voila ! Dépêche-toi, on dégage en vitesse !"
    leon "Qu’est-ce qui se passe ?!"
    gaston "C’est Hélène ! C’est une saloperie de démone !"
    leon "Qu… {w=0.5}quoi ?!"
    gaston "Elle a tué Anne et Charles et si on ne se grouille pas, on est les suivants !"
    leon "Qu’est-ce que tu racontes ?!"
    $ gaston("Magne-toi, putain, on n’a pas le temps ! Elle va nou…", interact=False)
    pause 1.75

    self "*bruit de coeur transpercé*"
    with flash_rouge
    hide gaston
    pause 0.5
    with shake
    self "*bruit de corps qui tombe au sol*"
    pause 1.5
    show helene_demon normal at center with dissolve

    helene "Qu’est-ce qu’il est bruyant, celui-là."
    self "...!"
    self "... Gaston !"
    helene_demon sourire "Cet imbécile avait une chance de s’échapper mais il a préféré revenir ici pour te prévenir."
    self "Cette chose… C’est Hélène ?!"
    helene_demon normal "J’aurais préféré garder ma couverture plus longtemps, mais l’attaque se déroulait trop bien et je ne pouvais pas risquer la vie du grand maître."
    self "C’est vraiment elle ?!"
    helene "Je devais récolter autant d’informations que possible sur les alliés de la résistance… On dirait que ma mission se termine prématurément."
    self "Qu’est-ce que je dois faire ? Fuir ?"
    helene_demon souriante "J’ai commencé par attaquer Anne dans le dos, par surprise. C’était la plus dangereuse des trois, après tout !"
    self "Impossible, elle bloque l’entrée… et elle me rattraperait probablement sans difficulté."
    helene_demon normal "Elle est morte en un instant. Charles était complètement figé, je l’ai tué dans la foulée sans qu’il ne bouge d’un pouce."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donné !"
    helene "Gaston a essayé d’utiliser son artefact sur moi."
    helene_demon souriante "Quel crétin ! Comme si ça pouvait marcher sur un démon !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene_demon normale "Quand il a vu que ça n’avait aucun effet, cet imbécile s’est enfuit au seul endroit où il savait que j’allais le chercher."
    self "Elle se rapproche de plus en plus… Je n’ai plus le choix !"
    helene_demon souriante "Je ne l’aurais pas cru capable de courir aussi vite."

    jump mort_de_helene_start
# END FILE 10 - Ending B - Massacre

# 11 - Mort de Hélène
label mort_de_helene_start:

    self "*bruit de coeur transpercé*"
    scene decor rouge with dissolve
    pause 4.0
    scene mort_de_helene

    helene "L...Léon."
    self "...Ça a marché ? Une simple dague ?"
    helene "Tu dois… vivre…"
    self "Qu’est-ce qu’elle raconte ?"
    helene "Je suis vraiment heureuse… de tout ce qu’on a vécu ensemble…"
    self "Elle débloque !"

    scene decor noir with dissolve
    with shake
    self "*bruit de corps qui tombe au sol*"
    self "..."
    self "...elle ne respire plus."
    self "...!"
    self "Je me sens si apaisé tout d’un coup… Qu’est-ce que ?!"

    scene arm_gant with dissolve
    pause 0.5
    scene arm_0 with dissolve

    self "...!"
    self "Pourquoi elle n’est plus là ?!"
    self "Ah ! Ma mémoire !"
    self "..."
    self "Je me souviens…"
    self "Je me souviens de tout…"

    jump flashback_start
# END FILE 11 - Mort de Hélène

# 12 - Flashback
label flashback_start:

    pause 1.0
    scene decor noir with dissolve

    jacques_inconnu "{cps=*3}Demain, c’est le grand jour…{/cps}"
    jacques_inconnu "{cps=*3}Nous allons enfin pouvoir nous débarrasser de cette monarchie exécrable avant que ce soit elle qui s’attaque à nous.{/cps}"
    jacques_inconnu "{cps=*3}N’es-tu pas excité, Léon ?{/cps}"
    jacques_inconnu "{cps=*3}Tu t’es préparé tellement longtemps pour ce jour.{/cps}"
    jacques_inconnu "{cps=*3}...{/cps}"
    jacques_inconnu "{cps=*3}Il y a plusieurs choses que tu dois savoir sur les démons.{/cps}"

    scene eglise with dissolve
    pause 1.0

    jacques "Les démons peuvent prendre une forme humaine."
    jacques "C’est vraiment pratique, ils deviennent totalement méconnaissables."
    jacques "Cependant..."
    jacques "On peut reconnaître ces démons sous forme humaine à leurs yeux."
    jacques "Leurs yeux sont vairons, c’est à dire que chaque oeil a une couleur différente."
    jacques "Fait en sorte que nos ennemis ne s’en rendent jamais comptes."

    jacques "Autre chose. Un démon et son invocateur peuvent se transférer leur énergie vitale."
    jacques "Un démon peut même allonger la durée de vie de son invocateur de cette façon."
    jacques "Cependant, celui lui coûterait sa propre espérance de vie. Il n’a pas vraiment d’intérêt à faire ça."
    jacques "Mais tout cela est sans importance pour le moment."
    jacques "Nous sommes sur le point de vivre un moment historique !"
    jacques "Je suppose que tu te souviens de toutes les étapes du rituel ?"
    leon "Oui, grand maître."
    jacques "Parfait. Tu vas pouvoir passer à l’invocation de ton démon."
    jacques "Tu lui as déjà choisi un nom ?"
    leon "Oui, grand maître."
    leon "Si c’est un mâle, je l’appellerai Horace."
    leon "Et si c’est une femelle, je l’appellerai…"
    leon "Hélène."
    return
# END 12 - Flashback