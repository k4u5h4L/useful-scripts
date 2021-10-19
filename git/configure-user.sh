#!/bin/sh

git config user.name "Kaushal"
git config user.email "1nt18is076.kaushal@nmit.ac.in"

echo "User name set to:"
git config user.name

echo ""
echo "--"
echo ""

echo "User email set to:"
git config user.email

echo ""
echo ""

echo "Do you want to set custom git credential cache timeout?"

read -p "[y/N]: " choice

if [ $choice == "y" ] || [ $choice == "yes" ] || [ $choice == "Y" ] || [ $choice == "YES" ]
then
        read -p "Enter value (in seconds): " seconds
        val="'cache --timeout=${seconds}'"
        # echo $val
        git config credential.helper "$val"

        echo "Credential Cache set to ${seconds} seconds"

else
        echo "Keeping the default value, which is 15 mins"
fi

# ----------

echo ""
echo ""

echo "Do you want view the config you have set right now?"

read -p "[y/N]: " choice

if [ $choice == "y" ] || [ $choice == "yes" ] || [ $choice == "Y" ] || [ $choice == "YES" ]
then
        git config --list

else
        echo "Ok, exiting..."
fi
