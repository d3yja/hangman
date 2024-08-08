stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''








word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]
hint = [
    # Hints for 'abruptly'
    ["Happens suddenly", "Not gradual", "Without warning", "Quick change", "Unexpected shift"],

    # Hints for 'absurd'
    ["Ridiculously unreasonable", "Completely silly", "Hard to believe", "Outrageously funny", "Strangely illogical"],

    # Hints for 'abyss'
    ["Deep hole", "Bottomless pit", "Extremely deep", "Chasm", "Endless void"],

    # Hints for 'affix'
    ["To attach", "Add something", "Fix something", "Stick on", "Join something"],

    # Hints for 'askew'
    ["Not straight", "Slanted", "Off center", "Tilted", "Crooked"],

    # Hints for 'avenue'
    ["Wide street", "Urban road", "Major thoroughfare", "Street name", "Boulevard"],

    # Hints for 'awkward'
    ["Uncomfortable", "Clumsy", "Lacking grace", "Embarrassing situation", "Uneasy"],

    # Hints for 'axiom'
    ["Self-evident truth", "Basic principle", "Fundamental concept", "Accepted truth", "Starting point of reasoning"],

    # Hints for 'azure'
    ["Sky color", "Light blue", "Clear blue", "Bright blue", "Shade of blue"],

    # Hints for 'bagpipes'
    ["Scottish instrument", "Wind instrument", "Hose and pipes", "Played with a bag", "Traditional music"],

    # Hints for 'bandwagon'
    ["Popular trend", "Join the crowd", "Follow the trend", "Support a popular cause", "Enthusiastic participation"],

    # Hints for 'banjo'
    ["Stringed instrument", "Four or five strings", "Played with a pick", "Often in folk music", "Has a circular body"],

    # Hints for 'bayou'
    ["Swampy area", "Slow-moving water", "Southern US marsh", "Wetlands", "Part of a river system"],

    # Hints for 'beekeeper'
    ["Person who keeps bees", "Honey producer", "Apiculturist", "Maintains hives", "Works with bees"],

    # Hints for 'bikini'
    ["Two-piece swimsuit", "Beachwear", "Summer clothing", "Popular swimwear", "Women's swimwear"],

    # Hints for 'blitz'
    ["Rapid attack", "Intense effort", "Lightning strike", "Quick and overwhelming", "Military term"],

    # Hints for 'blizzard'
    ["Heavy snowstorm", "Strong winds and snow", "Winter weather", "Snowfall with wind", "Extreme snow conditions"],

    # Hints for 'boggle'
    ["Confuse someone", "Bewilder", "Puzzle", "Challenge the mind", "Mental exercise"],

    # Hints for 'bookworm'
    ["Avid reader", "Lover of books", "Bibliophile", "Spends time reading", "Book enthusiast"],

    # Hints for 'boxcar'
    ["Train car type", "Cargo carriage", "Railroad vehicle", "Used for freight", "Box-shaped car"],

    # Hints for 'boxful'
    ["Container full", "Amount in a box", "Complete box", "Box filled up", "All the way full"],

    # Hints for 'buckaroo'
    ["Cowboy term", "Ranch worker", "Rides horses", "Western US", "Rodeo participant"],

    # Hints for 'buffalo'
    ["Large mammal", "Bison", "Native American symbol", "American plains", "Big horns"],

    # Hints for 'buffoon'
    ["Foolish person", "Clown", "Silly behavior", "Jester", "Comical figure"],

    # Hints for 'buxom'
    ["Full-figured", "Curvaceous", "Well-endowed", "Voluptuous", "Larger bust"],

    # Hints for 'buzzard'
    ["Bird of prey", "Scavenger", "Large raptor", "Feeding on carrion", "Often seen soaring"],

    # Hints for 'buzzing'
    ["Insect sound", "Continuous noise", "Like a bee", "Vibrating sound", "Persistent hum"],

    # Hints for 'buzzwords'
    ["Popular terms", "Catchphrases", "Trending words", "Jargon", "Popular expressions"],

    # Hints for 'caliph'
    ["Islamic ruler", "Leader of a caliphate", "Historical title", "Religious and political leader", "Successor to Muhammad"],

    # Hints for 'cobweb'
    ["Spider's web", "Insect web", "Old spider web", "Dusty web", "Found in corners"],

    # Hints for 'cockiness'
    ["Excessive pride", "Arrogance", "Overconfidence", "Self-importance", "Showing off"],

    # Hints for 'croquet'
    ["Lawn game", "Hit balls through wickets", "Played with mallets", "Outdoor sport", "British pastime"],

    # Hints for 'crypt'
    ["Underground chamber", "Burial place", "Tomb", "Historic grave", "Vault"],

    # Hints for 'curacao'
    ["Island in the Caribbean", "Dutch overseas territory", "Blue liqueur", "Popular vacation spot", "Part of the ABC islands"],

    # Hints for 'cycle'
    ["Series of events", "Repetitive sequence", "Circular pattern", "Regular occurrence", "Repeat pattern"],

    # Hints for 'daiquiri'
    ["Cocktail", "Rum-based drink", "Popular in Cuba", "Can be fruity", "Served chilled"],

    # Hints for 'dirndl'
    ["Traditional dress", "Austrian attire", "Bavarian clothing", "Women’s folk costume", "Popular in Oktoberfest"],

    # Hints for 'disavow'
    ["To deny responsibility", "Reject association", "Refuse to acknowledge", "Say something is not true", "Distance oneself"],

    # Hints for 'dizzying'
    ["Causing vertigo", "Making someone dizzy", "Unsettling", "Spinning feeling", "Confusing sensation"],

    # Hints for 'duplex'
    ["Two units", "Type of house", "Two-family dwelling", "Two-part structure", "Apartment with two levels"],

    # Hints for 'dwarves'
    ["Mythical beings", "Small people", "Legendary characters", "Short in stature", "Often in fantasy stories"],

    # Hints for 'embezzle'
    ["Steal money", "Misappropriate funds", "Fraudulent use", "Illegal financial gain", "Dishonest theft"],

    # Hints for 'equip'
    ["Provide with tools", "Prepare with necessary items", "Outfit for a task", "Set up with gear", "Supply with equipment"],

    # Hints for 'espionage'
    ["Spying", "Secret intelligence", "Covert operations", "Government secrets", "Undercover activities"],

    # Hints for 'euouae'
    ["Medieval musical term", "Six-letter word", "Unique vowel pattern", "Musical cadence", "Used in Gregorian chant"],

    # Hints for 'exodus'
    ["Mass departure", "Large-scale exit", "Leaving in great numbers", "Historic event", "Migration of people"],

    # Hints for 'faking'
    ["Pretending", "Not genuine", "False appearance", "Deception", "Simulating something"],

    # Hints for 'fishhook'
    ["Used for fishing", "Catches fish", "Baited with a hook", "Small curved metal", "Fishing gear"],

    # Hints for 'fixable'
    ["Able to be repaired", "Capable of being fixed", "Not permanently damaged", "Repairable", "Can be corrected"],

    # Hints for 'fjord'
    ["Glacial valley", "Narrow sea inlet", "U-shaped coastal feature", "Scenic waterway", "Norwegian landscape"],

    # Hints for 'flapjack'
    ["Pancake type", "Breakfast food", "Made with oats", "Sweet and chewy", "British treat"],

    # Hints for 'flopping'
    ["Falling heavily", "Failing badly", "Dropping down", "To flop over", "Not successful"],

    # Hints for 'fluffiness'
    ["Soft and airy", "Light texture", "Puffed up", "Not dense", "Feathery quality"],

    # Hints for 'flyby'
    ["Passing closely", "Aircraft maneuver", "Brief visit", "Quick aerial pass", "Close flyover"],

    # Hints for 'foxglove'
    ["Flowering plant", "Bell-shaped blooms", "Toxic plant", "Used in gardens", "Common in wild"],

    # Hints for 'frazzled'
    ["Exhausted", "Tired and stressed", "Worn out", "Overwhelmed", "Burned out"],

    # Hints for 'frizzled'
    ["Curled up hair", "Wavy texture", "Kinked hair", "Hair not smooth", "Messy appearance"],

    # Hints for 'fuchsia'
    ["Pinkish-purple color", "Color name", "Flowering plant", "Vivid shade", "Bright and bold"],

    # Hints for 'funny'
    ["Causing laughter", "Amusing", "Humorous", "Comical", "Bringing joy"],

    # Hints for 'gabby'
    ["Talkative", "Chatty", "Verbose", "Likes to talk", "Loquacious"],

    # Hints for 'galaxy'
    ["System of stars", "Milky Way", "Astronomical system", "Star cluster", "Spiral or elliptical"],

    # Hints for 'galvanize'
    ["Stimulate action", "Encourage activity", "Excite", "Inspire", "Shock into action"],

    # Hints for 'gazebo'
    ["Outdoor pavilion", "Garden structure", "Open-sided building", "Used for relaxation", "Decorative shelter"],

    # Hints for 'giaour'
    ["Historical term", "Non-Muslim person", "Used in Ottoman Empire", "Derogatory term", "Old usage"],

    # Hints for 'gizmo'
    ["Small device", "Useful gadget", "Mechanical contraption", "Ingenious tool", "Tech invention"],

    # Hints for 'glowworm'
    ["Bioluminescent insect", "Produces light", "Nighttime creature", "Glowing in the dark", "Larval stage light"],

    # Hints for 'glyph'
    ["Symbol or character", "Written mark", "Ancient script", "Carved figure", "Hieroglyph"],

    # Hints for 'gnarly'
    ["Twisted or bent", "Cool or impressive", "Complex", "Slang for great", "Rough appearance"],

    # Hints for 'gnostic'
    ["Knowledge-based", "Religious sect", "Spiritual enlightenment", "Ancient belief system", "Esoteric knowledge"],

    # Hints for 'gossip'
    ["Idle talk", "Rumors", "Unverified information", "Social chatter", "Spreading news"],

    # Hints for 'grogginess'
    ["Feeling dazed", "Lack of alertness", "Confused state", "Disoriented", "After waking up"],

    # Hints for 'haiku'
    ["Japanese poem", "Three-line verse", "Nature-themed", "Traditional form", "Seventeen syllables"],

    # Hints for 'haphazard'
    ["Random and careless", "Lacking organization", "Disorderly", "Unplanned", "Messy approach"],

    # Hints for 'hyphen'
    ["Punctuation mark", "Joins words", "Short dash", "Used in compound words", "Separates syllables"],

    # Hints for 'iatrogenic'
    ["Caused by medical treatment", "Resulting from therapy", "Doctor-induced", "Medical complications", "Unintended side effect"],

    # Hints for 'icebox'
    ["Old-style refrigerator", "Keeps things cold", "Predecessor to fridge", "Used for ice storage", "Cooling container"],

    # Hints for 'injury'
    ["Physical harm", "Damage to body", "Wound or cut", "Result of an accident", "Trauma"],

    # Hints for 'ivory'
    ["Material from elephant tusks", "White and smooth", "Used in carvings", "Color name", "Historical artifact"],

    # Hints for 'ivy'
    ["Climbing plant", "Evergreen vine", "Common on walls", "Has small leaves", "Can be invasive"],

    # Hints for 'jackpot'
    ["Big prize", "Winning the lottery", "Huge reward", "Large payout", "Gambling term"],

    # Hints for 'jaundice'
    ["Yellowing of skin", "Medical condition", "Liver disease symptom", "Yellowish discoloration", "Chronic illness"],

    # Hints for 'jawbreaker'
    ["Hard candy", "Large sweet", "Candy that lasts long", "Colorful sphere", "Tough to chew"],

    # Hints for 'jaywalk'
    ["Cross the street illegally", "Walk across traffic", "Pedestrian offense", "Cross outside a crosswalk", "Breaking traffic rules"],

    # Hints for 'jazziest'
    ["Most stylish", "Funky and lively", "Very cool", "Full of flair", "Trendy"],

    # Hints for 'jazzy'
    ["Lively and stylish", "Full of jazz", "Trendy and cool", "Energetic music", "Fashionable"],

    # Hints for 'jelly'
    ["Sweet spread", "Made from fruit", "Clear or semi-transparent", "Used on bread", "Gel-like consistency"],

    # Hints for 'jigsaw'
    ["Puzzle type", "Piece together", "Image with pieces", "Interlocking pieces", "Used for entertainment"],

    # Hints for 'jinx'
    ["Curse or spell", "Bring bad luck", "Superstitious belief", "Hex", "Misfortune"],

    # Hints for 'jiujitsu'
    ["Martial art", "Japanese fighting style", "Focus on grappling", "Self-defense technique", "Submission holds"],

    # Hints for 'jockey'
    ["Horse rider", "Rides in races", "Professional rider", "Competitor on horseback", "Racing sport"],

    # Hints for 'jogging'
    ["Light running", "Exercise activity", "Slow pace", "Running for fitness", "Leisurely run"],

    # Hints for 'joking'
    ["Making fun", "Humorous remarks", "Light-hearted banter", "Playing with words", "Not serious"],

    # Hints for 'jovial'
    ["Cheerful", "Good-humored", "Happy and friendly", "Joyful demeanor", "Light-hearted"],

    # Hints for 'joyful'
    ["Full of happiness", "Delighted", "Exuberant", "Cheerful", "Greatly pleased"],

    # Hints for 'juicy'
    ["Full of juice", "Moist and flavorful", "Succulent", "Rich in liquid", "Tasty and refreshing"],

    # Hints for 'jukebox'
    ["Music player", "Coin-operated", "Plays records", "Vintage machine", "Popular in diners"],

    # Hints for 'jumbo'
    ["Very large", "Oversized", "Huge", "Giant", "Extra big"],

    # Hints for 'kayak'
    ["Small boat", "Paddled by hand", "Narrow watercraft", "Used for paddling", "Can be solo or double"],

    # Hints for 'kazoo'
    ["Simple musical instrument", "Buzzing sound", "Played by humming", "Toy instrument", "Popular in children’s music"],

    # Hints for 'keyhole'
    ["Lock opening", "Hole for a key", "Where you insert a key", "Small opening", "Part of a lock"],

    # Hints for 'khaki'
    ["Light brown color", "Military uniform color", "Earthy tone", "Popular in pants", "Neutral color"],

    # Hints for 'kilobyte'
    ["Data measurement", "1024 bytes", "Small unit of data", "Used in computing", "Memory size"],

    # Hints for 'kiosk'
    ["Small structure", "Information stand", "Vendor booth", "Self-service terminal", "Miniature building"],

    # Hints for 'kitsch'
    ["Lowbrow art", "Cheap and gaudy", "Popular in pop culture", "Inexpensive decorations", "Often in bad taste"],

    # Hints for 'kiwifruit'
    ["Green fruit", "Fuzzy exterior", "Tart taste", "Also known as Chinese gooseberry", "Popular in salads"],

    # Hints for 'klutz'
    ["Clumsy person", "Accident-prone", "Awkward and graceless", "Uncoordinated", "Frequently drops things"],

    # Hints for 'knapsack'
    ["Backpack", "Carried on shoulders", "Outdoor gear", "Used for hiking", "Storage bag"],

    # Hints for 'larynx'
    ["Voice box", "Part of throat", "Contains vocal cords", "Responsible for speech", "Located in the neck"],

    # Hints for 'lengths'
    ["Measurement units", "Extent from end to end", "Distance", "Size of an object", "Long dimensions"],

    # Hints for 'lucky'
    ["Fortunate", "Bringing good luck", "Positive outcome", "Serendipitous", "Favorable circumstances"],

    # Hints for 'luxury'
    ["High-end quality", "Opulence", "Expensive and comfortable", "Exclusive", "Indulgence"],

    # Hints for 'lymph'
    ["Fluid in body", "Part of immune system", "Clear and watery", "Circulates in lymphatic system", "Contains white blood cells"],

    # Hints for 'marquis'
    ["Noble rank", "High aristocracy", "Historical title", "Rank above earl", "Nobleman"],

    # Hints for 'matrix'
    ["Grid of numbers", "Mathematical array", "Organizational framework", "Rectangular arrangement", "Used in algebra"],

    # Hints for 'megahertz'
    ["Frequency unit", "One million hertz", "Measurement of radio waves", "Used in electronics", "Radio frequency"],

    # Hints for 'microwave'
    ["Kitchen appliance", "Cooks food quickly", "Uses electromagnetic waves", "Heats food", "Radiant heat"],

    # Hints for 'mnemonic'
    ["Memory aid", "Learning tool", "Helps recall information", "Mnemonic device", "Aids in memorization"],

    # Hints for 'mystify'
    ["Confuse or puzzle", "Cause bewilderment", "Make unclear", "Mystical or enigmatic", "Create uncertainty"],

    # Hints for 'naphtha'
    ["Flammable liquid", "Used in fuels", "Hydrocarbon compound", "Volatile solvent", "Derived from petroleum"],

    # Hints for 'nightclub'
    ["Entertainment venue", "Open late", "Music and dancing", "Social gathering place", "Club with a bar"],

    # Hints for 'nowadays'
    ["Current times", "Present day", "Modern era", "Contemporary period", "Recent times"],

    # Hints for 'numbskull'
    ["Foolish person", "Dull-witted", "Not smart", "Simple-minded", "Dim-witted"],

    # Hints for 'nymph'
    ["Mythical creature", "Nature spirit", "Female deity", "Young and beautiful", "Classical mythology"],

    # Hints for 'onyx'
    ["Black gemstone", "Layered quartz", "Used in jewelry", "Smooth and polished", "Dark-colored stone"],

    # Hints for 'ovary'
    ["Female reproductive organ", "Produces eggs", "Part of reproductive system", "Hormone-secreting gland", "Located in pelvis"],

    # Hints for 'oxidize'
    ["Chemical reaction", "Combine with oxygen", "Rusting process", "Forms oxides", "Corrosion"],

    # Hints for 'oxygen'
    ["Essential for breathing", "Element in the air", "Supports combustion", "Chemical symbol O", "Vital for life"],

    # Hints for 'pajama'
    ["Sleepwear", "Comfortable clothing", "Worn at night", "Two-piece set", "Loungewear"],

    # Hints for 'peekaboo'
    ["Children's game", "Hide and reveal", "Playful interaction", "Surprise element", "Often with babies"],

    # Hints for 'phlegm'
    ["Mucus in throat", "Body fluid", "Produced by respiratory system", "Thick and sticky", "Related to illness"],

    # Hints for 'pixel'
    ["Picture element", "Tiny screen unit", "Smallest image part", "Digital image component", "Display resolution"],

    # Hints for 'pizazz'
    ["Excitement and flair", "Vibrant quality", "Stylish and lively", "Extra charm", "Sparkle"],

    # Hints for 'pneumonia'
    ["Lung infection", "Inflammation of lungs", "Respiratory illness", "Causes coughing", "Medical condition"],

    # Hints for 'polka'
    ["Dance style", "Lively music", "Traditional European dance", "Two-step rhythm", "Energetic"],

    # Hints for 'pshaw'
    ["Dismissive sound", "Expression of disbelief", "Showing scorn", "Sound of disapproval", "Lightly contemptuous"],

    # Hints for 'psyche'
    ["Mind and spirit", "Psychological self", "Inner self", "Mental processes", "Emotional and intellectual"],

    # Hints for 'puppy'
    ["Young dog", "Canine baby", "Playful and cute", "Newborn dog", "Puppy love"],

    # Hints for 'puzzling'
    ["Confusing", "Hard to solve", "Mystifying", "Requires thought", "Challenging"],

    # Hints for 'quartz'
    ["Mineral", "Common gemstone", "Silicon dioxide", "Used in watches", "Crystal structure"],

    # Hints for 'queue'
    ["Line of people", "Waiting in order", "Process of waiting", "Sequence", "Line-up"],

    # Hints for 'quips'
    ["Clever remarks", "Witty comments", "Short and amusing", "Quick jokes", "Humorous statements"],

    # Hints for 'quixotic'
    ["Idealistic and unrealistic", "Romantic and impractical", "Dreamy and impractical", "Chivalrous", "Unrealistic goals"],

    # Hints for 'quiz'
    ["Test of knowledge", "Short assessment", "Questionnaire", "Educational game", "Quick evaluation"],

    # Hints for 'quizzes'
    ["Multiple tests", "Series of questions", "Assessments", "Educational activities", "Short exams"],

    # Hints for 'quorum'
    ["Minimum number for decision", "Required attendees", "Group minimum", "Decision-making group", "Legal minimum"],

    # Hints for 'razzmatazz'
    ["Showiness", "Flamboyant display", "Excitement and show", "Entertainment flair", "Attention-getting"],

    # Hints for 'rhubarb'
    ["Plant with tart stalks", "Used in pies", "Vegetable with red stalks", "Often cooked with sugar", "Edible plant"],

    # Hints for 'rhythm'
    ["Pattern of sounds", "Musical timing", "Beat in music", "Regular pattern", "Flow of movement"],

    # Hints for 'rickshaw'
    ["Human-powered vehicle", "Transport in Asia", "Two-wheeled cart", "Pulled by a person", "Passenger carriage"],

    # Hints for 'schnapps'
    ["Strong liquor", "Flavored spirit", "Alcoholic beverage", "Popular in Germany", "Distilled drink"],

    # Hints for 'scratch'
    ["Small cut or mark", "Skin irritation", "To rub with nails", "Surface damage", "Minor injury"],

    # Hints for 'shiv'
    ["Improvised knife", "Sharp object", "Used as a weapon", "Homemade blade", "Prison shank"],

    # Hints for 'snazzy'
    ["Stylish and fashionable", "Attractive appearance", "Trendy", "Eye-catching", "Modern"],

    # Hints for 'sphinx'
    ["Mythical creature", "Lion with human head", "Ancient Egyptian statue", "Riddle guardian", "Legendary figure"],

    # Hints for 'spritz'
    ["Light spray", "Quick burst", "Refreshing drink", "Light mist", "Alcoholic beverage"],

    # Hints for 'squawk'
    ["Loud noise", "Harsh cry", "Bird call", "Sharp sound", "Squawking noise"],

    # Hints for 'staff'
    ["Group of employees", "Workforce", "Team members", "Organizational personnel", "Support team"],

    # Hints for 'strength'
    ["Physical power", "Force or vigor", "Ability to withstand", "Power and resilience", "Muscular capability"],

    # Hints for 'strengths'
    ["Positive qualities", "Areas of advantage", "Personal assets", "Strong points", "Capabilities"],

    # Hints for 'stretch'
    ["Extend lengthwise", "Lengthen something", "Increase reach", "Elasticity", "Expand"],

    # Hints for 'stronghold'
    ["Fortified place", "Military base", "Secure position", "Defensive structure", "Protected area"],

    # Hints for 'stymied'
    ["Blocked progress", "Hindered", "Prevented advancement", "Frustrated effort", "Obstructed"],

    # Hints for 'subway'
    ["Underground train", "Metro system", "Urban transportation", "Rapid transit", "City train"],

    # Hints for 'swivel'
    ["Rotate around a point", "Pivoting motion", "Turn on a central axis", "Swivel chair", "Adjustable movement"],

    # Hints for 'syndrome'
    ["Medical condition", "Group of symptoms", "Health disorder", "Collection of signs", "Specific medical pattern"],

    # Hints for 'thriftless'
    ["Wasteful with money", "Careless spending", "Lacking frugality", "Squanders resources", "Unwise with finances"],

    # Hints for 'thumbscrew'
    ["Old torture device", "Screw-like tool", "Applied pressure", "Historical instrument", "Used for punishment"],

    # Hints for 'topaz'
    ["Yellow gemstone", "Precious stone", "Variety of quartz", "Used in jewelry", "Hard and durable"],

    # Hints for 'transcript'
    ["Written record", "Document of speech", "Text version of audio", "Typed copy", "Official record"],

    # Hints for 'trivial'
    ["Minor importance", "Of little significance", "Insignificant details", "Not serious", "Petty or small"],

    # Hints for 'vortex'
    ["Whirling mass", "Spiral motion", "Circular flow", "Swirling fluid", "Turbulent center"],

    # Hints for 'waltz'
    ["Dance style", "Three-quarter time", "Elegant ballroom dance", "Partnered dance", "Graceful movement"],

    # Hints for 'whiz'
    ["Move quickly", "Speedy motion", "Quick action", "Fast mover", "Swift"],

    # Hints for 'woolly'
    ["Covered in wool", "Fuzzy texture", "Soft and warm", "Like wool fabric", "Fluffy appearance"],

    # Hints for 'xylophone'
    ["Musical instrument", "Wooden bars", "Played with mallets", "Percussion instrument", "Tuned bars"],

    # Hints for 'yacht'
    ["Luxury boat", "Sailing vessel", "Recreational watercraft", "Used for leisure", "Elegantly designed"],

    # Hints for 'yawn'
    ["Opening mouth wide", "Tiredness response", "Involuntary action", "Stretching mouth", "Sign of sleepiness"],

    # Hints for 'zebra'
    ["Striped animal", "Black and white stripes", "Native to Africa", "Herbivorous mammal", "Equid family"],

    # Hints for 'zephyr'
    ["Gentle breeze", "Soft wind", "Mild and pleasant", "Light air movement", "West wind"],

    # Hints for 'zodiac'
    ["Astrological signs", "Twelve signs", "Celestial belt", "Used in horoscopes", "Star signs"],

  #Hints for 'zombie'
  ["undead", "green", "like brains", "were once humans", "walking dead"]
]
