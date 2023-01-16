# Cat Or Dog

> My first AI

# Description

> Simply, this AI detects a photo from your PC or an URL and give you are response if it's a cat or a dog

# Set-up
> Creating AI

> Delete the text files in "result", "models", "data" folders

> In "data" folder you have to add a datastore a.k.a photos of cats and dogs ( this will teach your AI to make a difference between cats and dogs ). I used this datastore: https://www.microsoft.com/en-us/download/details.aspx?id=54765

> After downloading the datastore, place the 2 folders in "data" folder and run AI.py ( this will create your AI's brain and will save it in "models" folder )

> Now you have an AI that can recognize cats and dogs ( up to 97% )

> If you want to have more precise AI, you have to add more photos to your data :)

# Usage

> Comparing

> Now you can choose an image from internet and download it or copy the link, then you have to run the second python script "cat_or_dog.py"

> Press 1 to use the image link or 2 to select it from your PC

> If you are using the first option, it will automatically download the image and place it in "results" folder and give it a name ( dog.png or cat.png * it depends on the result obv* )

> Keep in mind that there is a 3% chance that the AI will make a mistake. :)

#Extra information

> I found many codes of creating this AI but they are ALL OUTDATED becauseee the newest version of TensorFlow requires your image to be (1, 224, 224, 3) so I had to reshape the image and change the transparency by using the CV2 module ( not the TensorFlow module as it's supposed to be ). Maybe that's not the best performance option, but it works perfectly if you want to test out what AI can do. I haven't test it for with a big amount of requests but I do not recommend it for large tasks ( comparing thousands images at the same time )
