# List of target audiences:
working_professional = 'a working professional who would like to be able to whip up a quick but delicious weeknight meal.'

important_person = 'an important person whom you have all the time, money and energy you need to make a fancy dish that is sure to impress!'

college_student = 'a college student who requires a simple recipe that can be prepared using only a microwave.'

family = "a busy family who requires a meal which is kid-friendly, can serve multiple people, and is both nutritious and tasty for children and adults."

elderly = "an elderly or mobility impaired individual who needs easy-to-make meals that don't require a lot of physical effort, finely chopping or mincing anything, or standing for long periods of time."

meal_prepper = "an avid meal prepper who needs meal-prep ideas that can be prepared on the weekend to eat during the following week, perfect for busy schedules. Make sure to specify if any ingredients should be stored seperately after the food is prepared, i.e. lettuce stored seperately from chicken or cooked noodles stored seperately from a broth. If a cooked ingredient cannot be safely refrigerated for a week without eating, mention this."

solo_diner = "a solitary individual looking for single-serving recipes that are quick and easy to prepare and won't leave any leftovers."

health_conscious = "a health enthusiast who prefers meals that are nutritious, low in unnecessary calories, include fresh produce (possibly organic) and are high in protein when possible."

dramatis_personae = ['A working professional.', 'An important person you want to impress!', 'A busy family with children.',
                     'The elderly or mobility impaired.',
                     'A meal prepper who makes food for the entire week in one go.',
                     "A solo diner who doesn't want to deal with leftovers.",
                     "A health conscious individual who prefers food that's nutritious, high in protein and low in empty calories."]

all_audiences = {
    'A working professional.': working_professional,
    'An important person you want to impress!': important_person,
    'A busy family with children.': family,
    'The elderly or mobility impaired.': elderly,
    'A meal prepper who makes food for the entire week in one go.': meal_prepper,
    "A solo diner who doesn't want to deal with leftovers.": solo_diner,
    "A health conscious individual who prefers food that's nutritious, high in protein and low in empty calories.": health_conscious
}

# List of target cuisines
### NOTE TO SELF: NO PUNCTUATION AT END OF EITHER KEY/VALUE PAIR!) ###

cuisines = ['Nothing in particular', 'American', 'American (Cajun)', 'Chinese (Cantonese - Most common style in US)',
            'Chinese (Hong Kong)', 'Chinese (Sichuan)', 'Chinese (Shandong)', 'Chinese (Jiangsu)',
            'French', 'Greek', 'North Indian', 'South Indian', 'Italian', 'Japanese (Kansai)', 'Japanese (Kanto)',
            'Korean', 'Mexican', 'Peruvian', 'Spanish', 'Thai', 'Turkish', 'Vietnamese']

blank = {1: "", 2: ""}

indian = {1: "Indian",
          2: "tamarind, cumin (Jeera), Coriander (Dhania), Tumeric (Haldi), Caradamon (Elaichi), "
             "Mustard Seeds (Sarson), Cloves (Laung), Cinnamon (Dalchini), Fenugreeek (Methi), and Red Chili (Lal Mirch)"}

north_indian = {1: "North Indian",
                2: "tumeric (haldi), cumin (jeera), coriander (dhania), red chili powder (lal mirch), garam masala,"
                   "green cardamon (elaichi), cloves (laung), black mustard seeds (rai), fenugreek (methi), and asafoetida (hing)"}

south_indian = {1: "South Indian",
                2: "mustard seeds (rai/kadugu), curry leaves (kadi patta/karuveppilai), tamarind (imli/puli), "
                   "urad dal (ulundu paruppu/uddina bele), dried red chilies (lal mirch/sukku milagai), "
                   "fenugreek seeds (methi/vendhayam/menthulu)asafoetida (hing/perungayam/inguva), "
                   "black pepper (kali mirch/milagu), coriander seeds (dhania/dhaniya/malli), and turmeric (haldi/manjal"}

japan_kansai = {1: "Kansai (Japanese)",
                2: "dashi, Kansai shoyu (soy sauce), mirin, sake, Kansai-style miso, shichimi togarashi, sansho (Japanese pepper), "
                   "yuzu, shiso, negi (scallions or green onions), bonito flakes (katsuobushi) and konbu"}

japan_kanto = {1: "Kanto (Japanese)",
               2: "Kanto shoyu (soy sauce), dashi, wasabi, negi (scallions or green onions), ginger (shoga), nori, "
                  "sansho (Japanese pepper), red miso (akamiso), sake, and tsuyu"}

thailand = {1: "Thai",
            2: "chilies (prik), galangal (kha), lemongrass (takrai), kaffir lime leaves (bai makrut), fish sauce (nam pla), "
               "Thai basil (horapa/bai horapa), coriander and cilantro (pak chi), tamarind (makham), coconut milk (nam kati), "
               "and palm sugar (nam tan pip)"}

mexican = {1: "Mexican",
           2: "chilies (chiles), cumin (comino), cilantro and coriander (coriando), Mexican oregano (orégano), garlic (ajo), "
              "epazote, chocolate, cinnamon (canela), annatto (achiote), and lime (limón)"}

italian = {1: "Italian",
           2: "garlic (aglio), basil (basilico), oregano (origano), roesemary (rosmarino), sage (la salvia), parsley (prezzemolo), "
              "red pepper flakes (peperoncino), fennel seeds (semi di finocchio), anchovies (acciughe), and nutmeg (noce moscata)"}

french = {1: "French",
          2: "thyme (thym), bay leaf (feuille de laurier), parsley (persil), tarragon (estragon), chervil (cerfeuil), "
             "rosemary (romarin), nutmeg (noix de muscade), dijon mustard (moutarde de dijon), garlic (ail) and shallots (échalotes)"}

spanish = {1: "Spanish",
           2: "saffron (azafrán), paprika (pimentón), garlic (ajo), parsley (perejil), bay leaf (laurel), rosemary (romero), "
              "cumin (comino), thyme (tomillo), olive oil (aceite de oliva), and sherry vinegar (vinagre de jerez)"}

greek = {1: "Greek",
         2: "oregano (ρίγανη; rígani), olive oil (ελαιόλαδο; elaiólado), lemon (λεμόνι; lemóni), dill (άνηθος; ánithos), "
            "mint (δυόσμος; dyósmos), bay leaf (φύλλο δάφνης; fýllo dáfnis), cinnamon (κανέλα; kanéla), "
            "nutmeg (μοσχοκάρυδο; moschokárydo), fennel (μάραθος; márathos), and mastiha (μαστίχα; mastícha)."}

peruvian = {1: "Peruvian",
            2: "aji amarillo (ají amarillo), aji panca (ají panca), cilantro (culantro), huacatay (huacatay), cumin (comino), "
               "garlic (ajo), lime (limón), annatto (achiote), oregano (orégano), and ginger (kion)"}

vietnamese = {1: "Vietnamese",
              2: "'fish sauce (nước mắm), lemongrass (xả), lime (chanh), ginger (gừng), turmeric (nghệ), "
                 "Vietnamese coriander (rau răm), Thai basil (húng quế), mint (húng lủi), star anise (đại hồi), "
                 "and green onions or scallions (hành lá)'"}
turkish = {1: "Turkish",
           2: "red pepper flakes (pul biber), sumac (sumak), mint (nane), cumin (kimyon), allspice (yenibahar), "
              "sesame seeds (susam), pomegranate molasses (nar ekşisi), fenugreek (çemen), oregano (kekik), and bay leaf (defne yaprağı)"}

korean = {1: "Korean",
          2: "kimchi (김치), (red pepper flakes (gochugaru, 고추가루), red pepper paste (gochujang, 고추장), soybean paste (doenjang, 된장), "
             "soy sauce (ganjang, 간장), garlic (maneul, 마늘), ginger (saenggang, 생강), green onions or scallions (pa, 파), "
             "sesame oil (chamgireum, 참기름), sesame seeds (chamggae, 참깨), and perilla leaves (kkaennip, 깻잎)"}

american = {1: "American",
            2: "black pepper, salt, garlic, onion, paprika, chili powder, cayenne pepper, cinnamon, oregano, vanilla extract and old bay"}

cajun = {1: "Cajun",
         2: "cayenne pepper, paprika, garlic, onion, bell peppers, celery, file powder, bay leaves, thyme and cajun seasoning"}

china_hong_kong = {1: "Hong Kong",
                   2: "five-spice powder (五香粉; wǔ xiāng fěn), star anise (八角; bā jiǎo), ginger (薑; gīng), "
                      "green onions or scallions (蔥; cōng), garlic (蒜; suàn), oyster sauce (蠔油; háo yóu), "
                      "soy sauce (醬油; jiàng yóu), sesame oil (芝麻油; zhī ma yóu), fermented black beans (豆豉; dòu chǐ), "
                      "and hoisin sauce (海鮮醬; hǎi xiān jiàng)"}

china_sichuan = {1: "Sichuan (Chinese)",
                 2: "Sichuan peppercorns (hua jiao, 花椒), dried chili peppers (gan la jiao, 干辣椒), broad bean chili paste (doubanjiang, 豆瓣酱), "
                    "garlic (suan, 蒜), ginger (jiang, 姜), green onions or scallions (cong, 葱), pickled vegetables (pao cai, 泡菜), "
                    "star anise (ba jiao, 八角), fermented black beans (douchi, 豆豉) and five-spice powder (wu xiang fen, 五香粉)"}

china_shangdong = {1: "Shangdong/Lue (Chinese)",
                   2: "green onions or scallions (cong, 葱), ginger (jiang, 姜), garlic (suan, 蒜), soy sauce (jiang you, 酱油), "
                      "rice wine (mi jiu, 米酒), sesame oil (zhi ma you, 芝麻油), star anise (ba jiao, 八角), "
                      "dried chinese black mushrooms (mu er, 木耳) and vinegar (cu, 醋)"}

china_cantonese = {1: "Cantonese/Guandong/Yue (Chinese)",
                   2: "ginger (jiang, 姜), green onions (cong, 葱), garlic (suan, 蒜), soy sauce (jiang you, 酱油), "
                      "oyster sauce (hao you, 蚝油), fermented black beans (douchi, 豆豉), sesame oil (zhi ma you, 芝麻油), "
                      "rice wine (mi jiu or shaoxing jiu, 米酒 or 绍兴酒), white pepper (bai hu jiao, 白胡椒), and dried tangerine peel (chen pi, 陈皮)"}

china_jiangsu = {1: "Huaiyang/Jianghuai(Chinese)",
                 2: "ginger (jiang, 姜), green onions or scallions (cong, 葱), rice wine (mi jiu or shaoxing jiu, 米酒 or 绍兴酒), "
                    "soy sauce (jiang you, 酱油), sugar (tang, 糖), vinegar (cu, 醋), sesame oil (zhi ma you, 芝麻油), "
                    "red fermented tofu (nan ru or fu ru, 南乳 or 腐乳), dried bamboo shoots (gan sun, 干笋), and "
                    "osmanthus syrup (gui hua tang, 桂花糖)"}

## Actual targets (for testing)
target_cuisine = {1: "", 2: ""}

all_cuisines = {
    'Nothing in particular': blank,
    'American': american,
    'American (Cajun)': cajun,
    'Chinese (Cantonese - Most common style in US)': china_cantonese,
    'Chinese (Hong Kong)': china_hong_kong,
    'Chinese (Sichuan)': china_sichuan,
    'Chinese (Shandong)': china_shangdong,
    'Chinese (Jiangsu)': china_jiangsu,
    'French': french,
    'Greek': greek,
    'North Indian': north_indian,
    'South Indian': south_indian,
    'Italian': italian,
    'Japanese (Kansai)': japan_kansai,
    'Japanese (Kanto)': japan_kanto,
    'Korean': korean,
    'Mexican': mexican,
    'Peruvian': peruvian,
    'Spanish': spanish,
    'Thai': thailand,
    'Turkish': turkish,
    'Vietnamese': vietnamese
}

# Definining dietary restrictions

all_restrictions = {
    "Halal": "The recipe must be halal. Halal food complies with Islamic dietary laws, forbidding pork and alcohol, "
             "and requiring that animals be slaughtered in a specific manner with a blessing.",
    "Vegan": "The recipe must be vegan. Vegan food contains no animal products at all, including those that do not harm "
             "or kill the animal in their harvest, such as eggs, milk, butter, and honey.",
    "Gluten-free": "The recipe must be gluten-free. Gluten-free food excludes gluten, a protein found in grains "
                   "like wheat, barley, and rye, and is suitable for those with celiac disease or gluten sensitivity. "
                   "Most types of flour contain gluten and are not gluten-free.",
    "Kosher": "The recipe must be kosher. Kosher food adheres to Jewish dietary laws, prohibiting pork and "
              "shellfish, requiring meat and dairy to be consumed separately, and mandating specific animal slaughter methods.",
    "Keto": "The recipe must be keto. Keto (ketogenic) food is low in carbohydrates and high in fats and protein, "
            "aiming to induce a state of ketosis in the body, where fat is burned for energy instead of carbs.",
    "Vegetarian": "The recipe must be vegetarian. Vegetarian food excludes meat, fish, and poultry, "
                  "but can include ingredients that do not kill the animal in harvesting them, including milk, butter, "
                  "other dairy products, honey and eggs.",
    "Free of major food allergens": "The recipe must be free of the eight major food allergens identified by the"
                                    "FALCA Act. The recipe can NOT contain these eight ingredients: milk, eggs, "
                                    "fish (such as bass, flounder, cod), crustacean shellfish (such as crab, lobster, shrimp), "
                                    "tree nuts (such as almonds, walnuts, pecans), peanuts, wheat, and soybeans.",
    "Low calorie": "The recipe must be low calorie. This indicates that the food should have a reduced calorie count,"
                   " typically beneficial for weight management.",
    "Diabetic": "The recipe must be suitable for diabetics. This usually means low in sugar and carbohydrates, "
                "with a focus on foods that have a low glycemic index to manage blood sugar levels."
}

# Fixing the prompt to accommodate target cuisine being left blank:



def generate_prompt(target_audience, target_cuisine, dessert=False, dietary_restrictions=None):
    if not target_cuisine == blank:
        intro_phrase = (
            f"from {target_cuisine[1]} cuisine, keeping in mind that the audience for your recipe is an enthusiast and expert in {target_cuisine[1]} "
            f"cuisine who would like you to prepare a dish with authentic {target_cuisine[1]} spices and flavors. "
            f"Make sure the recipe you suggest includes such classic {target_cuisine[1]} spices and flavors as {target_cuisine[2]}")
    else:
        intro_phrase = "from any cuisine or culture"
    if not target_cuisine == blank:
        conjunction = {1: "as well as", 2: ","}
    else:
        conjunction = {1: "", 2: ""}

    # Handle dietary restrictions
    dietary_restrictions_text = ""
    if dietary_restrictions:
        restrictions_list = [all_restrictions[restriction] for restriction in dietary_restrictions]
        if restrictions_list:
            dietary_restrictions_text = "In addition, the recipe you generate must meet the following dietary requirements. Please acknowledge your awareness of these dietary requirements in your response. " + ', '.join(
                restrictions_list) + ". "

    if not dessert:
        string = f'''
    Respond as if you were an acclaimed popular food blogger, renown for their knowledge of cooking fundamentals, their 
    flair for modern creativity, and their ability to break things down into straight-forward steps that anyone can follow. 

    You are being asked to prepare a recipe for {target_audience} . They will provide you with a list of ingredients to use in the recipe. If you are not given any food items to use, please decline to generate a recipe.

    {dietary_restrictions_text}

    Please suggest a recipe from {intro_phrase}. Your recipe may include other pantry staples such as butter, oil, salt and 
    pepper, herbs and spices, and milk, {conjunction[1]}  such classic {target_cuisine[1]} spices and flavors as {target_cuisine[2]}{conjunction[2]} 
    but otherwise the primary ingredients for the recipe should come ONLY from the ingredients wrapped in triple quotes in the user message below. 

    Please keep in mind that you cannot include any non-food or harmful ingredients in your recipe. If you are asked to provide
    a recipe using such ingredients, you will decline, or explain that you will provide a recipe that omits the non-food or 
    dangerous ingredients. You do not need to use every ingredient provided in the user message below in your recipe, but you should do your best to use as many as possible."
    '''
        return string

    else:
        string = f'''
        Respond as if you were an acclaimed popular food blogger, renown for their knowledge of cooking fundamentals, their 
        flair for modern creativity, and their ability to break things down into straight-forward steps that anyone can follow. 

        You are being asked to prepare a recipe for {target_audience}  Your target audience would like a DESSERT recipe! They will provide you with a list of ingredients to use in the recipe. If you are not given any food items to use, please decline to generate a recipe.

        {dietary_restrictions_text}

        Please suggest a recipe from {intro_phrase}. Your recipe may include other pantry staples such as butter, oil, salt and 
        pepper, brown and white sugar, herbs and spices, and milk, {conjunction[1]}   classic {target_cuisine[1]} spices and flavors{conjunction[2]} 
        but otherwise the primary ingredients for the recipe should come ONLY from the ingredients wrapped in triple quotes in the user message below. 

        Please keep in mind that you cannot include any non-food or harmful ingredients in your recipe. If you are asked to provide
        a recipe using such ingredients, you will decline, or explain that you will provide a recipe that omits the non-food or 
        dangerous ingredients. You do not need to use every ingredient provided in the user message below in your recipe, but you should do your best to use as many as possible. 
        And again, remember, your target audience wants you to try to create a recipe for a dessert. Don't include in the recipe you generate any ingredients inappropriate for a dessert."
        '''
        return string


print("MICROPHONE TESTING 1 2 3")
print(f'The value of all_cuisines[American (Cajun)] is {all_cuisines["American (Cajun)"]}')

print(all_cuisines['Nothing in particular'])

print(generate_prompt(target_audience=all_audiences['A working professional.'],
                      target_cuisine=all_cuisines['American (Cajun)'], dessert=True))