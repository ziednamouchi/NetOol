#!/bin/bash


#------Main Menu Fonction------------
main_menu(){

	echo "1/Subnet Calculator"
	echo "2/Packet Sniffer"
	echo "3/Email Credentials Stealing"
	echo "4/TCP Reverce Shell"
	echo "5/Read Me"
	echo "6/Exit"
}

cat tag.txt
main_menu
read -p "main menu>" choice
case $choice in 
	1) clear; python3 scripts/sub_calc.py;;
	2) clear; python scripts/Sniffer.py;;
	3) clear; echo "exec Email stealing";;
	4) clear; echo "exec TCP Reverse";;
	5) clear; echo "Read me";;
	6) clear; sh scripts/exit_script.sh ;;
	*) clear; echo "Bad choice please choice"
	   read -p "Main Menu>" choice;;

esac
