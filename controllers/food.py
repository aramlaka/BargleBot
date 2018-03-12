import random
import discord
import defaults

from clientWrapper import client


foodItems = [':green_apple:', ':apple:', ':pear:', ':tangerine:', ':tangerine:', ':lemon:', ':banana:', ':watermelon:',
             ':grapes:', ':strawberry:', ':melon:', ':cherries:', ':peach:', ':pineapple:', ':tomato:', ':eggplant:',
             ':hot_pepper:', ':corn:', ':sweet_potato:', ':honey_pot:', ':bread:', ':cheese:', ':poultry_leg:',
             ':meat_on_bone:', ':fried_shrimp:', ':cooking:', ':hamburger:', ':fries:', ':hotdog:', ':pizza:',
             ':spaghetti:',
             ':taco:', ':burrito:', ':ramen:', ':stew:', ':fish_cake:', ':sushi:', ':bento:', ':curry:', ':rice_ball:',
             ':rice:', ':rice_cracker:', ':oden:', ':dango:', ':shaved_ice:', ':ice_cream:', ':icecream:', ':cake:',
             ':birthday:', ':custard:', ':candy:', ':lollipop:', ':chocolate_bar:', ':popcorn:', ':doughnut:',
             ':cookie:',
             ':beer:', ':beers:', ':wine_glass:', ':cocktail:', ':tropical_drink:', ':champagne:', ':sake:', ':tea:',
             ':coffee:', ':baby_clienttle:', ':croissant:', ':avocado:', ':cucumber:', ':bacon:', ':potato:', ':carrot:',
             ':french_bread:', ':salad:', ':shallow_pan_of_food:', ':stuffed_flatbread:', ':tumbler_glass:', ':egg:',
             ':milk:', ':peanuts:', ':kiwi:', ':pancakes:']


@client.command()
async def food(context):
    await context.send(random.choice(foodItems))


@client.command()
async def menu(context):
    embed = discord.Embed(title=context.guild.name + " Menu", description="Seasonal Menu",
                          color=defaults.CLIENT_COLOR)

    for x in range(random.randint(1, 15)):
        foodItem = random.choice(foodItems)
        foodName = list(foodItem.replace(':', '').replace('_', ' '))
        random.shuffle(foodName)
        foodName = ''.join(foodName).title()
        foodPrice = random.randint(1, 1000)

        embed.add_field(name=foodItem + " - " + foodName,
                        value="$" + str(foodPrice), inline=True)

    await context.send(embed=embed)