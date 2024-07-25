# Start
echo "Helo world!"

age=10
name=$(echo "Vishnu")
echo $age + $name

# Constants
readonly country="India"
echo "Country $country"

# Inputs
read -p "What is your name? " yourname
echo "Your name is $yourname"

read -p "What is your age? " yourage

if [ $yourage -ge 18 ]
then 
        echo "You are 18+"
else
        echo "You are not 18"
fi

if [ -f basic.sh ]
then
        echo "folder present"
else
        echo "folder not present"
fi

# All other basic operations are also possible with the specific syntax

