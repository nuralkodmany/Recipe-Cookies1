#Recipe for chocolate chip cookies
#http://www.foodnetwork.com/recipes/food-network-kitchen/chewy-chocolate-chip-cookies-3362960

#Dictionary for steps
#list for ingredients

ingredients = ['all-purpose flour','baking soda', 'fine salt','unsalted butter','light brown sugar', 'granulated sugar','large eggs', 'pure vanilla extract', 'semisweet chocolate chips']
measurements = ['2 1/4 cups','3/4 tsp', '1/2 tsp', '1 stick', '1 cup', '1/2 cup', '2', '2 tsp','12 oz']

#ingredientsDict = dict(zip(ingredients,measurements))
#print (ingredientsDict)
print ('Measurements \t\t Ingredients')
for ingredients,measurements in zip(ingredients,measurements):
    print (measurements + '\t\t' + ingredients)


steps = '1. Preheat the oven to 375 degrees F. Line a baking sheet with parchment paper.', '2. Whisk together the flour, baking soda and salt in a medium bowl and set aside.', '3.Beat the butter, brown sugar and granulated sugar with an electric mixer on medium-high speed in a large bowl until well combined, about 2 minutes.', '4. Add the eggs and vanilla and beat until light in color, 2 to 3 minutes. Add the flour mixture and mix on low speed until well incorporated. Fold in the chocolate chips by hand using a rubber spatula.', '5. Using a small scoop or tablespoon, drop level tablespoonfuls of dough onto the prepared baking sheet, about 2 inches apart. (You should be able to fit about a dozen cookies.) Bake until golden around the edges and soft-set in the centers, 12 to 15 minutes.', '6.  Cool the cookies on the baking sheet for 5 minutes, and then remove to a rack to cool completely. Repeat with the remaining dough, baking 3 batches total.'

print ("\nsteps")

for number in steps:
    print (number)
