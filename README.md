Firewalld
=========

კლიენტების წვდომა გარე IP-ებით. 

ყველა IP პაკეტი რომელიც არ არის client_ips და admin_ips-ში იბლოკება. 
წვდომა კონტროლდება public და internal ზონების ფაილებით. 
ადმინისტრატორებისთვის დამატებითი სერვისები იწერება admin_services ცვლადში.
admin_ips ცვლადში ჩაწერილი IP-ები მიეკუთვნება internal ზონას. 


მოდულის გამოყენება
==================
 
1. git clone https://github.com/gurguration/ansible.git && cd ansible && ansible-playbook firewall.yml

თუ მოლეკულა გიყენიათ:

1. git clone https://github.com/gurguration/ansible.git && cd ansible/firewalld && sudo molecule test

მოლეკულას დაყანება Ubuntu-სთვის: https://www.digitalocean.com/community/tutorials/how-to-test-ansible-roles-with-molecule-on-ubuntu-16-04


ჯერჯერობით როლი მხოლოდ Centos7-ზე მუშაობს. 
-------------------------------------
License
-------

GNU GPL V3
