#Monster Hunter Rise Sunbreak is owned by Capcom
Selection=input('Which Database, Monsters or Weapons')
if(Selection in 'Monsters'):
    print('Welcome, what monster class are you looking for?')
    Monster_Class=input('Flying Wyvern, Fanged Wyvern, Brute Wyvern, Bird Wyvern, Piscine Wyvern, Levianths, Fanged Beasts, Amphians, Carapaceons, Elder Dragons, Other')
    if(Monster_Class == 'Flying Wyvern'or Monster_Class in 'Flying'):
        Monster=input('Rathian, Rathalos, Basrios, Khezu, Nargacuga, Tigrex, Diablos, Barioth, Bazelgeuse, Espinas, Astalos')
        if(Monster == 'Rathian'):
                Apex=input('Base, Apex')
                if(Apex == 'Base'):
                    print('Monster: Rathian, Elements: Fire, Aliments: Fireblight, Poison, Deadly Poison, Weaknesses: Dragon, Breakable Parts: Head, Back, Wings, and tail')
                    print('Rare Materials: Rathian Plate, Rathian Ruby, Rathian Mantle')
                if(Apex == 'Apex'):
                    print('Monster: Apex Rathian, Elements: Fire, Aliments: Fireblight, Poison, Deadly Poison, Weaknesses: Dragon, Breakable Parts: Head, Back, Wings, and tail')    
                    print('Rare Materials: Rathian Plate, Rathian Ruby')
        if(Monster == 'Rathalos'):
                Apex=input('Base, Apex')
                if(Apex == 'Base'):
                    print('Monster: Rathalos, Elements: Fire, Aliments: Fireblight, Poison, Weaknesses: Dragon, Breakable Parts: Head, Back, Wings, and tail')
                    print('Rare Materials: Rathalos Plate, Rathalos Ruby, Rathalos Mantle')
                if(Apex == 'Apex'):
                    print('Monster: Apex Rathalos, Elements: Fire, Aliments: Fireblight, Poison, Weaknesses: Dragon, Breakable Parts: Head, Back, Wings, and tail')
                    print('Rare Materials: Rathalos Plate, Rathalos Ruby')
        if(Monster == 'Basrios'):
                print('Monster: Basrios, Elements: Fire, Aliments: Fireblight, Poison, Sleep, Weaknesses: Water, Breakable Parts: Head, Back, Wings, and tail')
        if(Monster == 'Khezu'):
                print('Monster: Khezu, Elements: Thunder, Aliments: Thunderblight, Paralysis, Weaknesses: Fire, Breakable Parts: Head, Body, and Legs')
        if(Monster == 'Nargacuga'):
            Variant=input('Nargacuga, Lucent')
            if(Variant == 'Nargacuga'):
                print('Monster: Nargacuga, Elements: None, Aliments: None, Weaknesses: Thunder, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
            if(Variant == 'Lucent Nargacuga' or Variant in 'Lucent'):
                print('Monster: Lucent Nargacuga, Elements: None, Aliments: Poison, Weaknesses: Thunder, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Large Wyvern Gem')
        if(Monster == 'Tigrex'):
                print('Monster: Tigrex, Elements: None, Aliments: None, Weaknesses: Thunder, Breakable Parts: Head, Back, Wings, and tail')
                print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
        if(Monster == 'Diablos'):
                Apex=input('Base, Apex')
                if(Apex == 'Base'):
                    print('Monster: Diablos, Elements: None, Aliments: None, Weaknesses: Ice, Breakable Parts: Head, Back, and tail')
                    print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
                if(Apex == 'Apex'):
                    print('Monster: Apex Diablos, Elements: None, Aliments: None, Weaknesses: Ice, Breakable Parts: Head, Back, and tail')
                    print('Rare Materials: Wyvern Gem')
        if(Monster == 'Barioth'):
                print('Monster: Barioth, Elements: Ice, Aliments: Iceblight, Weaknesses: Fire, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
        if(Monster == 'Bazelgeuse'):
            Variant=input('Base, Seething')
            if(Variant == 'Base'):
                print('Monster: Bazelgeuse, Elements: Fire, Aliments: Fireblight, Weaknesses: Thunder, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Bazelgeuse Gem, Bazelgeuse Mantle')
            if(Variant == 'Seething'):
                print('Monster: Seething Bazelgeuse, Elements: Fire, Aliments: Fireblight, Weaknesses: Ice, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Bazelgeuse Mantle')
        if(Monster == 'Espinas'):
                print('Monster: Espinas, Elements: Fire, Aliments: Fireblight, Poison, Paralysis, Weaknesses: Ice, Breakable Parts: Head, Back, Belly, Wings, and tail')
        if(Monster == 'Seregios'):
                print('Monster: Seregios, Elements: None, Aliments: Bleeding, Weaknesses: Thunder, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Seregios Lens')
        if(Monster == 'Astalos'):
                print('Monster: Astalos, Elements: Thunder, Aliments: Thunderblight, Paralysis, Weaknesses: Ice, Breakable Parts: Head, Back, Wings, and tail')
    if(Monster_Class == 'Fanged Wyvern'or Monster_Class in 'Fanged'):
        Monster=input('Tobi-Kadachi, Zinogre, Magnamalo, Lunagaron')
        if(Monster == 'Tobi-Kadachi'):
                print('Monster: Tobi-Kadachi, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Water, Breakable Parts: Head, Back, and tail')
                print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
        if(Monster == 'Zinogre'):
                Apex=input('Base, Apex')
                if(Apex == 'Base'):
                    print('Monster: Zinogre, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Ice, Breakable Parts: Head, Back, Legs, and tail')
                    print('Rare Materials: Zinogre Plate, Zinogre Ruby, Zinogre Mantle')
                if(Apex == 'Apex'):
                    print('Monster: Apex Zinogre, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Ice, Breakable Parts: Head, Back, Legs, and tail')
                    print('Rare Materials: Zinogre Plate, Zinogre Ruby')
        if(Monster == 'Magnamalo'):
            Variant=input('Magnamalo, Scorned')
            if(Variant == 'Magnamalo'):
                    print('Monster: Magnamalo, Elements: None, Aliments: Blast-Fireblight, Weaknesses: Water, Breakable Parts: Head, Back, Scutes, and tail')
                    print('Rare Materials: Magnamalo Plate, Purple Magna Orb, Magnamalo Orb')
            if(Variant == 'Scorned Magnamalo' or Variant in 'Scorned'):
                    print('Monster: Magnamalo, Elements: None, Aliments: Blast-Fireblight, Weaknesses: Water, Breakable Parts: Head, Back, Scutes, and tail')
        if(Monster == 'Lunagaron'):
                print('Monster: Lunagaron, Elements: Ice, Aliments: Iceblight, Weaknesses: Dragon, Breakable Parts: Head, and tail')
                print('Rare Materials: Lunagaron Frostjewel')
    if(Monster_Class == 'Brute Wyvern' or Monster_Class in 'Brute'):
        Monster=input('Barroth, Anjanath')
        if(Monster == 'Barroth'):
                print('Monster: Barroth, Elements: Water, Aliments: Waterblight, Muddy, Weaknesses: Water(Mud) Fire(No Mud), Breakable Parts: Head, Back, Arms, and tail')
                print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
        if(Monster == 'Anjanath'):
                print('Monster: Anjanath, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Legs, and tail')
                print('Rare Materials: Anjanath Plate, Anjanath Gem, Anjanath Mantle')
    if(Monster_Class == 'Bird Wyvern' or Monster_Class in 'Bird'):
        Monster=input('Great Izuchi, Great Baggi, Great Wroggi, Kulu-Ya-Ku, Aknosom, Pukei-Pukei')
        if(Monster == 'Great Izuchi'):
            print('Monster: Great Izuchi, Elements: None, Aliments: None, Weaknesses: Thunder, Breakable Parts: Head and Tail')
            print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
        if(Monster == 'Great Baggi'):
            print('Monster: Great Baggi, Elements: None, Aliments: Sleep, Weaknesses: Fire, Breakable Parts: Head')
            print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
        if(Monster == 'Great Wroggi'):
            print('Monster: Great Wroggi, Elements: None, Aliments: Poison, Weaknesses: Ice, Breakable Parts: Head')
            print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
        if(Monster == 'Kulu-Ya-Ku'):
                print('Monster: Kulu-Ya-Ku, Elements: None, Aliments: None, Weaknesses: Water, Breakable Parts: Head and Arms')
                print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
        if(Monster == 'Aknosom'):
                print('Monster: Aknosom, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
        if(Monster == 'Pukei-Pukei'):
                print('Monster: Pukei-Pukei, Elements: None, Aliments: None, Weaknesses: Thunder, Breakable Parts: Head, Wings, and Tail')
                print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
    if(Monster_Class == 'Piscine Wyvern'or Monster_Class in 'Piscine'):
        Monster=input('Jyuratodus')
        if(Monster == 'Jyuratodus'):
            print('Monster: Jyuratodus, Elements: Water, Aliments: Waterblight, Muddy, Weaknesses: Water (Mud)/Thunder (No Mud), Breakable Parts: Head, Back, and tail')
    if(Monster_Class == 'Levianths'):
        Monster=input('Mizutsune, Somnacanth, Royal Ludroth, Almudron')
        if(Monster == 'Mizutsune'):
            Apex=input('Base, Apex')
            if(Apex == 'Base'):
                print('Monster: Mizutsune, Elements: Water, Aliments: Waterblight, Bubble, Weaknesses: Thunder, Breakable Parts: Head, Front Legs, and tail')
                print('Rare Materials: Mizutsune Plate, Mizutsune Ruby, Mizutsune Mantle')
            if(Apex == 'Apex'):
                print('Monster: Apex Mizutsune, Elements: Water, Aliments: Waterblight, Fire-Blastblight, Bubble, Weaknesses: Thunder, Breakable Parts: Head, Front Legs, and tail')
                print('Rare Materials: Mizutsune Plate, Mizutsune Ruby')
        if(Monster == 'Somnacanth'):
            Subspecies=input('Base or Aurora')
            if(Subspecies == 'Base'):
                print('Monster: Somnacanth, Elements: None, Aliments: Sleep, Weaknesses: Thunder, Breakable Parts: Head, Arms, and tail')
                print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
            if(Subspecies == 'Aurora'):
                print('Monster: Aurora Somnacanth, Elements: Ice, Aliments: Iceblight, Weaknesses: Fire, Breakable Parts: Head, Arms, and tail')
                print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
        if(Monster == 'Royal Ludroth'):
            print('Monster: Royal Ludroth, Elements: Water, Aliments: Waterblight, Weaknesses: Fire, Breakable Parts: Head, Creat, and tail')
            print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
        if(Monster == 'Almudron'):
            Subspecies=input('Base or Magma')
            if(Subspecies == 'Base'):
                print('Monster: Almudron, Elements: Water, Aliments: Waterblight, Muddy, Weaknesses: Fire, Breakable Parts: Head, Back, and tail')
                print('Rare Materials: Almudron Plate, Golden Almudron Orb, Almudron Mantle')
            if(Subspecies == 'Magma'):
                print('Monster: Magma Almudron, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Back, and tail')
                print('Rare Materials: Magmadron Mantle')
    if(Monster_Class == 'Fanged Beasts'or Monster_Class in 'Beasts'):
        Monster=input('Rajang, Bishaten, Arzuros, Lagombi, Volvidon, Goss Harag')
        if(Monster == 'Rajang'):
            Variant=input('Rajang, Furious')
            if(Variant == 'Rajang'):
                print('Monster: Rajang, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Ice, Breakable Parts: Head, Arms, and tail')
                print('Rare Materials: Beast Gem, Large Beast Gem')
            if(Variant == 'Rajang' or Variant in 'Furious'):
                print('Monster: Furious Rajang, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Ice, Breakable Parts: Head, and Arms')
                print('Rare Materials: Large Beast Gem')
        if(Monster == 'Bishaten'):
            Subspecies=input('Base or Blood Orange')
            if(Subspecies == 'Base'):
                    print('Monster: Bishaten, Elements: None, Aliments: Paralysis, Poison, Weaknesses: Dragon, Breakable Parts: Head, Wings, and tail')
                    print('Rare Materials: Beast Gem, Large Beast Gem')
            if(Subspecies == 'Blood Orange' or Subspecies in 'Blood Orange'):
                    print('Monster: Blood Orange Bishaten, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Wings, and tail')
                    print('Rare Materials: Large Beast Gem')
        if(Monster == 'Arzuros'):
            Apex=input('Base, Apex')
            if(Apex == 'Base'):
                print('Monster: Arzuros, Elements: None, Aliments: None, Weaknesses: Fire, Breakable Parts: Arms')
                print('Rare Materials: Beast Gem, Large Beast Gem')
            if(Apex == 'Apex'):
                print('Monster: Apex Arzuros, Elements: None, Aliments: None, Weaknesses: Ice, Breakable Parts: Arms')
                print('Rare Materials: Beast Gem')
        if(Monster == 'Lagombi'):
            print('Monster: Lagombi, Elements: Ice, Aliments: Iceblight, Weaknesses: Fire, Breakable Parts: Head, and Belly')
            print('Rare Materials: Beast Gem, Large Beast Gem')
        if(Monster == 'Volvidon'):
                print('Monster: Volvidon, Elements: None, Aliments: Stench, Weaknesses: Water, Breakable Parts: Back')
                print('Rare Materials: Beast Gem, Large Beast Gem')
        if(Monster == 'Goss Harag'):
            print('Monster: Goss Harag, Elements: Ice, Aliments: Iceblight, Weaknesses: Fire, Breakable Parts: Head, and Arms')
            print('Rare Materials: Beast Gem, Large Beast Gem')
        if(Monster == 'Garangolm'):
            print('Monster: Garangolm, Elements: , Aliments: , Weaknesses: Thunder, Breakable Parts: Head, and Arms')
            print('Rare Materials: Large Beast Gem')
    if(Monster_Class == 'Amphians'):
        Monster=input('Tetradon')
        if(Monster == 'Tetradon'):
            print('Monster: Tetradon, Elements: Water, Aliments: Waterblight, Weaknesses: Thunder, Breakable Parts: Head, and Arms')
    if(Monster_Class == 'Carapaceons'):
        Monster=input('Daimyo Hermitaur, Shogun Ceanataur')
        if(Monster == 'Daimyo Hermitaur'):
            print('Monster: Daimyo Hermitaur, Elements: Water, Aliments: Waterblight, Weaknesses: Ice, Breakable Parts: Arms and Shell')
        if(Monster == 'Shogun Ceanataur'):
            print('Monster: Shogun Ceanataur, Elements: None, Aliments: Bleeding, Weaknesses: Ice, Breakable Parts: Arms, and Shell')
    if(Monster_Class == 'Temnoceran'or Monster_Class in 'Temnoceran'):
        Monster=input('Rakna-Kadaki')
        if(Monster == 'Rakna-Kadaki'):
            Subspecies=input('Base or Pyre')
            if(Subspecies == 'Base'):
                    print('Monster: Rakna-Kadaki, Elements: Fire, Aliments: Fireblight, Webbed, Weaknesses: Ice, Breakable Parts: Head, Claws Legs, and Abdomen')
            if(Subspecies == 'Pyre'):
                    print('Monster: Pyre Rakna-Kadaki, Elements: Fire, Aliments: Fireblight, Blastblight, Webbed, Weaknesses: Water, Breakable Parts: Head, Claws, Legs, and Abdomen')
    if(Monster_Class == 'Elder Dragons'):
        Monster=input('Chameleos, Kushala Doara, Teostra, Ibushi, Narwa, Crimson Glow Valstrax, Shaguru Magala, Malzeno')
        if(Monster == 'Chameleos'):
            print('Monster: Chameleos, Elements: None, Aliments: Poison, Severe Poison, Weaknesses: Fire, Breakable Parts: Head, Wings, and tail')
            print('Rare Materials: Chameleos Gem, Elder Dragon Gem')
        if(Monster == 'Kushala Doara' or Monster in 'Kushala'):
            print('Monster: Kushala Doara, Elements: Ice, Dragon, Aliments: , Weaknesses: Thunder/Dragon, Breakable Parts: Head, Wings, and tail')
            print('Rare Materials: Kushala Gem, Elder Dragon Gem')
        if(Monster == 'Teostra'):
            print('Monster: Teostra, Elements: Fire, Aliments: Fireblight, Blastblight, Weaknesses: Water/Ice, Breakable Parts: Head, Wings, and tail')
            print('Rare Materials: Teostra Gem, Elder Dragon Gem')
        if(Monster == 'Ibushi'):
            print('Monster: Wind Serpent Ibushi, Elements: Fire, Aliments: Fireblight, Blastblight, Weaknesses: Water/Ice, Breakable Parts: Head, Wings, and tail')
            print('Rare Materials: Rathian Plate, Rathian Ruby, Rathian Mantle')
        if(Monster == 'Narwa'):
            Variant=input('Narwa, Allmother Narwa')
            if(Variant == 'Narwa'):  
                print('Monster: Thunder Serpent Narwa, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Dragon, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Rathian Plate, Rathian Ruby, Rathian Mantle')
            if(Variant == 'Allmother Narwa'):
                print('Monster: Narwa the Allmother, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Dragon, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Orb of Orgin, Mantle of Orgin')
        if(Monster == 'Crimson Glow Valstrax' or Monster in 'Valstrax'):
            print('Monster: Crimson Glow Valstrax, Elements: Dragon, Aliments: Dragonblight, Weaknesses: Fire/Water/Thunder/Ice, Breakable Parts: Head, Wings, Back and tail')
            print('Rare Materials: Valstrax Gem, Valstrax Mantle')
        if(Monster == 'Shaguru Magala' or Monster in 'Shaguru'):
                print('Monster: Shaguru Magala, Elements: None, Aliments: Frenzy, Weaknesses: Dragon, Breakable Parts: Head, Wingarms, and tail')
                print('Rare Materials: Shaguru Mantle')
        if(Monster == 'Malzeno'):
                print('Monster: Malzeno, Elements: Dragon, Aliments: Dragonblight, Bloodblight, Weaknesses: Dragon, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Malzeno Bloodstone')
        if(Monster == 'Gaismagorm'):
                print('Monster: Gaismagorm, Elements: None, Aliments: Quiro, Weaknesses: Dragon, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Abyssal Dragonspire')
    if(Monster_Class == 'Others'):
        Monster=input('Gore Magala')
        if(Monster == 'Gore Magala'):
                print('Monster: Gore Magala, Elements: None, Aliments: Frenzy, Weaknesses: Fire, Breakable Parts: Head, Feelers, Wingarms, and tail')
                print('Rare Materials: Gore Mantle')
if(Selection in 'Weapons'):
    print('Welcome, what weapon class are you looking for?')
    Weapon_Class=input('Cutting, Blunt, Ammo')
    if(Weapon_Class == 'Cutting'):
      Weapon=input('Great Sword, Long Sword, Sword and Shield, Dual Blades, Charge Blade, Switch Axe, Lance, Gunlance, Insect Glaive')
      if(Weapon == 'Great Sword' or Weapon.lower == 'GS'):
                print('Weapon: Great Sword')
                print('A weapon designed with Heavy, Powerful Swings with three charges.')
                print('The Geat Sword is designed with heavy damage in mind as well.')
                print('The Great Sword is cabable of protecting the user due the large blade being cabable to blocking attacks')
                print('Important Skills')
                print('Focus, Partbreaker, Razor Sharp')
                print('Introduced in Monster Hunter')
      if(Weapon == 'Long Sword' or Weapon.lower == 'LS'):
                print('Weapon: Long Sword')
                print('A weapon designed with Heavy, Powerful Swings with three charges.')
                print('Important Skills')
                print('Focus, Partbreaker, Razor Sharp')
                print('Introduced in Monster Hunter Freedom 2')
      if(Weapon == 'Sword and Shield' or Weapon.lower == 'SnS'):
                print('Weapon: Sword and Shield')
                print('A weapon designed with Heavy, Powerful Swings with three charges.')
                print('Important Skills')
                print('Focus, Partbreaker, Razor Sharp')
                print('Introduced in Monster Hunter')
      if(Weapon == 'Dual Blades'):
                print('Weapon: Dual Blades')
                print('Dual Blades are a pair of blades cabaple of quick and fluid attacks.')
                print('Important Skills') 
                print('Focus, Power Prolonger, Partbreaker, Razor Sharp')
                print('Introduced in Monster Hunter')
      if(Weapon == 'Charge Blade' or Weapon.lower == 'CB'):
                print('Weapon: Charge Blade')
                print('A weapon designed with Heavy, Powerful Swings with three charges.')
                print('Important Skills')
                print('Focus, Artillery, Razor Sharp')
                print('Introduced in Monster Hunter 4')
      if(Weapon == 'Switch Axe'):
                print('Weapon: Switch Axe')
                print('A weapon designed with Heavy, Powerful Swings with three charges.')
                print('Important Skills')
                print('Focus, Partbreaker, Razor Sharp')
                print('Introduced in Monster Hunter Tri')
      if(Weapon == 'Lance'):
                print('Weapon: Lance')
                print('The Lance is a large lance with a Big shield made for blocking attacks')
                print('')
                print('Important Skills')
                print('Guard, Guard up, Offensive Guard, Razor Sharp')
                print('Introduced in Monster Hunter')
      if(Weapon == 'Gunlance' or Weapon.lower == 'GL'):
                print('Weapon: Gunlance')
                print('A weapon designed with Heavy, Powerful Swings with three charges.')
                print('Important Skills')
                print('Guard, Artillery, Evade Extender, Load Shells, Razor Sharp, Attack Boost Speed Sharpening, Flinch Free')
                print('Introduced in Monster Hunter 2')
      if(Weapon == 'Insect Glaive' or Weapon.lower == 'IG'):
                print('Weapon: Insect Glaive')
                print('The Insect Glaive is a double-ended rod is capable of quick and fluid attacks.')
                print('It also allows the hunter to pole vault at any time, allowing Jumping Attacks to be performed at will.')
                print('Coming with the rod is a giant insect called the Kinsect, which can be sent out to attack monsters')
                print('and gather extracts from said monster.')
                print('Red Extract: Increases attack')
                print('White Extract: Increases mobility')
                print('Orange Extract: Increases defense')
                print('Triple is achieved by collecting all three extracts.')
                print('Important Skills')
                print('Focus, Partbreaker, Razor Sharp')
                print('Introduced in Monster Hunter 4')
    if(Weapon_Class == 'Blunt'):
      Weapon=input('Hammer, Hunting Horn')
      if(Weapon == 'Hammer'):
                print('Weapon: Hammer')
                print('A weapon designed with Heavy, Powerful Swings with three charges and the ability to Stun Targets.')
                print('Important Skills')
                print('Focus, Partbreaker, Slugger, Razor Sharp')
                print('Introduced in Monster Hunter')
      if(Weapon == 'Hunting Horn' or Weapon.lower == 'HH'):
                print('Weapon: Hunting Horn')
                print('A weapon designed with Heavy, Powerful Swings with three charges and the ability to Stun Targets.')
                print('Important Skills')
                print('Partbreaker, Slugger,Razor Sharp')
                print('Introduced in Monster Hunter Portable')
    if(Weapon_Class == 'Ammo'):
      Weapon=input('Light Bowgun, Heavy Bowgun, Bow')
      if(Weapon == 'Light Bowgun' or Weapon.lower == 'LBG' or Weapon.lower == 'LB' or Weapon.lower == 'LG'):
                print('Weapon: Light Bowgun')
                print('A weapon designed with Heavy, Powerful Swings with three charges and the ability to Stun Targets.')
                print('Important Skills')
                print('Focus, Partbreaker, Slugger, Spare Shot')
                print('Introduced in Monster Hunter')
      if(Weapon == 'Heavy Bowgun' or Weapon.lower == 'HBG' or Weapon.lower == 'HB' or Weapon.lower == 'HG'):
                print('Weapon: Heavy Bowgun')
                print('A weapon designed with Heavy, Powerful Swings with three charges and the ability to Stun Targets.')
                print('Important Skills')
                print('Focus, Partbreaker, Slugger, Spare Shot')
                print('Introduced in Monster Hunter')
      if(Weapon == 'Bow'):
                print('Weapon: Bow')
                print('A weapon designed with Heavy, Powerful Swings with three charges and the ability to Stun Targets.')
                print('Important Skills')
                print('Focus, Spare Shot')
                print('Introduced in Monster Hunter 2')
